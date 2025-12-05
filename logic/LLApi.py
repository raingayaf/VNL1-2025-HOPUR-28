from datetime import date
from models.modelTeam import Team
from models.modelMatch import Match
from models.modelPlayer import Player
from models.modelTournament import Tournament
from models.modelPerson import Person

class LogicApi:
    """LogicApi lætur Logic layer og UI layer tala saman"""
    def __init__(self):
        self._tournaments: list[Tournament] = []   

    def create_tournament(self, name: str, start: date, end: date, venue: str,
contact: Person, max_servers: int) -> Tournament:

        new_id = len(self._tournaments) + 1 #Ef við viljum fara í B kröfuna(Eyða fyrir skil annars)

        tournament = Tournament(
            tournament_id = new_id,
            name = name,
            venue = venue,
            start_date = start,
            end_date = end,
            contact_name = contact.name,
            contact_email = contact.email,
            contact_phone = contact.phone,
            max_servers = max_servers
        )

        self._tournaments.append(tournament)
        return tournament


    def add_team_to_tournament(self, tournament_id: int, team: Team) -> bool:
        pass

    def create_match(self, team_1: Team, team_2: Team, time: int) -> Match:
        pass

    def register_player(self, player: Player) -> bool:
        pass

    def archive_matches(self, match_id: int, winner: Team):
        pass

    def list_tournaments(self) -> list[Tournament]:
        pass

    def list_matches(self) -> list[Match]:
        pass