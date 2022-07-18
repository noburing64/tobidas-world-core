class MtlMaterialTr:
    def __init__(self, input: str):
        data = input.split(" ")
        if len(data) != 2:
            raise Exception
        if data[0].lower() != "tr":
            raise Exception
        self.__header = "Tr"
        self.__value  = float(data[1])
        
    def getHeaderValue(self):
        return f"{self.__header} {round(self.__value, 6)}"
        