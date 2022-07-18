from domain.repository.object_model_repository import AbsObjectModelRepository
from domain.service.abs_object_model_service import AbsObjectModelService
from injector import inject
import domain.helper.storage_helper as storage_helper
import os
import shutil

class ObjectModelService(AbsObjectModelService):
    @inject
    def __init__(self, object_model_repository: AbsObjectModelRepository):
        self.__object_model_repository = object_model_repository
        
    def store(self, local_file_path: str, file_path: str) -> int:
        storage_helper.store(local_file_path + "/model_data.mtl", file_path + "/model_data.mtl")
        storage_helper.store(local_file_path + "/model_data.obj", file_path + "/model_data.obj")
        storage_helper.store(
            local_file_path + "/model_data_material_0_map_Kd.jpg",
            file_path + "/model_data_material_0_map_Kd.jpg"
        )
        # ファイルサイズを取得する
        mtl_file_size = os.path.getsize(local_file_path + "/model_data.mtl")
        obj_file_size = os.path.getsize(local_file_path + "/model_data.obj")
        img_file_size = os.path.getsize(local_file_path + "/model_data_material_0_map_Kd.jpg")
        
        return mtl_file_size + obj_file_size + img_file_size
    
    def delete_local_files(self, local_file_path: str):
        shutil.rmtree(local_file_path)