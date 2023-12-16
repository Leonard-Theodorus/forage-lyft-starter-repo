from battery import Battery

class SpindlerBattery(Battery):
    def __init__(self, currentYear, lastServiceYear):
        self.currentYear = currentYear
        self.lastServiceYear = lastServiceYear
        #PerYear = 2
    def needsService(self) -> bool:
        return (self.currentYear - self.lastServiceYear) % 2 == 0