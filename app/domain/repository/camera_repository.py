from abc import ABCMeta, abstractmethod

class AbsCameraRepository(metaclass=ABCMeta):
    @abstractmethod
    def FindAll(self):
        pass
    
    @abstractmethod
    def FindByModelName(self, maker_name: str, model_name: str):
        pass
    
    @abstractmethod
    def Create(self, maker_name, model_name, focal_length):
        pass