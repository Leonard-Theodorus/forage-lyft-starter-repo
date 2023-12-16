from tires.tire import Tire

class CarriganTire(Tire):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def needsService(self) -> bool:
        for wear in self.tire_wear:
            if wear >= 0.9:
                return True
        return False