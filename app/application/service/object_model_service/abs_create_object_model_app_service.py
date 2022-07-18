from abc import ABCMeta, abstractmethod
from presentation.request_param.object_model.create_object_model_param import CreateObjectModelParam

class AbsCreateObjectModelAppService(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, param: CreateObjectModelParam):
        pass