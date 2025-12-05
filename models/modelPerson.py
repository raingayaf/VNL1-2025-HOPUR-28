from datetime import date


class Person:
    def __init__(self, name: str, date_of_birth: date):
        self.name = name
        self.date_of_birth = date_of_birth