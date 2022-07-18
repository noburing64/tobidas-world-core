class ObjFileHeader:
    def __init__(self, input: str):
        values = input.split(" ")
        if len(values) != 2:
            raise Exception
        if values[0] != "mtllib":
            raise Exception
        self.__header = values[0]
        self.__file_name = values[1]
        
    def getFileName(self):
        return self.__file_name
    
    def getValues(self):
        return f"{self.__header} {self.__file_name}"