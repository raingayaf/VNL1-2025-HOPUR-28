from datetime import date

class Player: 

    def __init__(self, player_id: int, name: str, date_of_birth: date,
address: str, phone: str, email:str, link: str, handle: str, team_name: str):
        self.player_id = player_id
        self.name = name
        self.date_of_birth = date_of_birth
        self.address = address
        self.phone = phone
        self.email = email
        self.link = link
        self.handle = handle
        self.team_name = team_name


