from abc import ABCMeta, abstractmethod

class AbsObjectModelService(metaclass=ABCMeta):
    @abstractmethod
    def store(self, local_file_path: str, file_path: str) -> int:
        pass
    
    @abstractmethod
    def delete_local_files(self, local_file_path: str):
        pass