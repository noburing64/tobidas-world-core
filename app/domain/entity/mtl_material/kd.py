class MtlMaterialKd:
    def __init__(self, input: str):
        data = input.split(" ")
        if len(data) != 4:
            raise Exception
        if data[0].lower() != "kd":
            raise Exception
        self.__header = "Kd"
        self.__values = [
            int(data[1]),
            int(data[2]),
            int(data[3])
        ]
        
    def getHeaderValues(self):
        return " ".join([
            self.__header
        ].extend(self.__values))