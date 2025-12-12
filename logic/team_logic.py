from data.data_api import DataApi
from models.model_team import Team
from models.model_match import Match
from models.model_player import Player
from models.model_tournament import Tournament
from models.exceptions import ValidationError

class TeamLogic:
    """Handles team related logic."""

    def __init__(self, data_api: DataApi) -> None:
        """Initializes the logic class with a refrence to the data API."""
        self._data_api = data_api

    #------------------METHODS-THAT-GET-DATA------------------------
    def get_all_teams(self) -> list[Team]:
        """Returns a list of all teams from the data layer."""
        return self._data_api.read_all_teams()
    
    def team_name_exists(self, team_name: str) -> bool:
        """Return True if a team name already exists."""
        teams = self._data_api.read_all_teams()
        name_casefold = team_name.casefold()
        return any(team.team_name.casefold() == name_casefold for team in teams)

    def get_matches_for_tournaments(self, tournament_id: int) -> list[Match]:
        """Return all matches from selected tournament."""
        matches = self._data_api.read_all_matches()
        # Iterate over every match belonging to a given tournament ID and creates a list
        return [match for match in matches if match.tournament_id == tournament_id]

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
    
    def get_tournaments_for_team(self, team_name: str) -> list[Tournament]:
        """Return all tournaments a selected team has participated in."""
        all_matches = self._data_api.read_all_matches()
        all_tournaments = self._data_api.read_all_tournaments()

        tournament_ids: set[int] = set()
        for match in all_matches:
            if match.team_a_name == team_name or match.team_b_name == team_name:
                tournament_ids.add(match.tournament_id)
        
        tournaments_by_id: dict[int, Tournament] = {t.tournament_id: t for t in all_tournaments}

        result: list[Tournament] = []
        for tid in tournament_ids:
            tournament = tournaments_by_id.get(tid)
            if tournament is not None:
                result.append(tournament)
            return result
        
    def get_team_captain(self, team: Team) -> Player | None:
        """Reads all players and returns team captain"""
        if not team.captain_handle:
            return None
        
        all_players = self._data_api.read_all_players()
        for player in all_players:
            if (player.handle == team.captain_handle
            and player.team_name == team.team_name):
                return player
        return None


    def validate_team_name_format(self, team_name: str) -> str:
        """Public wrapper so UI/LLApi can validate team name."""
        return self._validate_team_name_format(team_name)

    def validate_team_website(self, website: str) -> str:
        """Public wrapper so UI/LLApi can validate team website."""
        return self._normalize_website(website)
    
    def validate_logo_value(self, logo: str) -> str:
        """Public wrapper so UI/LLApi can validate logo"""
        return self._validate_logo_value(logo)

    #------------------METHODS-THAT-CHANGE-DATA----------------------
    def create_team(self, 
        name: str, 
        captain_handle: str, 
        player_handles: list[str],
        website: str = '',
        logo: str = '',
    ) -> Team:
        """Creates a new team and assigns players to it."""

        # validation
        name = self._validate_team_name_format(name)
        captain_handle = self._validate_handle_format(captain_handle)
        website = self._normalize_website(website)
        logo = self._validate_logo_value(logo)

        all_teams = self._data_api.read_all_teams()

        # Unique team name
        name_casefold = name.casefold()
        if any(team.team_name.casefold() == name_casefold for team in all_teams):
            raise ValidationError(f"Liðið '{name}' er nú þegar á skrá!")

        # Validate player list contains captain
        if captain_handle not in player_handles:
            raise ValidationError("Fyrirliði þarf að vera einn af leikmönnunum!")

        # Check team size
        if len(player_handles) < 3:
            raise ValidationError("Fjöldinn má ekki vera minni en 3!")
        if len(player_handles) > 5:
            raise ValidationError("Fjöldinn má ekki vera meiri en 5!")

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

    #------------------INTERNAL-HELPER-METHODS----------------------

    def get_team_and_players_by_name(self, team_name: str):
        """Finds a team by it's Id and all it's players"""

        #Loads all teams and players
        teams = self._data_api.read_all_teams()
        players = self._data_api.read_all_players()

        #Finds the team matchit team_id
        team = None
        for t in teams:
            if t.team_name == team_name:
                team = t
                break

        if team is None:
            raise ValidationError("Lið er ekki til.")
        #Collects all players belonging to team
        team_players: list[Player] = []
        for player in players:
            if player.team_name == team.team_name:
                team_players.append(player)

        return team, players, team_players

    def _generate_new_team_id(self, teams: list[Team]) -> int:
        """Return next integer ID after the current max or 1 if no teams."""
        if not teams:
            return 1
        existing_ids = [team.team_id for team in teams]
        return max(existing_ids) + 1
    
    def _validate_team_name_format(self, team_name: str) -> str:
        """Validate team name by length of name, size and alpha"""
        name = team_name.strip()
        if len(name) < 2:
            raise ValidationError("Nafn liðs verður að vera a.m.k. 2 stafir.")
        if len(name) > 30:
            raise ValidationError("Nafn liðs má ekki vera lengra en 30 stafir.")
        if name.startswith("/"):
            raise ValidationError("Nafn liðs má ekki byrja á '/'.")
        if not any(ch.isalpha() for ch in name):
            raise ValidationError("Nafn liðs verður að innihalda a.m.k einn bókstaf.")
        return name
    
    def _validate_handle_format(self, handle: str) -> str:
        """Validate player handle by name length, starts with and empty string"""
        h = handle.strip()
        if len(h) < 2:
            raise ValidationError("Leikmanna nafn (handle) verður að vera a.m.k. 2 stafir.")
        if len(h) > 30:
            raise ValidationError("Leikmanna nafn (handle) má ekki vera lengra en 30 stafir.")
        if h.startswith("/"):
            raise ValidationError("Leikmanna nafn (handle) má ekki byrja á '/'.")
        if " " in h:
            raise ValidationError("Leikmanna nafn (handle) má ekki innihalda bil.")
        if not any(ch.isalpha() for ch in h):
            raise ValidationError("Leikmanna nafn (handle) verður að innihalda a.m.k einn bókstaf.")
        return h
    
    def _normalize_website(self, website: str) -> str:
        """Adds https:// and checks if website ends correctly"""
        w = website.strip()
        if not w:
            return ""
        lower = w.lower()
        if not (lower.endswith(".com") or lower.endswith(".is") or lower.endswith(".tv")):
            raise ValidationError("Vefslóðin verður að enda á .is, .com eða .tv.")
        if not (lower.startswith("http://") or lower.startswith("https://")):
            w = "https://" + w
        return w
    
    def _validate_logo_value(self, logo: str) -> str:
        """Checks whether logo start with ASCII"""
        l = logo.strip()
        if not l:
            return ""
        if not l.startswith("ASCII_"):
            raise ValidationError("Logoið verður að byrja á 'ASCII_'.")
        return l

