from application.service.object_model_service.abs_create_object_model_app_service import AbsCreateObjectModelAppService
from application.service.object_model_service.create_object_model_app_service import CreateObjectModelAppService
from application.service.camera_service.abs_create_camera_app_service import AbsCreateCameraAppService
from application.service.camera_service.create_camera_app_service import CreateCameraAppService
from application.interactor.object_model_interactor.abs_create_object_model_interactor import AbsCreateObjectModelInteractor
from application.interactor.object_model_interactor.create_object_model_interactor import CreateObjectModelInteractor
from domain.repository.camera_repository import AbsCameraRepository
from domain.repository.object_model_repository import AbsObjectModelRepository
from domain.service.abs_mtl_material_service import AbsMtlMaterialService
from domain.service.mtl_material_service import MtlMaterialService
from domain.service.abs_obj_file_service import AbsObjFileService
from domain.service.obj_file_service import ObjFileService
from domain.service.abs_mvg_service import AbsMvgService
from domain.service.mvg_service import MvgService
from domain.service.abs_mvs_service import AbsMvsService
from domain.service.mvs_service import MvsService
from domain.service.abs_object_model_service import AbsObjectModelService
from domain.service.object_model_service import ObjectModelService
from infrastructure.repository.camera_repository import CameraRepository
from infrastructure.repository.object_model_repository import ObjectModelRepository
from injector import Module, singleton

class AppDIModule(Module):
    def configure(self, binder):
        binder.bind(AbsCameraRepository, to=CameraRepository, scope=singleton)
        binder.bind(AbsObjectModelRepository, to=ObjectModelRepository, scope=singleton)
        binder.bind(AbsCreateObjectModelAppService, to=CreateObjectModelAppService, scope=singleton)
        binder.bind(AbsCreateCameraAppService, to=CreateCameraAppService, scope=singleton)
        binder.bind(AbsCreateObjectModelInteractor, to=CreateObjectModelInteractor, scope=singleton)
        binder.bind(AbsMtlMaterialService, to=MtlMaterialService, scope=singleton)
        binder.bind(AbsObjFileService, to=ObjFileService, scope=singleton)
        binder.bind(AbsMvgService, to=MvgService, scope=singleton)
        binder.bind(AbsMvsService, to=MvsService, scope=singleton)
        binder.bind(AbsObjectModelService, to=ObjectModelService, scope=singleton)