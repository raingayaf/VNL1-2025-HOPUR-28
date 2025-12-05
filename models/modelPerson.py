from datetime import date


class Person:
    def __init__(self, name: str, date_of_birth: date, phone: str, email: str):
        self.name = name
        self.date_of_birth = date_of_birth
        self.email = email
        self.phone = phone
