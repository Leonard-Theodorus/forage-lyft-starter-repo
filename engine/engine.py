from abc import ABC, abstractmethod

class Engine(ABC):
    @abstractmethod
    def needsService(self) -> bool:
        pass