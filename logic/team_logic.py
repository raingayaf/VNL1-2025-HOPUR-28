from models.modelTeam import Team
from models.exceptions import ValidationError


class TeamLogic:
    """handles the logic for teams"""
    def __init__(self, data_api):
        self._data = data_api


    def create_team(self, name: str, captain_handle: str, player_handles: list):
        """Creates a new team and validates rules such as player count and captain presence."""

        # Validate unique team name
        all_teams = self._data.read_all_teams()
        if any(team.team_name == name for team in all_teams):
            raise ValidationError(f"Liðið '{name}' er þegar til.")

        # Validate player list contains captain
        if captain_handle not in player_handles:
            raise ValidationError("Captain must be included in the player list.")

        # raise errror if team has less than 3 or more than 5 players
        if len(player_handles) < 3:
            raise ValidationError("Team must have at least 3 players.")
        if len(player_handles) > 5:
            raise ValidationError("Team cannot exceed 5 players.")
        
        # prevent players from belonging to multiple teams
        for team in all_teams:
            for member in team.player_handles:
                if member in player_handles:
                    raise ValidationError(f"Player '{member}' is already assigned to another team.c")

        # Ensure each player exists
        all_players = self._data.read_all_players()
        for handle in player_handles:
            if not any(p.player_handle == handle for p in all_players):
                raise ValidationError(f"Player '{handle}' does not exist.")

        # Determine new team ID
        existing_ids = [team.team_id for team in all_teams]
        new_id = max(existing_ids) + 1 if existing_ids else 1

        # Create Team model
        new_team = Team(
            team_id=new_id,
            team_name=name,
            captain_handle=captain_handle,
            player_handles=player_handles
        )

        all_teams.append(new_team)
        self._data.save_all_teams(all_teams)

        return new_team


    def get_team_details(self, team_id: int):
        """Returns a Team object by ID."""
        teams = self._data.read_all_teams()
        for team in teams:
            if team.team_id == team_id:
                return team
        raise ValidationError("Team not found.")


    def add_player(self, team_id: int, player_handle: str):
        """Adds a player to an existing team."""

        teams = self._data.read_all_teams()
        players = self._data.read_all_players()

        # Validate player exists
        if not any(p.player_handle == player_handle for p in players):
            raise ValidationError(f"Player '{player_handle}' does not exist.")

        # prevent player from joining multiple teams
        for t in teams:
            if player_handle in t.player_handles:
                raise ValidationError(f"Player '{player_handle}' is already assigned to another team.")
        
        
        # Find team
        for team in teams:
            if team.team_id == team_id:

                # Prevent duplicates
                if player_handle in team.player_handles:
                    raise ValidationError("Player already in team.")
                
                if len(team.player_handles) >= 5:
                    raise ValidationError("Team cannot exceed 5 players.")

                team.player_handles.append(player_handle)
                self._data.save_all_teams(teams)
                return team

        raise ValidationError("Team not found.")
        



    def remove_player(self, team_id: int, player_handle: str):
        """Removes a player from an existing team."""
        teams = self._data.read_all_teams()

        for team in teams:
            if team.team_id == team_id:

                if player_handle not in team.player_handles:
                    raise ValidationError("Player not in team.")

                # Prevent the captain from being removed
                if player_handle == team.captain_handle:
                    raise ValidationError("Cannot remove the captain of the team.")
                
                # enforce minimum team size

                if len(team.player_handles) <= 3:
                    raise ValidationError()

                team.player_handles.remove(player_handle)
                self._data.save_all_teams(teams)
                return team

        raise ValidationError("Team not found.")


    def list_team_players(self, team_id: int) -> list:
        """Returns a list of Player models for a given team."""
        team = self.get_team_details(team_id)
        all_players = self._data.read_all_players()

        return [p for p in all_players if p.player_handle in team.player_handles]


    def validate_team_size(self, team_id: int) -> bool:
        """Checks if the team satisfies the minimum and maximum size rules."""
        team = self.get_team_details(team_id)
        size = len(team.player_handles)
        return 3 <= size <= 5


    def change_captain(self, team_id: int, new_captain_handle: str):
        """Assigns a new captain, ensuring player is in team."""
        teams = self._data.read_all_teams()

        for team in teams:
            if team.team_id == team_id:

                if new_captain_handle not in team.player_handles:
                    raise ValidationError("New captain must be a team member.")

                team.captain_handle = new_captain_handle
                self._data.save_all_teams(teams)
                return team

        raise ValidationError("Team not found.")
