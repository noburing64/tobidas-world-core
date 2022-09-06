from domain.entity.obj_file.face import ObjFileFace
from domain.entity.obj_file.mtllib import ObjFileMtllib
from domain.entity.obj_file.usemtl import ObjFileUsemtl
from domain.entity.obj_file.vertex import ObjFileVertex
from domain.entity.obj_file.vertex_texture import ObjFileVertexTexture
from domain.entity.obj_file.obj_file import ObjFile
from domain.service.abs_obj_file_service import AbsObjFileService

class ObjFileService(AbsObjFileService):
    def getFilepath(self, dir_name: str) -> str:
        return f"./storage/{dir_name}/output/reconstruction_sequential/model_data.obj"
    
    def load(self, file_path: str) -> ObjFile:
        with open(file_path) as fp:
            data = fp.read()
            lines = data.split("\n")
            lines = list(filter(lambda x: x.strip() != "", lines))
            faces = []
            mtllib: ObjFileMtllib
            usemtl: ObjFileUsemtl
            vertexes = []
            vertex_textures = []
            
            
            for line in lines:
                kv = line.split(" ")
                if kv[0].lower() == "f":
                    faces.append(ObjFileFace(line))
                elif kv[0].lower() == "v":
                    vertexes.append(ObjFileVertex(line))
                elif kv[0].lower() == "vt":
                    vertex_textures.append(ObjFileVertexTexture(line))
                elif kv[0].lower() == "mtllib":
                    mtllib = ObjFileMtllib(line)
                elif kv[0].lower() == "usemtl":
                    usemtl = ObjFileUsemtl(line)
                    
            obj_file = ObjFile(faces, vertexes, vertex_textures, mtllib, usemtl)
            obj_file.modify()
            return obj_file
    
    def save(self, obj_file: ObjFile, file_path: str):
        # ファイル保存
        with open(file_path, "w") as fp:
            fp.write(obj_file.getMtllib().getHeaderValue() + "\n")
            for v in obj_file.getVertexes():
                fp.write(v.getHeaderValues() + "\n")
            for vt in obj_file.getVertexTextures():
                fp.write(vt.getHeaderValues() + "\n")
            fp.write(obj_file.getUsemtl().getHeaderValue() + "\n")
            for face in obj_file.getFaces():
                fp.write(face.getHeaderValues() + "\n")
            fp.write("\n")
            
            