class ObjFileV:
    def __init__(self, input: str):
        data = input.split(" ")
        if len(data) != 4:
            raise Exception
        if data[0] != "v":
            raise Exception
        self.__header = data[0]
        self.__vertex = [float(data[1]), float(data[2]), float(data[3])]
        
    def getValues(self):
        return " ".join(
            self.__header,
            round(self.__vertext[0], 6),
            round(self.__vertext[1], 6),
            round(self.__vertext[2], 6)
        )
        