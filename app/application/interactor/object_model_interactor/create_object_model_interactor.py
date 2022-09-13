from presentation.request_param.object_model.create_object_model_param import CreateObjectModelParam
from presentation.request_param.interactor.object_model.create_object_model_param import CreateObjectModelParam as CreateObjectModelInteractorParam
from application.interactor.object_model_interactor.abs_create_object_model_interactor import AbsCreateObjectModelInteractor
from application.service.object_model_service.abs_create_object_model_app_service import AbsCreateObjectModelAppService
from application.service.camera_service.abs_create_camera_app_service import AbsCreateCameraAppService
from domain.repository.object_model_repository import AbsObjectModelRepository
import base64
import hashlib
import random
import os
from PIL import Image
import domain.helper.storage_helper as storage_helper
from domain.entity.camera_database import CameraDatabase
from injector import inject
from flask import make_response, jsonify


class CreateObjectModelInteractor(AbsCreateObjectModelInteractor):
    @inject
    def __init__(
        self,
        object_model_app_service: AbsCreateObjectModelAppService,
        camera_app_service: AbsCreateCameraAppService,
        object_model_repository: AbsObjectModelRepository
    ):
        self.__object_model_app_service = object_model_app_service
        self.__camera_app_service = camera_app_service
        self.__object_model_repository = object_model_repository
        
    def handle(self, input: CreateObjectModelInteractorParam):
        # イメージの取得
        images = input.get_images()
        images = list(map(lambda x: base64.b64decode(x.replace('data:image/jpeg;base64,', '', 1).encode()), images))
        hash = input.get_hash()
        # 画像を一時保存する
        dirname = hashlib.sha256(str(random.random()).encode()).hexdigest()
        exif = self.__get_exif_list(dirname, images)
                
        # EXIFにモデル情報が存在するか
        if not self.__needs_focal_length(exif):
            return make_response(jsonify({"error_code": 1002, "msg": "invalid image"}), 404)
        
        # EXIFのmodel情報がすべて同じか
        if not self.__is_all_model(exif):
            return make_response(jsonify({"msg": "error"}), 400)
        
        object_model = self.__object_model_repository.FindByHash(hash)
        if not object_model:
            return make_response(jsonify({"msg": f"invalid hash {hash}"}), 400)
        
        # ローカルのカメラデータベースに存在するかを確認
        camera_database = CameraDatabase()
        camera_database.load()
        camera = next(filter(
            lambda x: x['model'] == exif[0][272],
            camera_database.getDataBase()
        ), None)
        
        # 存在しない場合は新規に登録する
        if not camera:
            maker_name = exif[0][271]
            model_name = exif[0][272]
            focal_length = float(exif[0][37386])
            self.__camera_app_service.handle(maker_name, model_name, focal_length)
            
        # 二重登録防止
        if "process_histories" in object_model:
            return {"msg": "process is duplicated"}
        # PIDを登録する
        pid = os.getpid()
        
        create_object_model_param = CreateObjectModelParam(object_model["id"], pid, dirname)
        try:
            ret = self.__object_model_app_service.handle(create_object_model_param)
            return make_response(jsonify(ret), 200)
        except:
            return make_response(jsonify({"message": "error"}), 400)

    
    def __is_all_model(self, exif_list):
        model = exif_list[0][272]
        for exif in exif_list:
            if exif[272] != model:
                return False
        return True
        
    def __save_image(self, dirname: str, data: bytes):
        #image_path = hashlib.sha256(data).hexdigest()
        # JPGとして保存する
        #file_path = "/".join(['.', dirname, 'input', image_path + '.jpg'])
        file_path = dirname + ".jpg"
        storage_helper.save(data, file_path)
        
    def __get_exif_list(self, dirname:str, images):
        exif_list = []
        image_dir = f"./storage/{dirname}/input"
        os.makedirs(image_dir, exist_ok=True)
        os.makedirs(f"./storage/{dirname}/output", exist_ok=True)
        os.makedirs(f"./storage/{dirname}/output/reconstruction_sequential", exist_ok=True)
        os.makedirs(f"./storage/{dirname}/output/reconstruction_global", exist_ok=True)
        os.makedirs(f"./storage/{dirname}/output/matches", exist_ok=True)
        
        for image in images:
            image_hash = hashlib.sha256(image).hexdigest()
            file_path = image_dir + f"/{image_hash}"
            self.__save_image(file_path, image)
            img = Image.open(file_path + '.jpg')
            #img.getdata()
            if img._getexif():
                exif_list.append(img._getexif())
                
        return exif_list
        
        
    def __needs_focal_length(self, exif_list):
        for exif in exif_list:
            if exif[272] == "":
                return False
        return True