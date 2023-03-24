
from battery.battery import Battery


class SpindlerBattery(Battery):
    def __init__(self, current_date,last_service_date):
        self.last_service_date = last_service_date
        self.current_date = current_date
        self.number_of_years = 3

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(
            year=self.last_service_date.year + self.number_of_years)
        return service_threshold_date < self.current_date

    def __str__(self):
        return super().__str__()+f"""SpindlerBattery: last service date: {self.last_service_date}, 
        current date: {self.current_date}, 
        number of years each service {self.number_of_years}"""
