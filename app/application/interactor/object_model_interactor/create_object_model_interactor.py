from presentation.request_param.object_model.create_object_model_param import CreateObjectModelParam
from application.interactor.object_model_interactor.abs_create_object_model_interactor import AbsCreateObjectModelInteractor
from application.service.object_model_service.abs_create_object_model_app_service import AbsCreateObjectModelAppService
from application.service.camera_service.abs_create_camera_app_service import AbsCreateCameraAppService
import base64
import hashlib
import random
import os
from PIL import Image
import domain.helper.storage_helper as storage_helper
from domain.entity.camera_database import CameraDatabase
from injector import inject


class CreateObjectModelInteractor(AbsCreateObjectModelInteractor):
    @inject
    def __init__(
        self,
        object_model_app_service: AbsCreateObjectModelAppService,
        camera_app_service: AbsCreateCameraAppService
    ):
        self.__object_model_app_service = object_model_app_service
        self.__camera_app_service = camera_app_service
        
    def handle(self, input):
        # イメージの取得
        images = list(map(lambda x: base64.b64decode(x.encode()), input['images']))
        # 画像を一時保存する
        dirname = hashlib.sha256(str(random.random()).encode()).hexdigest()
        exif = self.__get_exif_list(dirname, images)
                
        # EXIFにモデル情報が存在するか
        if not self.__needs_focal_length(exif):
            return {"error_code": 1002, "msg": "invalid image"}
        
        # EXIFのmodel情報がすべて同じか
        if not self.__is_all_model(exif):
            return {"msg": "error"}
        
        object_model = self.__object_model_repository.FindByHash(hash)
        if not object_model:
            return {"msg": f"invalid hash {hash}"}
        
        # ローカルのカメラデータベースに存在するかを確認
        camera_database = CameraDatabase()
        camera_database.load()
        camera = next(filter(
            lambda x: x['model'] == exif[0]['model_name'], camera_database.getDataBase()
        ))
        
        # 存在しない場合は新規に登録する
        if not camera:
            model_name = exif[0]['model_name']
            focal_length = float(exif[0]['focal_length'])
            self.__camera_app_service.handle(model_name, focal_length)
            
        # 二重登録防止
        if object_model["process_histories"]:
            return {"msg": "process is duplicated"}
        # PIDを登録する
        pid = os.getpid()
        
        create_object_model_param = CreateObjectModelParam(object_model["id"], pid)
        self.__object_model_app_service.handle(create_object_model_param)

    
    def __is_all_model(self, exif_list):
        model = exif_list[0]['model']
        for exif in exif_list:
            if exif['model'] != model:
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
        for image in images:
            image_hash = hashlib.sha256(image).hexdigest()
            os.makedirs(f"./storage/{dirname}/input", exist_ok=True)
            self.__save_image(f"./storage/{dirname}/input/{image_hash}", image)
            img = Image.open(f'./storage/{dirname}/input/{image_hash}.jpg')
            data = img.getdata()
            if img._getexif():
                exif_list.append(img._getexif())
                
        return exif_list
        
        
    def __needs_focal_length(self, exif_list):
        for exif in exif_list:
            if "model" not in exif or exif["model"] == "":
                return False
        return True