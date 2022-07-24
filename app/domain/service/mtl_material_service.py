from domain.entity.mtl_material.illum import MtlMaterialIllum
from domain.entity.mtl_material.kd import MtlMaterialKd
from domain.entity.mtl_material.ks import MtlMaterialKs
from domain.entity.mtl_material.ns import MtlMaterialNs
from domain.entity.mtl_material.tr import MtlMaterialTr
from domain.entity.mtl_material.ka import MtlMaterialKa
from domain.entity.mtl_material.newmtl import MtlMaterialNewmtl
from domain.entity.mtl_material.map_kd import MtlMaterialMapKd
from domain.service.abs_mtl_material_service import AbsMtlMaterialService
from domain.entity.mtl_material.mtl_material import MtlMaterial
class MtlMaterialService(AbsMtlMaterialService):
    def getFilepath(self, dir_name: str) -> str:
        return f"./storage/{dir_name}/output/reconstruction_sequential/model_data.mtl"
    
    def load(self, file_path: str) -> MtlMaterial:
        with open(file_path) as fp:
            data = fp.read()
            lines = data.split("\n")
            lines = list(filter(lambda x: x.strip() != "", lines))
            newmtl: MtlMaterialNewmtl
            ka: MtlMaterialKa
            kd: MtlMaterialKd
            ks: MtlMaterialKs
            tr: MtlMaterialTr
            illum: MtlMaterialIllum
            ns: MtlMaterialNs
            map_kd: MtlMaterialMapKd
            
            
            
            for line in lines:
                kv = line.split(" ")
                if kv[0].lower() == "newmtl":
                    newmtl = MtlMaterialNewmtl(line)
                elif kv[0].lower() == "ka":
                    ka = MtlMaterialKa(line)
                elif kv[0].lower() == "kd":
                    kd = MtlMaterialKd(line)
                elif kv[0].lower() == "ks":
                    ks = MtlMaterialKs(line)
                elif kv[0].lower() == "tr":
                    tr = MtlMaterialTr(line)
                elif kv[0].lower() == "illum":
                    illum = MtlMaterialIllum(line)
                elif kv[0].lower() == "ns":
                    ns = MtlMaterialNs(line)
                elif kv[0].lower() == "map_kd":
                    map_kd = MtlMaterialMapKd(line)
                    
            mtl_material = MtlMaterial(newmtl, ka, kd, ks, tr, illum, ns, map_kd)
            mtl_material.modify()
            return mtl_material
    
    def save(self, mtl_material: MtlMaterial, file_path: str):
        # ファイル保存
        with open(file_path, "w") as fp:
            fp.write(mtl_material.getNewmtl().getHeaderValue() + "\n")
            fp.write(mtl_material.getKa().getHeaderValues() + "\n")
            fp.write(mtl_material.getKd().getHeaderValues() + "\n")
            fp.write(mtl_material.getKs().getHeaderValues() + "\n")
            fp.write(mtl_material.getTr().getHeaderValue() + "\n")
            fp.write(mtl_material.getIllum().getHeaderValue() + "\n")
            fp.write(mtl_material.getNs().getHeaderValue() + "\n")
            fp.write(mtl_material.getMapKd().getHeaderValue() + "\n")
            