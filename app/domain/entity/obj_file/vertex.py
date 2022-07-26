class ObjFileVertex:
    def __init__(self, input: str):
        data = input.split(" ")
        if len(data) != 4:
            raise Exception
        if data[0].lower() != "v":
            raise Exception
        self.__header = "v"
        self.__values = [
            float(data[1]),
            float(data[2]),
            float(data[3])
        ]
        
    def getHeaderValues(self):
        return " ".join([
            self.__header,
            str(round(self.__values[0], 6)),
            str(round(self.__values[1], 6)),
            str(round(self.__values[2], 6))
        ])
        
    def get_values(self) -> list:
        return self.__values