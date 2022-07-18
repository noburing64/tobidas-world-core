class CreateObjectModelParam:
    def __init__(self, object_model_id, pid, dir_name):
        self.__object_model_id = object_model_id
        self.__pid = pid
        self.__dir_name = dir_name
        
    def getObjectModelId(self):
        return self.__object_model_id
    
    def getPid(self):
        return self.__pid
    
    def getDirName(self):
        return self.__dir_name