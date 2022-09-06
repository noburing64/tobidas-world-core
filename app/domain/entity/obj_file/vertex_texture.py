class ObjFileVertexTexture:
    def __init__(self, input: str):
        data = input.split(" ")
        if len(data) != 3:
            raise Exception
        if data[0].lower() != "vt":
            raise Exception
        self.__header = "vt"
        self.__values = [
            float(data[1]),
            float(data[2])
        ]
        
    def getHeaderValues(self):
        return " ".join([
            self.__header,
            str(round(self.__values[0], 6)),
            str(round(self.__values[1], 6))
        ])