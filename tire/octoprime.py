
from tire.tire import Tire

class OctoprimeTire(Tire):
    def __init__(self, tire_wear_4_wheels):
        self.tire_wear_4_wheels = tire_wear_4_wheels
        self.tire_wear_limit = 3

    def needs_service(self):
        return sum(self.tire_wear_4_wheels)>=self.tire_wear_limit

    def __str__(self):
        return super().__str__()+f"""OctoprimeTire: tire_wear_4_wheels: {self.tire_wear_4_wheels}, 
        tire_wear_limit: {self.tire_wear_limit}"""