from abc import ABCMeta, abstractmethod

class AbsCreateCameraAppService(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, model_name: str, focal_length: float):
        pass