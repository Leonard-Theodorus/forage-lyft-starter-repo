from engine.engine import Engine


class CapuletEngine(Engine):
    def __init__(self,current_mileage, last_service_mileage):
        self.current_milleage = current_mileage
        self.last_service_milleage = last_service_mileage

    def needsService(self) -> bool:
        return self.current_milleage - self.last_service_milleage > 30000


