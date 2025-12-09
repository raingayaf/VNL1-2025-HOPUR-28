from data.data_api import DataApi
from logic.team_logic import TeamLogic
from logic.match_logic import MatchLogic
from logic.player_logic import PlayerLogic
from logic.tournament_logic import TournamentLogic
from models.model_tournament import Tournament
from models.model_player import Player
from models.model_team import Team
from models.model_match import Match


class LLApi:
    """
    Connects UI to Logic layer.
    UI layer should only talk to this class, not directly to logic or data.
    """

    def __init__(self) -> None:
        self._data_api = DataApi()
        self._team_logic = TeamLogic(self._data_api)
        self._match_logic = MatchLogic(self._data_api)
        self._player_logic = PlayerLogic(self._data_api)
        self._tournament_logic = TournamentLogic(self._data_api)

    def create_team(self, name: str, captain_handle: str, player_handles: str):

        return self._team_logic.create_team(name, captain_handle, player_handles)

    def get_team_details(self, team_id: int):
        return self._team_logic.get_team_details(team_id)

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
        return self._player_logic.create_player(
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
        return self._match_logic.create_match(
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
        return self._data_api.read_all_tournaments()

    def get_tournament_name_list(self) -> list[str]:
        """UI calls this to get a list of tournament names."""
        return self._tournament_logic.get_tournament_name_list()

    def get_all_tournaments(self) -> list[Tournament]:
        """UI calls this to get all tournaments."""
        return self._tournament_logic.get_all_tournaments()

    def get_tournament_by_index(self, index: int) -> Tournament:
        """UI calls this to get a single tournament by its index."""
        return self._tournament_logic.get_tournament_by_index(index)

    def get_teams_for_tournament(self, tournament_id: int) -> list[Team]:
        """UI calls this to get all teams participating in a tournament."""
        return self._team_logic.get_teams_for_tournament(tournament_id)

    def get_players_for_team(self, team_name: str) -> list[Player]:
        """UI calls this to get all players on team."""
        return self._player_logic.get_players_for_team(team_name)

    def get_all_teams(self):
        return self._data_api.read_all_teams()
    
    # Team related

    def team_name_exists(self, team_name: str) -> bool:
        return self._team_logic.team_name_exists(team_name)
    
    def create_team(self, team_name: str, captain_handle: str):
        return self._team_logic.create_team(team_name, captain_handle)
    
    # Player related
    def handle_exists(self, handle: str) -> bool:
        return self._player_logic.handle_exists(handle)
    


    def create_tournament(
        self,
        name: str,
        venue: str,
        start_date: str,
        end_date: str,
        contact_name: str,
        contact_email: str,
        contact_phone: str,
        max_servers: int,
    ):

        return self.create_tournament(
            name,
            venue,
            start_date,
            end_date,
            contact_name,
            contact_email,
            contact_phone,
            max_servers,
        )
