from abc import ABCMeta, abstractmethod

from domain.entity.mtl_material.mtl_material import MtlMaterial

class AbsMtlMaterialService(metaclass=ABCMeta):
    @abstractmethod
    def getFilepath(self, dir_name: str) -> str:
        pass
    
    @abstractmethod
    def load(self, file_path: str) -> MtlMaterial:
        pass
    
    @abstractmethod
    def save(self, mtl_material: MtlMaterial, file_path: str):
        pass