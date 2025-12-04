#TeamLL
#-Team
#-data: TeamData
#+ createTeam(name: string, captainHandle : string, playerHandles: list)
#+ getTeamDetails(teamld : int):
#Team
#+addPlayer(teamld : int,
#playerHandle : string)
#+ removePlayer(teamld : int,
#playerHandle : string)
#+listTeamPlayers : list
#+ validateTeamSize(teamid : int)
#bool
#+ changePlayer(captainHandle : string, PlayerData: Player)
#+registerTeam(captainHandle :
#string, TeamData: Team)
#+ changeCaptain(team: Team, newCaptain: Player)


from models.team import Team       
from models.player import Player   
from models.team_data import TeamData 


class TeamLL:
    def __init__(self):
        