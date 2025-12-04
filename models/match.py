from datetime import date
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




class Players:
    
    def __init__(self, player_id = int, name = str, date_of_birth = date, address = str, phone = str, email = str, link = str, handle = str, team_name = str):
        self.player_id = player_id
        self.name = name
        self.date_of_birth = date_of_birth
        self.address = address
        self.phone = phone
        self.email = email
        self.link = link
        self.handle = handle
        self.team_name = team_name


class Teams:
    def __init__(self, team_id = int, team_name = str, captain_handle = str, website = str, logo = str):
        self.team_id = team_id
        self.team_name = team_name
        self.captain_handle = captain_handle
        self.website = website
        self.logo = logo

class Tournaments:
    def __init__(self, tournament_id, name, venue, start_date, end_date, contact_name, contact_email, contact_phone, max_servers):
        self.tournament_id = tournament_id
        self.name = name
        self.venue = venue
        self.start_date = start_date
        self.end_date = end_date
        self.contact_name = contact_name
        self.contact_email = contact_email
        self.contact_phone = contact_phone
        self.max_servers = max_servers
        






