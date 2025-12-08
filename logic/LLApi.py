from data.data_api import DataApi
from logic.team_logic import TeamLogic
from logic.match_logic import MatchLogic
from logic.player_logic import PlayerLogic


class LLApi:
    """
    Connects UI to Logic layer.
    UI layer should only talk to this class, not directly to logic or data.
    """

    def __init__(self, data_api: DataApi):
        self.data_api = data_api
        self.team_logic = TeamLogic(data_api)       
        self.match_logic = MatchLogic(data_api)
        self.player_logic = PlayerLogic(data_api)

    
    def create_team(self, name, captain_handle, player_handles):
        return self.team_logic.create_team(name, captain_handle, player_handles)

    def get_team_details(self, team_id):
        return self.team_logic.get_team_details(team_id)

    
    def create_player(
        self,
        name: str,
        date_of_birth: str,
        address: str,
        phone: str,
        email: str,
        link: str,
        handle: str,
        team_name: str,
    ):
        """UI calls this to create a player it forwards to PlayerLogic."""
        return self.player_logic.create_player(
            name,
            date_of_birth,
            address,
            phone,
            email,
            link,
            handle,
            team_name,
        )


    def create_match(
        self,
        tournament_id: int,
        round_name: str,
        match_number: int,
        team_a_name: str,
        team_b_name: str,
        match_date: str,
        match_time: str,
        server_id: str,
    ):
        return self.match_logic.create_match(
            tournament_id,
            round_name,
            match_number,
            team_a_name,
            team_b_name,
            match_date,
            match_time,
            server_id,
        )
