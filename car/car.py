

# from ..serviceable import Serviceable
from serviceable import *


class Car(Serviceable):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()

    def __str__(self):
        return f"""{super().__str__()}, 
        engine: {self.engine.__str__()},
        battery: {self.battery.__str__()}"""
