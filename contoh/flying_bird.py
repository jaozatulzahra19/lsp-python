from abc import ABC, abstractmethod   

class FlyingBird(ABC):
    
    @abstractmethod
    def fly():
        pass