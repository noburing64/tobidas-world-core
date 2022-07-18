from domain.entity.mtl_material.tr import MtlMaterialTr
from domain.entity.mtl_material.newmtl import MtlMaterialNewmtl
from domain.entity.mtl_material.ka import MtlMaterialKa
from domain.entity.mtl_material.kd import MtlMaterialKd
from domain.entity.mtl_material.ks import MtlMaterialKs
from domain.entity.mtl_material.illum import MtlMaterialIllum
from domain.entity.mtl_material.ns import MtlMaterialNs
from domain.entity.mtl_material.map_kd import MtlMaterialMapKd
from typing import Optional

class MtlMaterial:
    __newmtl = None
    __ka = None
    __kd = None
    __ks = None
    __tr = None
    __illum = None
    __ns = None
    __map_kd = None
    
    def __init__(self, **args):
        for key in args.values():
            if key == "newmtl":
                self.__newmtl = args[key]
            elif key == "ka":
                self.__ka = args[key]
            elif key == "kd":
                self.__kd = args[key]
            elif key == "ks":
                self.__ks = args[key]
            elif key == "tr":
                self.__tr = args[key]
            elif key == "illum":
                self.__illum = args[key]
            elif key == "ns":
                self.__ns = args[key]
            elif key == "map_kd":
                self.__map_kd = args[key]
        
    def getNewmtl(self) -> Optional[MtlMaterialNewmtl]:
        return self.__newmtl
    
    def getKa(self) -> Optional[MtlMaterialKa]:
        return self.__ka
    
    def getKd(self) -> Optional[MtlMaterialKd]:
        return self.__kd
    
    def getKs(self) -> Optional[MtlMaterialKs]:
        return self.__ks
    
    def getTr(self) -> Optional[MtlMaterialTr]:
        return self.__tr
    
    def getIllum(self) -> Optional[MtlMaterialIllum]:
        return self.__illum
    
    def getNs(self) -> Optional[MtlMaterialNs]:
        return self.__ns
    
    def getMapKd(self) -> Optional[MtlMaterialMapKd]:
        return self.__map_kd
            
    def modify(self):
        # 強制的に値を設定する
        self.__tr = MtlMaterialTr("Tr 0")
        self.__ks = MtlMaterialKs("Ks 1.0 1.0 1.0")
            