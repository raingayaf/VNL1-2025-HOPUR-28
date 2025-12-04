from datetime import date


from models.modelTournaments import Tournament   
from models.modelPerson import Person            

class LogicApi:
    def __init__(self):
        self._tournaments: list[Tournament] = []   

    def create_tournament(self, name: str, start: date, end: date, venue: str, contact: Person) -> Tournament:
        

        tournament = Tournament(
            name = name,
            venue = venue,
            start_date = start,
            end_date = end,
            contact_name = contact.name,
            contact_email = contact.email,
            contact_phone = contact.phone,
            max_servers = contact.max_servers,   
        )

        self._tournaments.append(tournament)
        return tournament




    
        

