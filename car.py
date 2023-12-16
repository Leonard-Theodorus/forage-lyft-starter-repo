from servicable import Servicable

class Car(Servicable):
    def __init__(self, engine, battery, tire):
        self.engine = engine
        self.battery = battery
        self.tire = tire
        
    def needs_service(self) -> bool:
        return self.engine.needsService() or self.battery.needsService() or self.tire.needsService()
