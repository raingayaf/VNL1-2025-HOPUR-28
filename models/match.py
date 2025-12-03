from datetime import datetime
from typing import Optional
from team import Team




class Match:
    """Represents a match between two teams"""

    def __init__(self, match_id: int, team_a: Team, team_b: Team, scheduled_date: datetime, server_id: str, result: Optional[str] = None):
        self.match_id = match_id              
        self.team_a = team_a(Team)                  
        self.team_b = team_b(Team)                 
        self.scheduled_date = scheduled_date  
        self.server_id = server_id           
        self.result = result                  

 