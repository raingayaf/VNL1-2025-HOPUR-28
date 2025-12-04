import os
from models.modelMatch import Match
from models.modelTournament import Tournament
from models.modelTeam import Team
from models.modelPlayer import Player

from data.matches_data import MatchesData
from data.TournamentData import TournamentData
from data.Team_data import TeamData
from data.Player_data import PlayersData


class DataApi:
    """API notaður til að logic layer geti sótt í data layer"""
    def __init__(self, base_path: str = "data_base"):
        """Býr til rétta slóð fyrir .csv skrárnar og býr til repo object til að
        geta lesið og skrifað í allar .csv skrárnar"""
        matches_path = os.path.join(base_path, "matches.csv")
        self._matches_repo = MatchesData(matches_path)

        players_path = os.path.join(base_path, "players.csv")
        self._players_repo = PlayersData(players_path)

        tournaments_path = os.path.join(base_path, "tournaments.csv")
        self._tournaments_repo = TournamentData(tournaments_path)

        teams_path = os.path.join(base_path, "teams.csv")
        self._teams_repo = TeamData(teams_path)


    def read_all_matches(self) -> list[Match]:
        """Les matches.csv og skilar lista af Match objects"""
        return self._matches_repo.read_all()

    def save_all_matches(self, matches: list[Match]) -> None:
        """Skrifar Match objects inn í matches.csv skránna"""
        self._matches_repo.write_all(matches)

    def read_all_players(self) -> list[Player]:
        """Les players.csv og skilar lista af Player objects"""
        return self._players_repo.read_all()

    def save_all_players(self, players: list[Player]) -> None:
        """Skrifar Player objects inn í players.csv skránna """
        self._players_repo.write_all(players)

    def read_all_teams(self) -> list[Team]:
        """Les teams.csv og skilar lista af Team objects"""
        return self._teams_repo.read_all()

    def save_all_teams(self, teams: list[Team]) -> None:
        """Skrifar Team objects inn í teams.csv skránna"""
        self._teams_repo.write_all(teams)

    def read_all_tournaments(self) -> list[Tournament]:
        """Les tournaments.csv og skilar lista af Tournament objects"""
        return self._tournaments_repo.read_all()

    def save_all_tournaments(self, tournaments: list[Tournament]) -> None:
        """Skrifar Tournament object inn í tournaments.csv skránna"""
        self._tournaments_repo.write_all(tournaments)