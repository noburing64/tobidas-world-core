class MtlMaterialKa:
    def __init__(self, input: str):
        data = input.split(" ")
        if len(data) != 4:
            raise Exception
        if data[0].lower() != "ka":
            raise Exception
        self.__header = "Ka"
        self.__values = [
            float(data[1]),
            float(data[2]),
            float(data[3])
        ]
        
    def getHeaderValues(self):
        return " ".join([
            self.__header,
            round(self.__values[0], 6),
            round(self.__values[1], 6),
            round(self.__values[2], 6)
        ])