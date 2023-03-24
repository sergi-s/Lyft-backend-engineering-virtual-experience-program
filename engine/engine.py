from abc import ABC


class Engine(ABC):
    def needs_service(self):
        pass

    def __str__(self):
        return super().__str__()
