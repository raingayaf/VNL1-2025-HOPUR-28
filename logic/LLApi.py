from data.data_api import DataApi
from logic.team_logic import TeamLogic
from logic.match_logic import MatchLogic
from logic.player_logic import PlayerLogic
from logic.tournament_logic import TournamentLogic
from logic.schedule_logic import ScheduleLogic

from models.model_tournament import Tournament
from models.model_player import Player
from models.model_team import Team
from models.model_match import Match
from models.exceptions import ValidationError

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
        self._schedule_logic = ScheduleLogic(self._data_api)

    #-------------------------TOURNAMENT-RELATED-METHODS-------------------------
    def create_tournament(self,
        name: str,
        venue: str,
        start_date: str,
        end_date: str,
        contact_name: str,
        contact_email: str,
        contact_phone: str,
        max_servers: int,
    ) -> Tournament:
        """UI calls this to create a new tournament."""
        return self._tournament_logic.create_tournament(
            name,
            venue,
            start_date,
            end_date,
            contact_name,
            contact_email,
            contact_phone,
            max_servers,
        ) 
        
    def get_all_tournaments(self) -> list[Tournament]:
        """UI calls this to get all tournaments."""
        return self._tournament_logic.get_all_tournaments()
    
    def get_tournament_name_list(self) -> list[str]:
        """UI calls this to get a list of tournament names."""
        return self._tournament_logic.get_tournament_name_list()
    
    def get_tournament_by_index(self, index: int) -> Tournament:
        """UI calls this to get a single tournament by its index."""
        return self._tournament_logic.get_tournament_by_index(index)
    
    def generate_round_of_16(self, tournament: Tournament, teams: list[Team]):
        """generate day 1 matches (R16)"""
        team_names = [t.team_name for t in teams]
        return self._match_logic.generate_round_of_16(tournament.tournament_id, team_names)
    
    def generate_quarterfinals(self, tournament: Tournament):
        """Generate day 2 morning matches from R16 winners"""
        return self._match_logic.generate_quarterfinals(tournament.tournament_id)
    
    def generate_semifinals(self, tournament: Tournament):
        """Generate day 2 later (SF) matches from QF winners"""
        return self._match_logic.generate_semifinals(tournament.tournament_id)
    
    def generate_final(self, tournament: Tournament):
        """Generate day 3 final from SF winners"""
        return self._match_logic.generate_final(tournament.tournament_id)
    
    def get_schedule_for_tournament(self, tournament):
        """Build schedule for tournament"""
        return self._schedule_logic.build_schedule_for_tournament(tournament)
    
    def record_match_result(self, match_id: int, score_a: int, score_b: int):
        """Record match results"""
        return self._match_logic.record_match_result(match_id, score_a, score_b)
    
    def get_matches_for_tournament(self, tournament) -> list[Match]:
        """Gets matches for tournament"""
        all_matches = self._data_api.read_all_matches()
        return [m for m in all_matches if m.tournament_id == tournament.tournament_id]
    
    #-------------------------TEAM-RELATED-METHODS---------------------------

    def create_team(self,
        name: str,
        captain_handle: str,
        player_handles: list[str],
        website: str = '',
        logo: str = '',
    ) -> Team:
        """UI calls this to create a team."""
        return self._team_logic.create_team(
            name, 
            captain_handle, 
            player_handles,
            website,
            logo,
        )
    
    def create_team_with_players(self,
        name: str,
        captain_handle: str,
        registered_team_players: list[dict[str, str]],
        website: str = "",
        logo: str = "",
    ):
        """ """
        for pdata in registered_team_players:
            self._player_logic.create_player(
            name = pdata["name"],
            date_of_birth = pdata["date_of_birth"],
            address = pdata["address"],
            phone = pdata["phone"],
            email = pdata["email"],
            link = pdata["link"],
            handle = pdata["handle"],
            team_name = name,
            )                         
        
        players_handles = [p["handle"] for p in registered_team_players]
        return self._team_logic.create_team(
            name = name,
            captain_handle = captain_handle,
            player_handles = players_handles,
            website = website,
            logo = logo,
        )
    
    def get_team_info_for_captain(self, captain_handle: str, team_name: str):
        """ """
        teams = self._team_logic.get_all_teams()

        matching_team = None
        for team in teams:
            if team.team_name == team_name and team.captain_handle == captain_handle:
                matching_team = team
                break 

        if matching_team is None:
            raise ValueError(f"Fyrirliði '{captain_handle}' tilheyrir ekki liðinu '{team_name}.")
        
        players = self._player_logic.get_players_for_team(team_name)

        return {
            "team": matching_team,
            "players": players,
            "captain_handle": captain_handle,
        }
        


    def team_name_exists(self, team_name: str) -> bool:
        """ """
        return self._team_logic.team_name_exists(team_name)
    
    def get_team_details(self, team_id: int):
        """ """
        return self._team_logic.get_team_details(team_id)

    def get_all_teams(self) -> list[Team]:
        """Return all teams."""
        return self._team_logic.get_all_teams()

    def get_teams_for_tournament(self, tournament_id: int) -> list[Team]:
        """UI calls this to get all teams participating in a tournament."""
        return self._team_logic.get_teams_for_tournament(tournament_id)
    
    #-------------------------PLAYER-RELATED-METHODS---------------------------

    def create_player(self,
        name: str,
        date_of_birth: str,
        address: str,
        phone: str,
        email: str,
        link: str,
        handle: str,
        team_name: str,
    ) -> Player:
        """UI calls this to create a player and it forwards to PlayerLogic."""
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
    
    def handle_exists(self, handle: str) -> bool:
        """Return True if a player handle already exists."""
        return self._player_logic.handle_exists(handle)
    
    def get_players_for_team(self, team_name: str) -> list[Player]:
        """UI calls this to get all players on team."""
        return self._player_logic.get_players_for_team(team_name)
    
    def get_all_players(self):
        return self._data_api.read_all_players()
    
    def get_all_player_names(self) -> list[str]:
        players = self.get_all_players()
        return [player.name for player in players]
    
    def update_player(self, player: Player) -> None:
        """UI calls this to update a player's information."""
        self._player_logic.update_player(player)

    #-------------------------MATCH-RELATED-METHODS---------------------------

    def create_match(self,
        tournament_id: int,
        round_name: str,
        match_number: int,
        team_a_name: str,
        team_b_name: str,
        match_date: str,
        match_time: str,
        server_id: str,
    ) -> Match:
        """UI calls this to create match."""
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
    
    def get_matches_for_tournament(self, tournament_id: int) -> list[Match]:
        """UI calls this to get all matches for a given tournament."""
        return self._match_logic.get_matches_for_scoreboard(tournament_id)
    #-------------------------VALIDATION-HELPERS-FOR-UI--------------------------
    def validate_team_name_format(self, team_name: str) -> str:
        return self._team_logic._validate_team_name_format(team_name)
    
    def validate_captain_handle_format(self, handle: str) -> str:
        return self._team_logic._validate_handle_format(handle)
    
    def validate_team_website(self, website: str) -> str:
        return self._team_logic.validate_team_website(website)
    
    def validate_team_logo(self, logo: str) -> str:
        return self._team_logic.validate_logo_value(logo)
    
