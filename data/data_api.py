import os
from models.match import Match          
from data.matches_data import MatchesData


class DataApi:
    """API notaður til að logic layer geti sótt í data layer"""
    def __init__(self, base_path: str = "data_base"):
        #players_path = os.path.join(base_path, "players.csv")
        #teams_path = os.path.join(base_path, "teams.csv")
        matches_path = os.path.join(base_path, "matches.csv")
        #tournaments_path = os.path.join(base_path, "tournaments.csv")
        self._matches_repo = MatchesData(matches_path)
        




    def read_all_matches(self) -> list[Match]:
        return self._matches_repo.read_all()

    def save_all_matches(self, matches: list[Match]) -> None:
        self._matches_repo.write_all(matches)
