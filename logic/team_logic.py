from data.data_api import DataApi
from models.model_team import Team
from models.model_match import Match
from models.exceptions import ValidationError


class TeamLogic:
    """Handles the logic for teams."""

    def __init__(self, data_api):
        self._data = data_api

    def create_team(self, name: str, captain_handle: str, player_handles: list[str]) -> Team:
        """Creates a new team and validates rules such as player count and captain presence."""

        # Validate unique team name
        all_teams = self._data.read_all_teams()
        if any(team.team_name == name for team in all_teams):
            raise ValidationError(f"Liðið '{name}' er þegar til.")

        # Validate player list contains captain
        if captain_handle not in player_handles:
            raise ValidationError("Captain must be included in the player list.")

        # Check team size
        if len(player_handles) < 3:
            raise ValidationError("Team must have at least 3 players.")
        if len(player_handles) > 5:
            raise ValidationError("Team cannot exceed 5 players.")

        # Checks if player exists and is not in another team
        all_players = self._data.read_all_players()

        for handle in player_handles:
            player = next((p for p in all_players if p.handle == handle), None)
            if player is None:
                raise ValidationError(f"Player '{handle}' does not exist.")


            if player.team_name and player.team_name != name:
                raise ValidationError(
                    f"Player '{handle}' is already assigned to another team: '{player.team_name}'."
                )

        # Make new team ID
        existing_ids = [team.team_id for team in all_teams]
        new_id = max(existing_ids) + 1 if existing_ids else 1

        # Create team model
        new_team = Team(
            team_id = new_id,
            team_name = name,
            captain_handle = captain_handle,
            website = "",   
            logo = "",
        )

        all_teams.append(new_team)
        self._data.save_all_teams(all_teams)

        for p in all_players:
            if p.handle in player_handles:
                p.team_name = name
        self._data.save_all_players(all_players)

        return new_team

    def get_team_details(self, team_id: int) -> Team:
        """Returns a Team object by ID."""
        teams = self._data.read_all_teams()
        for team in teams:
            if team.team_id == team_id:
                return team
        raise ValidationError("Team not found.")

    def _get_team_and_players(self, team_id: int):
        """Helper: returns (team, [players_in_team])."""
        teams = self._data.read_all_teams()
        players = self._data.read_all_players()

        team = next((t for t in teams if t.team_id == team_id), None)
        if team is None:
            raise ValidationError("Team not found.")

        team_players = [p for p in players if p.team_name == team.team_name]
        return team, teams, players, team_players

    def add_player(self, team_id: int, player_handle: str):
        """Adds a player to an existing team."""

        team, all_teams, all_players, team_players = self._get_team_and_players(team_id)

        # Check if player exists
        player = next((p for p in all_players if p.handle == player_handle), None)
        if player is None:
            raise ValidationError(f"Player '{player_handle}' does not exist.")

        # Prevent player from joining multiple teams
        if player.team_name and player.team_name != team.team_name:
            raise ValidationError(
                f"Player '{player_handle}' is already assigned to another team: '{player.team_name}'."
            )

        # Prevent duplicates within this team
        if any(p.handle == player_handle for p in team_players):
            raise ValidationError("Player already in team.")

        # Enforce max size
        if len(team_players) >= 5:
            raise ValidationError("Team cannot exceed 5 players.")

        # Assign player to this team
        player.team_name = team.team_name
        self._data.save_all_players(all_players)
        return team

    def remove_player(self, team_id: int, player_handle: str):
        """Removes a player from an existing team."""
        team, all_teams, all_players, team_players = self._get_team_and_players(team_id)

        # Find player in this team
        player = next((p for p in team_players if p.handle == player_handle), None)
        if player is None:
            raise ValidationError("Player not in team.")

        # Prevent the captain from being removed
        if player_handle == team.captain_handle:
            raise ValidationError("Cannot remove the captain of the team.")

        # Enforce minimum team size (after removal must still be >= 3)
        if len(team_players) <= 3:
            raise ValidationError("Team must have at least 3 players.")

        # Remove from team by clearing team_name
        player.team_name = ""
        self._data.save_all_players(all_players)
        return team

    def list_team_players(self, team_id: int):
        """Returns a list of Player models for a given team."""
        team, _, all_players, team_players = self._get_team_and_players(team_id)
        return team_players

    def validate_team_size(self, team_id: int) -> bool:
        """Checks if the team satisfies the minimum and maximum size rules."""
        _, _, _, team_players = self._get_team_and_players(team_id)
        size = len(team_players)
        return 3 <= size <= 5

    def change_captain(self, team_id: int, new_captain_handle: str):
        """Assigns a new captain, ensuring player is in team."""
        team, all_teams, all_players, team_players = self._get_team_and_players(team_id)

        if not any(p.handle == new_captain_handle for p in team_players):
            raise ValidationError("New captain must be a team member.")

        team.captain_handle = new_captain_handle
        self._data.save_all_teams(all_teams)
        return team
