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
    
    def __init__(
        self,
        newmtl: Optional[MtlMaterialNewmtl],
        ka: Optional[MtlMaterialKa],
        kd: Optional[MtlMaterialKd],
        ks: Optional[MtlMaterialKs],
        tr: Optional[MtlMaterialTr],
        illum: Optional[MtlMaterialIllum],
        ns: Optional[MtlMaterialNs],
        map_kd: Optional[MtlMaterialMapKd]
    ):
        self.__newmtl = newmtl
        self.__ka = ka
        self.__kd = kd
        self.__ks = ks
        self.__tr = tr
        self.__illum = illum
        self.__ns = ns
        self.__map_kd = map_kd
        
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
            