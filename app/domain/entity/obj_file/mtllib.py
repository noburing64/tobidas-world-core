class ObjFileMtllib:
    def __init__(self, input: str):
        data = input.split(" ")
        if len(data) != 2:
            raise Exception
        if data[0].lower() != "mtllib":
            raise Exception(data[0] + " is not mtllib")
        self.__header = "mtllib"
        if data[1] != "model_data.mtl":
            raise Exception(data[1] + " is not model_data.mtl")
        self.__value = data[1]
        
    def getHeaderValue(self):
        return f"{self.__header} {self.__value}"