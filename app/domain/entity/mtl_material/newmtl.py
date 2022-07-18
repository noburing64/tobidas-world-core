class MtlMaterialNewmtl:
    def __init__(self, input: str):
        data = input.split(" ")
        if len(data) != 2:
            raise Exception
        if data[0].lower() != "newmtl":
            raise Exception
        self.__header = "newmtl"
        self.__value = data[1]
        
    def getHeaderValue(self):
        return f"{self.__header} {self.__value}"
        