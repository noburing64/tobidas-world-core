class ObjFileUsemtl:
    def __init__(self, input: str):
        data = input.split(" ")
        if len(data) != 2:
            raise Exception
        if data[0].lower() != "usemtl":
            raise Exception(data[0] + " is not usemtl")
        self.__header = "usemtl"
        self.__value = data[1]
        
    def getHeaderValue(self):
        return f"{self.__header} {self.__value}"