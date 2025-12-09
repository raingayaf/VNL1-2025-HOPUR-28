from data.data_api import DataApi
from logic.team_logic import TeamLogic
from logic.match_logic import MatchLogic
from logic.player_logic import PlayerLogic
from logic.tournament_logic import TournamentLogic


class LLApi:
    """
    Connects UI to Logic layer.
    UI layer should only talk to this class, not directly to logic or data.
    """

    def __init__(self):
        self.data_api = DataApi()
        self.team_logic = TeamLogic(self.data_api)
        self.match_logic = MatchLogic(self.data_api)
        self.player_logic = PlayerLogic(self.data_api)

    def create_team(self, name: str, captain_handle: str, player_handles: str):

        return self.team_logic.create_team(name, captain_handle, player_handles)

    def get_team_details(self, team_id: int):
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

    def get_all_tournaments(self):
        """UI calls this to get a list of all tournaments."""
        return self.data_api.read_all_tournaments()


    def create_tournament(self, 
                name: str, venue: str, 
                start_date: str, 
                end_date: str, 
                contact_name: str, 
                contact_email: str, 
                contact_phone: str,
                max_servers: int);
        
        return self.create_tournament(
            name,
            start_date,
            end_date,
            contact_name,
            contact_email,
            contact_phone,
            max_servers
        )