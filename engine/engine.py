from abc import ABC, abstractmethod

class Engine(ABC):
    @abstractmethod
    def needService(self) -> bool:
        pass