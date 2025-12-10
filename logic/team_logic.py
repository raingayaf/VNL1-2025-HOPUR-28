from data.data_api import DataApi
from models.model_team import Team
from models.model_match import Match
from models.model_player import Player
from models.exceptions import ValidationError

class TeamLogic:
    """Handles team related logic."""

    def __init__(self, data_api: DataApi) -> None:
        """Initializes the logic class with a refrence to the data API."""
        self._data_api = data_api

    #------------------METHODS-THAT-GET-DATA------------------------
    # ÞETTA ER NOTAÐ
    def get_all_teams(self) -> list[Team]:
        """Returns a list of all teams from the data layer."""
        return self._data_api.read_all_teams()
    
    # VEIT EKKI HVORT VIÐ NOTUM ÞETTA
    def team_name_exists(self, team_name: str) -> bool:
        """Return True if a team name already exists."""
        teams = self._data_api.read_all_teams()
        return any(team.team_name == team_name for team in teams)
    
    # VEIT EKKI HVORT VIÐ NOTUM ÞETTA
    def get_team_details(self, team_id: int) -> Team:
        """Returns a Team object by ID."""
        teams = self._data_api.read_all_teams()
        for team in teams:
            if team.team_id == team_id:
                return team
        raise ValidationError("Team not found.")

    # ÞETTA ER NOTAÐ
    def get_matches_for_tournaments(self, tournament_id: int) -> list[Match]:
        """Return all matches from selected tournament."""
        matches = self._data_api.read_all_matches()
        # Iterate over every match belonging to a given tournament ID and creates a list
        return [match for match in matches if match.tournament_id == tournament_id]

    # ÞETTA ER NOTAÐ
    def get_teams_for_tournament(self, tournament_id: int) -> list[Team]:
        """Returns a list of all teams competing in a tournament"""
        #Gets a list of all matches belonging to a tournament id
        matches = self.get_matches_for_tournaments(tournament_id)

        #Creates a set of all teams in tournament to remove duplicates
        team_names: set[str] = set()
        for match in matches:
            team_names.add(match.team_a_name)
            team_names.add(match.team_b_name)
        #Retrieves a list of all teams
        all_teams = self.get_all_teams()
        #Filters only the teams participating
        participating_teams = [
            team for team in all_teams if team.team_name in team_names
        ]
        return participating_teams
    

    # def list_team_players(self, team_id: int):
    #     """Returns a list of Player models for a given team."""
    #     teams = self._data_api.read_all_teams()
    #     players = self._data_api.read_all_players()

    #     wanted_team = None

    #     for team in teams:
    #         if team.team_id == team_id:
    #             wanted_team = team

    #     if wanted_team is None:
    #         raise ValidationError("Lið með auðkenni {team_id} fannst ekki.")

    #     team_players = []
    #     for player in players:
    #         if player.team_name == wanted_team.team_name:
    #             team_players.append(player)

    #     return team_players


    # def validate_team_size(self, team_id: int) -> bool:
    #     """Checks if the team satisfies the minimum and maximum size rules."""

    #     teams = self._data_api.read_all_teams()
    #     players = self._data_api.read_all_players()

    #     validate_team = None
    #     for team in teams:
    #         if team.team_id == team_id:
    #             validate_team = team

    #     count = 0
    #     for player in players:
    #         if player.team_name == validate_team.team_name:
    #             count += 1
    #     return 3 <= count <= 5

    #------------------METHODS-THAT-CHANGE-DATA----------------------
    def create_team(self, 
        name: str, 
        captain_handle: str, 
        player_handles: list[str],
        website: str = '',
        logo: str = '',
    ) -> Team:
        """Creates a new team and assigns players to it."""

        all_teams = self._data_api.read_all_teams()

        # Unique team name
        if any(team.team_name == name for team in all_teams):
            raise ValidationError(f"Liðið '{name}' er þegar til.")

        # Validate player list contains captain
        if captain_handle not in player_handles:
            raise ValidationError("Team captain þarf að vera skráður leikmaður.")

        # Check team size
        if len(player_handles) < 3:
            raise ValidationError("Minnst 3 þurfa að vera í liði.")
        if len(player_handles) > 5:
            raise ValidationError("Mest 5 geta verið í hverju liði.")

        # Checks if player exists and is not in another team
        all_players = self._data_api.read_all_players()
        players_by_handle: dict[str, Player] = {
            player.handle: player for player in all_players
            }
        
        # Validate each handle
        for player_handle in player_handles:
            player = players_by_handle.get(player_handle)
            if player is None:
                raise ValidationError(f"Leikmaður {player_handle} er ekki til.")
        if player.team_name and player.team_name != name:
            raise ValidationError(f"Leikmaður {player_handle} er nú þegar skráður í liðið {player.team_name}.")

        # Make new team ID
        new_id = self._generate_new_team_id(all_teams)

        # Create team model
        new_team = Team(
            team_id = new_id,
            team_name = name,
            captain_handle = captain_handle,
            website = website or "",
            logo = logo or "",
            )

        all_teams.append(new_team)
        self._data_api.save_all_teams(all_teams)

        # Assign players to team
        for player in all_players:
            if player.handle in player_handles:
                player.team_name = name
        self._data_api.save_all_players(all_players)

        return new_team


    # def add_player(self, team_id: int, player_handle: str):
    #     """Adds a player to an existing team."""

    #     team, all_players, team_players = self._get_team_and_players(team_id)

    #     # Check if player exists
    #     player = next((p for p in all_players if p.handle == player_handle), None)
    #     if player is None:
    #         raise ValidationError(f"Leikmaður '{player_handle}' er ekki til.")

    #     # Prevent player from joining multiple teams
    #     if player.team_name and player.team_name != team.team_name:
    #         raise ValidationError(
    #             f"Leikmaður '{player_handle}' er nú þegar skráður í liðið: '{player.team_name}'."
    #         )

    #     # Prevent duplicates within this team
    #     if any(p.handle == player_handle for p in team_players):
    #         raise ValidationError("Leikmaður er nú þegar í liði.")

    #     # Enforce max size
    #     if len(team_players) >= 5:
    #         raise ValidationError("Mest geta 5 verið í liði.")

    #     # Assign player to this team
    #     player.team_name = team.team_name
    #     self._data_api.save_all_players(all_players)
    #     return team


    # def remove_player(self, team_id: int, player_handle: str):
    #     """Removes a player from an existing team."""
    #     team, all_players, team_players = self._get_team_and_players(team_id)

    #     player_to_remove = None
    #     for p in team_players:
    #         if p.handle == player_handle:
    #             player_to_remove = p

    #     if player_to_remove is None:
    #         raise ValidationError("Leikmaður er ekki í liði.")

    #     if player_handle == team.captain_handle:
    #         raise ValidationError("Ekki er hægt að fjarlægja fyrirliða úr liði.")

    #     if len(team_players) < 3:
    #         raise ValidationError("Minnst þarf þrjá leikmenn í lið")

    #     #Removes player from team
    #     for p in all_players:
    #         if p.handle == player_handle:
    #             p.team_name = ""
    #     self._data_api.save_all_players(all_players)


    # def change_captain(self, team_id: int, new_captain_handle: str):
    #     """Assigns a new captain, ensuring player is in team."""
    #     team, all_teams, team_players = self._get_team_and_players(team_id)
    #     is_member = False
    #     for player in team_players:
    #         if player.handle == new_captain_handle:
    #             is_member = True
    #     if not is_member:
    #         raise ValidationError("Fyrirliði verður að vera skráður í lið.")
    #     team.captain_handle = new_captain_handle
    #     self._data_api.save_all_teams(all_teams)
    #     return team

    #------------------INTERNAL-HELPER-METHODS----------------------

    # def _get_team_and_players(self, team_id: int):
    #     """Finds a team by it's Id and all it's players"""

    #     #Loads all teams and players
    #     teams = self._data_api.read_all_teams()
    #     players = self._data_api.read_all_players()

    #     #Finds the team matchit team_id
    #     team = None
    #     for t in teams:
    #         if t.team_id == team_id:
    #             team = t

    #     if team is None:
    #         raise ValidationError("Lið er ekki til")
    #     #Collects all players belonging to team
    #     team_players = []
    #     for player in players:
    #         if player.team_name == team.team_name:
    #             team_players.append(player)

    #     return team, players, team_players

    def _generate_new_team_id(self, teams: list[Team]) -> int:
        """Return next integer ID after the current max or 1 if no teams."""
        if not teams:
            return 1
        existing_ids = [team.team_id for team in teams]
        return max(existing_ids) + 1
    

    


    


    

    
