
from engine.engine import Engine


class CapuletEngine(Engine):
    def __init__(self, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.number_miles = 30000

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > self.number_miles

    def __str__(self):
        return f"""{super().__str__()}, 
        CapuletEngine: 
        current_mileage: {self.current_mileage},
        last_service_mileage: {self.last_service_mileage}
        number_miles: {self.number_miles}"""
