from domain.entity.mvg import Mvg
from domain.repository.object_model_repository import AbsObjectModelRepository
from domain.service.abs_mvg_service import AbsMvgService
from injector import inject

class MvgService(AbsMvgService):
    @inject
    def __init__(self, object_model_repository: AbsObjectModelRepository):
        self.__object_model_repository = object_model_repository
        
    def handle(self, object_model_id, dir_name: str):
        mvg = Mvg(
            f"/app/storage/{dir_name}/input",
            "/opt/openMVG_Build/Linux-x86_64-RELEASE",
            f"/app/storage/{dir_name}/output/matches",
            f"/app/storage/{dir_name}/output/reconstruction_sequential",
            f"/app/storage/{dir_name}/output/reconstruction_global",
            "/opt/openMVG/src/openMVG/exif/sensor_width_database/sensor_width_camera_database.txt"
        )
        self.__exec_mvg(mvg, object_model_id)
        
    def __exec_mvg(self, mvg: Mvg, object_model_id):
        process_list = [
            [mvg.SfmInitImageListing, [], 1],
            [mvg.ComputeFeatures, [], 2],
            [mvg.ComputeMatches, [], 3],
            [mvg.GeometricFilter, ["f"], 4],
            [mvg.StartSfm, [""], 5],
            [mvg.ComputeSfmDataColor, [""], 6],
            [mvg.ComputeStructureFromKnownPoses, [], 7],
            [mvg.GeometricFilter, ["e"], 8],
            [mvg.StartSfm, ["global"], 9],
            [mvg.ComputeSfmDataColor, ["global"], 10],
            [mvg.ComputeStructureFromKnownPoses, ["global"], 11]
        ]
        
        self.__exec_process_list(process_list, object_model_id)
        
    def __exec_process_list(self, process_list:list, object_model_id):
        for process in process_list:
            func, args, process_type_id = process
            ret = func(*args)
            if ret.returncode == 0:
                # 正常終了
                self.__object_model_repository.CreateProcessHistory(object_model_id, process_type_id)
            else:
                # エラーが発生
                raise Exception