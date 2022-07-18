class MtlMaterialNs:
    def __init__(self, input: str):
        data = input.split(" ")
        if len(data) != 2:
            raise Exception
        if data[0].lower() != "ns":
            raise Exception
        
        self.__header = "Ns"
        self.__value = float(data[1])
        
    def getHeaderValue(self):
        return f"{self.__header} {round(self.__value, 6)}"
        