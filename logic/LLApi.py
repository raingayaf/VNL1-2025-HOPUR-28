from data.data_api import DataApi
from logic.team_logic import TeamLL
from datetime import date
#Allt hérna inni er tengt UML nöfnunum, þannig það er mjög líklegt að breytinga þurfi
class LLApi:
    """
    Connects UI to Logic later.
    UI layer should only talk to this class, not directly to logic or data.
    """
    def __init__(self, data_api):
        self.data_api = data_api
        self.team_logic = TeamLogic(data_api)

    def create_team(self, name, captain_handle, player_handles):
        return self.team_logic.create_team(name, captain_handle, player_handles)

    def get_team_details(self, team_id):
        return self.team_logic.get_team_details(team_id)