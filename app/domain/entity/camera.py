
class Camera():
    def __init__(self, model_name: str, focal_length: float):
        self.__model_name = model_name
        self.__focal_length = focal_length
        
    def getModelName(self) -> str:
        return self.__model_name
    
    def getFocalLength(self) -> float:
        return self.__focal_length