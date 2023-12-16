from car import Car
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.spindlerbattery import SpindlerBattery
from battery.nubbinbattery import NubbinBattery

class CarFactory():
    def create_calliope(current_date, last_service_date, current_milleage, last_service_milleage) -> Car:
        engine = CapuletEngine.__init__(current_milleage, last_service_milleage)
        battery = SpindlerBattery.__init__(current_date, last_service_date)
        car = Car.__init__(engine, battery)
        return car
    
    def create_glissade(current_date, last_service_date, current_milleage, last_service_milleage) -> Car:
        engine = WilloughbyEngine.__init__(current_milleage, last_service_milleage)
        battery = SpindlerBattery.__init__(current_date, last_service_date)
        car = Car.__init__(engine, battery)
        return car
    
    def create_palindrome(current_date, last_service_date, warning_light_on) -> Car:
        engine = SternmanEngine.__init__(warning_light_on)
        battery = SpindlerBattery.__init__(current_date, last_service_date)
        car = Car.__init__(engine, battery)
        return car
    
    def create_rorschach(current_date, last_service_date, current_milleage, last_service_milleage) -> Car:
        engine = WilloughbyEngine.__init__(current_milleage, last_service_milleage)
        battery = NubbinBattery.__init__(current_date, last_service_date)
        car = Car.__init__(engine, battery)
        return car
    
    def create_thovex(current_date, last_service_date, current_milleage, last_service_milleage) -> Car:
        engine = CapuletEngine.__init__(current_milleage, last_service_milleage)
        battery = NubbinBattery.__init__(current_date, last_service_date)
        car = Car.__init__(engine, battery)
        return car