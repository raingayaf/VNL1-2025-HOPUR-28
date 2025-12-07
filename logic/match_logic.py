from datetime import date
from models.modelMatch import Match
from models.excpetions import ValidationError


class MatchLogic:
    def __init__(self, data_api):
        self._data = data_api
    


    def create_match(self, team_a_name, team_b_name, match_date):
        if team_a_name == team_b_name:
            raise ValidationError("Ekki er hægt að velja sama liðið tvisvar")
        team_a_object = self._data.team_repo.get_by_name(team_a_name)

        if team_a_object is None:
            raise ValidationError(f"Liðið '{team_a_name}' er ekki á skrá.")

        team_b_object = self._data.team_repo.get_by_name(team_b_name)
        if team_b_object is None:
            raise ValidationError(f"Liðið '{team_b_name}' er ekki á skrá.")

        #Loads existing matches
        all_matches = self._data.matches_data.read_all()


