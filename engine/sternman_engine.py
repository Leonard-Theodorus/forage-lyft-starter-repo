from engine.engine import Engine


class SternmanEngine(Engine):
    def __init__(self, warning_light_is_on):
        self.warning_light_is_on = warning_light_is_on
    
    def needsService(self) -> bool:
        return True if self.warning_light_is_on else False