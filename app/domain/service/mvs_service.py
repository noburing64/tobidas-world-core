from domain.entity.mvs import Mvs
from domain.repository.object_model_repository import AbsObjectModelRepository
from domain.service.abs_mvs_service import AbsMvsService
from injector import inject

class MvsService(AbsMvsService):
    @inject
    def __init__(self, object_model_repository: AbsObjectModelRepository):
        self.__object_model_repository = object_model_repository
        
    def handle(self, object_model_id, dir_name: str):
        mvs = Mvs(
            "/opt/openMVG_Build/Linux-x86_64-RELEASE",
            "/openMVS_build/bin",
            f"/app/storage/{dir_name}/output/reconstruction_sequential",
            f"/app/storage/{dir_name}"
        )
        self.__exec_mvg(mvs, object_model_id)
        
    def __exec_mvg(self, mvs: Mvs, object_model_id):
        process_list = [
            [mvs.OpenMVG2OpenMVS, [], 12],
            [mvs.DensifyPointCloud, [], 13],
            [mvs.ReconstructMesh, [], 14],
            [mvs.RefineMesh, [], 15],
            [mvs.TextureMesh, [], 16]
        ]
        
        self.__exec_process_list(process_list, object_model_id)
        
    def __exec_process_list(self, process_list:list, object_model_id):
        for process in process_list:
            func, args, process_type_id = process
            func(*args)
            self.__object_model_repository.CreateProcessHistory(object_model_id, process_type_id)