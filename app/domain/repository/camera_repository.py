from abc import ABCMeta, abstractmethod

class AbsCameraRepository(metaclass=ABCMeta):
    @abstractmethod
    def FindAll(self):
        pass
    
    @abstractmethod
    def FindByModelName(self, model_name):
        pass
    
    @abstractmethod
    def Create(self, model_name, focal_length):
        pass