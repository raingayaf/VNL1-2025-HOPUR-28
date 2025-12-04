import os
from models.match import Match          
from data.matches_data import MatchesData


class DataApi:
    """API notaður til að logic layer geti sótt í data layer"""
    def __init__(self, base_path: str = "data_base"):

        self._matches_repo = MatchesData(matches_path)
        
#inniheldur self.breytur af öllum data klösunum. Þannig að þegar logic player kallar á readall() 




    def read_all_matches(self) -> list[Match]:
        return self._matches_repo.read_all()

    def save_all_matches(self, matches: list[Match]) -> None:
        self._matches_repo.write_all(matches)

