from abc import ABCMeta, abstractmethod

class AbsCreateObjectModelInteractor(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, input):
        pass