class ObjFileFace:
    def __init__(self, input: str):
        data = input.split(" ")
        if len(data) != 4:
            raise Exception
        if data[0].lower() != "f":
            raise Exception
        self.__header = "f"
        self.__values = [
            data[1],
            data[2],
            data[3]
        ]
        
    def getHeaderValues(self):
        return " ".join([
            self.__header,
            self.__values[0],
            self.__values[1],
            self.__values[2]
        ])