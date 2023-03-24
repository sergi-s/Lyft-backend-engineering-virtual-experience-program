
from ..battery import Battery


class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date
        self.number_of_years = 4

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(
            year=self.last_service_date.year + self.number_of_years)
        return service_threshold_date < self.current_date

    def __str__(self):
        return super().__str__()+f"""NubbinBattery: last service date: {self.last_service_date}, 
        current date: {self.current_date}, 
        number of years each service {self.number_of_years}"""
