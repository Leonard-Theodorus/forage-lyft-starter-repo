from abc import ABC, abstractmethod

class Tire(ABC):
    @abstractmethod
    def needsService(self) -> bool:
        pass