class MtlMaterialIllum:
    def __init__(self, input: str):
        data = input.split(" ")
        if len(data) != 2:
            raise Exception
        if data[0].lower() != "illum":
            raise Exception
        self.__header = "illum"
        value = int(data[1])
        if value not in [0, 1, 2]:
            raise Exception
        self.__value = value
        
    def getHeaderValue(self):
        return f"{self.__header} {self.__value}"