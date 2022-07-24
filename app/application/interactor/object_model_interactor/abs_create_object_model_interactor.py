from abc import ABCMeta, abstractmethod
from presentation.request_param.interactor.object_model.create_object_model_param import CreateObjectModelParam

class AbsCreateObjectModelInteractor(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, input: CreateObjectModelParam):
        pass