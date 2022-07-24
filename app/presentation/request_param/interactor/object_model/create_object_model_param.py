class CreateObjectModelParam:
    def __init__(self, hash: str, images: list):
        if len(hash) != 64:
            raise Exception
        self.__hash = hash
        self.__images = images
        
    def get_hash(self) -> str:
        return self.__hash
    
    def get_images(self) -> list:
        return self.__images