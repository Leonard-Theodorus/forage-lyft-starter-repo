from car import Car
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.spindlerbattery import SpindlerBattery
from battery.nubbinbattery import NubbinBattery
from tires.carrigantire import CarriganTire
from tires.octoprimetire import OctoprimeTire

class CarFactory():
    def create_calliope(current_date, last_service_date, current_milleage, last_service_milleage, tire_wear) -> Car:
        engine = CapuletEngine(current_milleage, last_service_milleage)
        battery = SpindlerBattery(current_date, last_service_date)
        tire = CarriganTire(tire_wear)
        car = Car(engine, battery, tire)
        return car
    
    def create_glissade(current_date, last_service_date, current_milleage, last_service_milleage, tire_wear) -> Car:
        engine = WilloughbyEngine(current_milleage, last_service_milleage)
        battery = SpindlerBattery(current_date, last_service_date)
        tire = OctoprimeTire(tire_wear)
        car = Car(engine, battery, tire)
        return car
    
    def create_palindrome(current_date, last_service_date, warning_light_on, tire_wear) -> Car:
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(current_date, last_service_date)
        tire = CarriganTire(tire_wear)
        car = Car(engine, battery, tire)
        return car
    
    def create_rorschach(current_date, last_service_date, current_milleage, last_service_milleage, tire_wear) -> Car:
        engine = WilloughbyEngine(current_milleage, last_service_milleage)
        battery = NubbinBattery(current_date, last_service_date)
        tire = OctoprimeTire(tire_wear)
        car = Car(engine, battery, tire)
        return car
    
    def create_thovex(current_date, last_service_date, current_milleage, last_service_milleage, tire_wear) -> Car:
        engine = CapuletEngine(current_milleage, last_service_milleage)
        battery = NubbinBattery(current_date, last_service_date)
        tire = CarriganTire(tire_wear)
        car = Car(engine, battery,tire)
        return car