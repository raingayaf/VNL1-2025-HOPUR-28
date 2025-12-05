from datetime import date

class Match:
    """Represents a match between two teams"""

    def __init__(self, match_id: int, tournament_id: str,
team_name_a: Team, team_name_b: Team, match_date: date,match_number, match_time: int, server_id: str, score_a: int, score_b: int, winner_team_name: Team, completed = bool):

        self.match_id = match_id
        self.tournament_id = tournament_id
        self.team_name_a = team_name_a
        self.team_name_b = team_name_b
        self.match_date = match_date
        self.match_number = match_number
        self.match_time = match_time
        self.server_id = server_id
        self.score_a = score_a
        self.score_b = score_b
        self.winner_team_name = winner_team_name
        self.completed = completed
