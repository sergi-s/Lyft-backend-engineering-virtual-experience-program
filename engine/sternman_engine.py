
from engine.engine import Engine


class SternmanEngine(Engine):
    def __init__(self, warning_light_is_on):
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self):
        return self.warning_light_is_on

    def __str__(self):
        return f"""{super().__str__()}, 
        SternmanEngine: 
        warning_light_is_on: {self.warning_light_is_on},"""
