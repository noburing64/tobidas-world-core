from abc import ABCMeta, abstractmethod

class AbsMvgService(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, object_model_id, dir_name: str):
        pass