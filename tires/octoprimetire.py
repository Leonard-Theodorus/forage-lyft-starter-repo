from tires.tire import Tire

class OctoprimeTire(Tire):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def needsService(self) -> bool:
        return True if sum(self.tire_wear) >= 3 else False