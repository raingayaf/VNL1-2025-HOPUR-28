
from models.model_match import Match
from models.exceptions import ValidationError


class MatchLogic:
    def __init__(self, data_api):
        self._data = data_api



    def create_match(self,
        tournament_id: int,
        round: str,
        match_number: int,
        team_a_name: str,
        team_b_name: str,
        match_date: str,
        match_time: str,
        server_id: str,):
        """Creates a new match between two teams"""

        #Checks if user chooses same team twice
        if team_a_name == team_b_name:
            raise ValidationError("Ekki er hægt að velja sama liðið tvisvar")

        #Checks all teams and raises errors if team doesn't exist
        all_teams = self._data.read_all_teams()
        team_a_exists = any(team.team_name == team_a_name for team in all_teams)
        team_b_exists = any(team.team_name == team_b_name for team in all_teams)

        if not team_a_exists:
            raise ValidationError(f"Liðið '{team_a_name}' er ekki á skrá.")
        if not team_b_exists:
            raise ValidationError(f"Liðið '{team_b_name}' er ekki á skrá.")
        

        #Loads existing matches
        all_matches = self._data.read_all_matches()

        #Checks the highest existing Id to assign new Id to new match
        existing_ids = []
        for match in all_matches:
            existing_ids.append(match.match_id)
        
        highest_id = max(existing_ids)
        new_id = highest_id + 1

        new_match = Match(
            match_id = new_id,
            tournament_id = tournament_id,
            round = round,
            match_number = match_number,
            team_a_name = team_a_name,
            team_b_name = team_b_name,
            match_date = match_date,
            match_time = match_time,
            server_id = server_id,
            score_a = 0,
            score_b = 0,
            winner_team_name = "",
            completed = False,

        )
        matches = self._data.read_all_matches()
        matches.append(new_match)
        self._data.save_all_matches(matches)

        return new_match