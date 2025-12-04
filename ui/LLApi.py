import 


from datetime import date
#<< Interface>> LLApi
#+ createTournament(name: String, start: date, end:
#date, venue: String, contact: Person)

#+addTeamToTournament(tournamentid: int, team:
#Team): bool

#+ createMatch(team1: Team, team2: Team, time:
#int): Match

#+registerPlayer (player: Player): bool

#+archeiveMatches (matchid: int, winner: Team): void + 
# listTournaments): List < Tournament> +listMatches(tournamentld: int): List < Match>

class LogicApi:
    def __init__(self, name = str, start = date, end = date, venue = str, contact = Person):
        self.name = name
        self.start = start
        self.end = end
        self.venue = venue
        self.contact = contact

    def create_tournament(self, name = str, start = date, end = date, venue = str, contact = Person):


    
        

