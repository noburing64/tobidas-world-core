class MtlMaterialMapKd:
    def __init__(self, input: str):
        data = input.split(" ")
        if len(data) != 2:
            raise Exception
        if data[0].lower() != "map_kd":
            raise Exception
        self.__header = "map_Kd"
        self.__value = data[1]
        
    def getHeaderValue(self):
        return f"{self.__header} {self.__value}"
        