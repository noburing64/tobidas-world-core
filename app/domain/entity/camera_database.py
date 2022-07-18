class CameraDatabase():
    __database_path = "/opt/openMVG/src/openMVG/exif/sensor_width_database/sensor_width_camera_database.txt"
    __data = []
    
    def load(self):
        with open(self.__database_path) as f:
            lines = f.read().split("\n")
            lines = list(filter(lambda x: x != "", lines))
            self.__data = list(map(lambda x: self.__parse(x), lines))
        
    def exists(self, model):
        return True if next(filter(lambda x: x["model"] == model, self.__database_path)) else False
        
    def getDataBase(self):
        return self.__data
    
    def add(self, model_name: str, focal_length: float):
        with open(self.__database_path, "a") as fp:
            fp.write(f'{model_name};{round(focal_length, 2)}\n')
            self.__data.append({"model": model_name, "focal_length": round(focal_length, 2)})
            
    def __parse(self, line):
        parsed_line = line.split(";")
        if len(parsed_line) == 2:
            return {"model":parsed_line[0], "focal_length": float(parsed_line[1].strip())}
        else:
            # 最後の値を焦点距離として取得
            focal_length = parsed_line[len(parsed_line) - 1]
            focal_length = float(focal_length.strip())
            model = ";".join([parsed_line[l] for l in range(len(parsed_line) - 1)])
            return {"model": model, "focal_length": focal_length}