from application.service.camera_service.abs_create_camera_app_service import AbsCreateCameraAppService
from domain.repository.camera_repository import AbsCameraRepository
from domain.entity.camera_database import CameraDatabase
from injector import inject

class CreateCameraAppService(AbsCreateCameraAppService):
    @inject
    def __init__(self, camera_repository: AbsCameraRepository):
        self.__camera_repository = camera_repository
        
    def handle(self, maker_name: str, model_name: str, focal_length: float):
        camera = self.__camera_repository.FindByModelName(maker_name, model_name)
        # 存在を確認する
        if "message" in camera:
            # DB登録
            self.__camera_repository.Create(maker_name, model_name, focal_length)
            # ローカル保存
            camera_database = CameraDatabase()
            camera_database.load()
            camera_database.add(maker_name, model_name, focal_length)
            
        
            
            