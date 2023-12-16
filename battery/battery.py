from abc import ABC

class Battery(ABC):

    def needsService(self) -> bool:
        pass