from data.matches_data import MatchesData 


class Matches:
    """Represents a match between two teams"""

    def __init__(self, match_id: int, team_a: Team, team_b: Team, scheduled_date: datetime, server_id: str, result: Optional[str] = None, completed = bool):
        self.match_id = match_id              
        self.team_a = team_a                  
        self.team_b = team_b                
        self.scheduled_date = scheduled_date  
        self.server_id = server_id           
        self.result = result
        self.completed = completed  