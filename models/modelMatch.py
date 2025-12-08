class Match:
    """Represents a match between two teams."""

    def __init__(
        self,
        match_id: int,
        tournament_id: int,
        round: str,
        match_number: int,
        team_a_name: str,
        team_b_name: str,
        match_date: str,   
        match_time: str,   
        server_id: str,
        score_a: int,
        score_b: int,
        winner_team_name: str,
        completed: bool = False,):


        self.match_id = match_id
        self.tournament_id = tournament_id
        self.round = round
        self.match_number = match_number
        self.team_a_name = team_a_name
        self.team_b_name = team_b_name
        self.match_date = match_date
        self.match_time = match_time
        self.server_id = server_id
        self.score_a = score_a
        self.score_b = score_b
        self.winner_team_name = winner_team_name
        self.completed = completed
