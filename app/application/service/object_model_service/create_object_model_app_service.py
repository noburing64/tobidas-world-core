from presentation.request_param.object_model.create_object_model_param import CreateObjectModelParam
from application.service.object_model_service.abs_create_object_model_app_service import AbsCreateObjectModelAppService
from domain.service.abs_mvg_service import AbsMvgService
from domain.service.abs_mvs_service import AbsMvsService
from domain.service.abs_mtl_material_service import AbsMtlMaterialService
from domain.service.abs_object_model_service import AbsObjectModelService
from injector import inject
from domain.repository.object_model_repository import AbsObjectModelRepository
import os

class CreateObjectModelAppService(AbsCreateObjectModelAppService):
    @inject
    def __init__(
        self,
        object_model_repository: AbsObjectModelRepository,
        mvg_service: AbsMvgService,
        mvs_service: AbsMvsService,
        mtl_material_service: AbsMtlMaterialService,
        object_model_service: AbsObjectModelService
    ):
        self.__object_model_repository = object_model_repository
        self.__mvg_service = mvg_service
        self.__mvs_service = mvs_service
        self.__mtl_material_service = mtl_material_service
        self.__object_model_service = object_model_service
        
    def handle(self, param: CreateObjectModelParam) -> dict:
        object_model_id = param.getObjectModelId()
        pid = param.getPid()
        dir_name = param.getDirName()
        
        # PIDを登録する
        self.__object_model_repository.UpdatePid(object_model_id, str(pid))
        # MVGの実行
        self.__mvg_service.handle(object_model_id, dir_name)
        # MVSの実行
        self.__mvs_service.handle(object_model_id, dir_name)
        
        # オブジェクトが生成されているかを確認する
        if not os.path.exists(f"/app/storage/{dir_name}/output/reconstruction_sequential/model_data.obj"):
            return {"msg": "error"}
            #file_size = self.__get_model_object_size(dir_name, object_model_id)
            
        # MTLファイルの修正
        mtl_material_file_path = self.__mtl_material_service.getFilepath(dir_name)
        mtl_material = self.__mtl_material_service.load(mtl_material_file_path)
        self.__mtl_material_service.save(mtl_material, mtl_material_file_path)
        
        # ファイルの保存（アップロード）
        local_file_path = f"/app/storage/{dir_name}/output/reconstruction_sequential"
        file_path = f"{dir_name}/obj"
        file_size = self.__object_model_service.store(local_file_path, file_path)
        self.__object_model_service.delete_local_files(f"/app/storage/{dir_name}")
        
        return {"msg": "ok", "file_size": file_size}
    
        