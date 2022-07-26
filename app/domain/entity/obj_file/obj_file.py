import numpy as np
import quaternion

from domain.entity.obj_file.vertex import ObjFileVertex

class ObjFile:
    def __init__(self, f: list, v: list, vt: list, mtllib, usemtl):
        self.__f = f
        self.__v = v
        self.__vt = vt
        self.__mtllib = mtllib
        self.__usemtl = usemtl
            
    def getFaces(self) -> list:
        return self.__f
    
    def getVertexes(self) -> list:
        return self.__v
    
    def getVertexTextures(self) -> list:
        return self.__vt
    
    def getMtllib(self):
        return self.__mtllib
    
    def getUsemtl(self):
        return self.__usemtl
    
    def modify(self):
        # X,Y,Z座標の最小値・最大値を取得する
        x_list = list(map(lambda x: x.get_values()[0], self.__v))
        y_list = list(map(lambda x: x.get_values()[1], self.__v))
        z_list = list(map(lambda x: x.get_values()[2], self.__v))
        
        x_min, x_max = min(x_list), max(x_list)
        y_min, y_max = min(y_list), max(y_list)
        z_min, z_max = min(z_list), max(z_list)
        
        x_center = (x_min + x_max) / 2
        y_center = (y_min + y_max) / 2
        z_center = (z_min + z_max) / 2
        
        self.__v = list(map(
            lambda x: self.__rotate(
                np.array([1.0, 0.0, 0.0]),
                [
                    x.get_values()[0] - x_center,
                    x.get_values()[1] - y_center,
                    x.get_values()[2] - z_center
                ],
                90.0 * np.pi / 2.0
            ),
            self.__v
        ))
        
    def __rotate(self, base_vector: np.ndarray, a: np.ndarray, angle: float) -> ObjFileVertex:
        cos = np.cos(angle/2)
        sin = np.sin(angle/2)
        
        d = np.linalg.norm(base_vector)
        if d == 0:
            return a
        
        qx, qy, qz = base_vector * sin / d
        qw = cos
        
        q = np.quaternion(qw, qx, qy, qz)
        qa = np.quaternion(0, a[0], a[1], a[2])
        
        qt = q * qa * np.conj(q)
        ary = quaternion.as_float_array(qt)
        
        #return [ary[1], ary[2], ary[3]]
        return ObjFileVertex(f"v {ary[1]} {ary[2]} {ary[3]}")
        
            