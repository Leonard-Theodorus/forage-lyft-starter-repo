from car import Car
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.spindlerbattery import SpindlerBattery
from battery.nubbinbattery import NubbinBattery

class CarFactory():
    def create_calliope(current_date, last_service_date, current_milleage, last_service_milleage) -> Car:
        engine = CapuletEngine(current_milleage, last_service_milleage)
        battery = SpindlerBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car
    
    def create_glissade(current_date, last_service_date, current_milleage, last_service_milleage) -> Car:
        engine = WilloughbyEngine(current_milleage, last_service_milleage)
        battery = SpindlerBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car
    
    def create_palindrome(current_date, last_service_date, warning_light_on) -> Car:
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car
    
    def create_rorschach(current_date, last_service_date, current_milleage, last_service_milleage) -> Car:
        engine = WilloughbyEngine(current_milleage, last_service_milleage)
        battery = NubbinBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car
    
    def create_thovex(current_date, last_service_date, current_milleage, last_service_milleage) -> Car:
        engine = CapuletEngine(current_milleage, last_service_milleage)
        battery = NubbinBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car