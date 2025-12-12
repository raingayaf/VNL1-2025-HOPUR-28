import os
from models.model_match import Match
from models.model_tournament import Tournament
from models.model_team import Team
from models.model_player import Player

from data.matches_data import MatchesData
from data.tournament_data import TournamentData
from data.Team_data import TeamData
from data.Player_data import PlayerData
#from data.schedule_data import ScheduleData


class DataApi:
    """Api for the logic layer to be able to fetch from data layer"""
    def __init__(self, base_path: str = "data/data_base"):
        """Creates a correct file path for the .csv file and makes repo 
    objects for reading and writing into them"""

        #Connects matches repo to csv. file
        matches_path = os.path.join(base_path, "matches.csv")
        self._matches_repo = MatchesData(matches_path)

        #Connects players repo to csv. file
        players_path = os.path.join(base_path, "players.csv")
        self._players_repo = PlayerData(players_path)

        #Connects tournaments repo to csv. file
        tournaments_path = os.path.join(base_path, "tournaments.csv")
        self._tournaments_repo = TournamentData(tournaments_path)
        #Connects teams repo to csv. file
        teams_path = os.path.join(base_path, "teams.csv")
        self._teams_repo = TeamData(teams_path)

        #self._data = ScheduleData()

    #All of these below have functions called write_all(), read_all() that should be used by the repos.
    def read_all_matches(self) -> list[Match]:
        """Reads matches.csv and returns a list of objects"""
        return self._matches_repo.read_all()

    def save_all_matches(self, matches: list[Match]) -> None:
        """Writes match objects in matches.csv file"""
        self._matches_repo.write_all(matches)

    def read_all_players(self) -> list[Player]:
        """Reads players.csv and returns a list of objects"""
        return self._players_repo.read_all()

    def save_all_players(self, players: list[Player]) -> None:
        """Writes player objects into players.csv file"""
        self._players_repo.write_all(players)

    def read_all_teams(self) -> list[Team]:
        """Reads teams.csv and returns a list of objects"""
        return self._teams_repo.read_all()

    def save_all_teams(self, teams: list[Team]) -> None:
        """Writes team objects into teams.csv file"""
        self._teams_repo.write_all(teams)

    def read_all_tournaments(self) -> list[Tournament]:
        """Reads tournaments.csv and returns a list of objects"""
        return self._tournaments_repo.read_all()

    def save_all_tournaments(self, tournaments: list[Tournament]) -> None:
        """Writes tournament objects into tournaments.csv file"""
        self._tournaments_repo.write_all(tournaments)