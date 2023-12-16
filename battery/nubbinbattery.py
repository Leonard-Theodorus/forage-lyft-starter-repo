from battery import Battery

class NubbinBattery(Battery):
    def __init__(self, currentYear, lastServiceYear):
        self.currentYear = currentYear
        self.lastServiceYear = lastServiceYear
        #PerYear = 4
    def needsService(self) -> bool:
        return (self.currentYear - self.lastServiceYear) % 4 == 0