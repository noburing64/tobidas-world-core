class ObjFile:
    def __init__(self, file_path):
        self.__file_path = file_path
        with open(file_path) as fp:
            data = fp.read()
            lines = data.split("\n")
            
    def __load(self, lines: list[str]) -> None:
        for line in lines:
            data = line.split(" ")
            