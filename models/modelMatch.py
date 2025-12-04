

class Match:
    """Represents a match between two teams"""

    def __init__(self, match_id: int, team_1: Team, team_2: Team, match_date: datetime, match_time: int, server_id: str, result: Optional[str] = None, completed = bool):
        self.match_id = match_id              
        self.team_1 = team_1                  
        self.team_2 = team_2                
        self.match_date = match_date 
        self.match_time = match_time 
        self.server_id = server_id           
        self.result = result
        self.completed = completed  