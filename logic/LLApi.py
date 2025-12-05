from datetime import date
from models.modelTeam import Team
from models.modelMatch import Match
from models.modelPlayer import Player
from models.modelTournament import Tournament
from models.modelPerson import Person

class LogicApi:
    """LogicApi lætur Logic layer og UI layer tala saman"""
    def __init__(self):
        #Listi yfir þær keppnir sem eru í gangi
        self._tournaments: list[Tournament] = []
        #Tekur tournament_id og býr til lista af Team objects
        self._tournament_teams: dict[int, list[Team]] = {}


