from abc import ABCMeta, abstractmethod

class AbsObjectModelRepository(metaclass=ABCMeta):
    @abstractmethod
    def FindByHash(self, hash: str):
        pass
    @abstractmethod
    def UpdatePid(self, object_model_id, pid):
        pass
    
    @abstractmethod
    def CreateProcessHistory(self, object_model_id, process_type_id):
        pass
    
    @abstractmethod
    def CreateModelObjectFile(self, object_model_id, file_path, file_name, file_size):
        pass