from datetime import date

class Tournament:
    """Creates new tournament"""
    def __init__(self, tournament_id: int, name: str, venue: str, start_date: date, end_date: date, contact_name: str, contact_email: str, contact_phone: str, max_servers: int):
        self.tournament_id = tournament_id
        self.name = name
        self.venue = venue
        self.start_date = start_date
        self.end_date = end_date
        self.contact_name = contact_name
        self.contact_email = contact_email
        self.contact_phone = contact_phone
        self.max_servers = max_servers
