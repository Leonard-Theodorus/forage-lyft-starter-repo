from battery.battery import Battery
from util import add_years_to_date

class NubbinBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date
        #PerYear = 4
    def needsService(self) -> bool:
        needs_to_be_serviced_by = add_years_to_date(self.last_service_date, 4)
        return needs_to_be_serviced_by < self.current_date