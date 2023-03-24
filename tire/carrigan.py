
from tire.tire import Tire

class CarriganTire(Tire):
    def __init__(self, tire_wear_4_wheels):
        self.tire_wear_4_wheels = tire_wear_4_wheels
        self.tire_wear_limit = 0.9

    def needs_service(self):
        for tire in self.tire_wear_4_wheels:
            if tire >= self.tire_wear_limit:
                return True
        return False

    def __str__(self):
        return super().__str__()+f"""CarriganTire: tire_wear_4_wheels: {self.tire_wear_4_wheels}, 
        tire_wear_limit: {self.tire_wear_limit}"""
