from data.data_api import DataApi
from models.model_player import Player
from models.exceptions import ValidationError

class PlayerLogic:
    """Handles all player related logic."""

    def __init__(self, data_api: DataApi) -> None:
        self._data_api = data_api

    #------------------METHODS-THAT-GET-DATA------------------------
    
    # ER ÞETTA NOTAÐ?
    def handle_exists(self, handle: str) -> bool:
        """Return True if player handle already exists."""
        players = self._data_api.read_all_players()
        return any(player.handle == handle for player in players)

    def get_players_for_team(self, team_name: str) -> list[Player]:
        """Retrives all players whose team name matches the given team."""
        players = self._data_api.read_all_players()
        return [player for player in players if player.team_name == team_name]

    def get_list_of_all_players(self, all_players: list):
        """Gets a list of all players on file"""
        all_players = self._data_api.read_all_players()
        return all_players

    #------------------METHODS-THAT-CHANGE-DATA----------------------
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
        """Creates a new player in system."""

        # Checks if player already exists
        players = self._data_api.read_all_players()
        if any(player.handle == handle for player in players):
            raise ValidationError("Leikmaður er nú þegar á skrá.")

        # Creates new player_id
        existing_player_nums = [int(player.player_id[1:]) for player in players]
        highest_num = max(existing_player_nums)

        new_id = f"P{highest_num + 1:03d}"

        #Creates a new player object
        new_player = Player(
            player_id = new_id,
            name = name,
            date_of_birth = date_of_birth,
            address = address,
            phone = phone,
            email = email,
            link = link,
            handle = handle,
            team_name = team_name,
        )

        players.append(new_player)
        self._data_api.save_all_players(players)

        return new_player
    
    def update_player(self, update_player: Player) -> None:
        """ """
        players = self._data_api.read_all_players()

        for index, player in enumerate(players):
            if player.player_id == update_player.player_id:
                players[index] = update_player
                self._data_api.save_all_players(players)
                return
        
        raise ValidationError("Leikmaður með þetta auðkenni fannst ekki.")
    
    
    
    