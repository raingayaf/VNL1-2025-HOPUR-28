from data.data_api import DataApi

class TournamentDTO:
    """Represents a Tournament passed through the Api"""
    def __init__(self, name, start_date, end_date, venue, contact_person_id):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.venue = venue
        self.contact_person_id = contact_person_id


class PlayerDTO:
    """Represent a player passed through the Api"""
    def __init__(self, player_id, name, age, email):
        self.player_id = player_id
        self.name = name
        self.age = age
        self.email = email


class MatchDTO:
    """Represents a match passed through the Api"""
    def __init__(self, match_id, team1_id, team2_id, start_time, winner_id=None):
        self.match_id = match_id
        self.team1_id = team1_id
        self.team2_id = team2_id
        self.start_time = start_time
        self.winner_id = winner_id


class TeamDTO:
    """Represents a Team passed through the Api"""
    def __init__(self, team_id, name):
        self.team_id = team_id
        self.name = name




class LLApi:
    """Takes data from UI layer and transfers to logic layer"""
    def __init__(self, data_api):
        self.data_api = data_api


    def create_tournament(self, dto: TournamentDTO) -> int:
        return self.data_api.save_tournament(dto)


    def list_tournaments(self) -> list:
        return self.data_api.load_tournaments()


    def register_player(self, dto: PlayerDTO) -> int:
        return self.data_api.save_player(dto)


    def add_team(self, dto: TeamDTO) -> int:
        return self.data_api.save_team(dto)


    def schedule_match(self, dto: MatchDTO) -> int:
        return self.data_api.save_match(dto)


    def list_matches(self) -> list:
        return self.data_api.load_matches()


    def record_match_result(self, match_id: int, winner_team_id: int):
        self.data_api.update_match_winner(match_id, winner_team_id)
