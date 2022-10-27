from abc import *

class AbstractGenererMot(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def generer(self):
        pass