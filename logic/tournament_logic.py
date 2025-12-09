from models.model_tournament import Tournament
from data.data_api import DataApi

class TournamentLogic:
    """Logic for accessing and managing tournament data."""
    def __init__(self, data_api: DataApi) -> None:
        """Initializes the logic class with refrence to the data API."""
        self._data_api = data_api
    
    def get_all_tournaments(self) -> list[Tournament]:
        """Retrieves a list of all tournaments from the data layer."""
        return self._data_api.read_all_tournaments()

    def get_tournament_name_list(self) -> list[str]:
        """Returns a list of tournament names."""
        tournaments = self.get_all_tournaments()
        return [tournament.name for tournament in tournaments]
    
    def get_tournament_by_index(self, index: int) -> Tournament:
        """Returns the tournament at the given index."""
        tournaments = self.get_all_tournaments()
        return tournaments[index]
    

