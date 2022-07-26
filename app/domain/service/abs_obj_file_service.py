from abc import ABCMeta, abstractmethod

from domain.entity.obj_file.obj_file import ObjFile

class AbsObjFileService(metaclass=ABCMeta):
    @abstractmethod
    def getFilepath(self, dir_name: str) -> str:
        pass
    
    @abstractmethod
    def load(self, file_path: str) -> ObjFile:
        pass
    
    @abstractmethod
    def save(self, obj_file: ObjFile, file_path: str):
        pass