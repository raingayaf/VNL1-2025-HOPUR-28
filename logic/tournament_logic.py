from models.model_tournament import Tournament
from data.data_api import DataApi


class TournamentLogic:
    """Logic layer for tournaments."""
    def __init__(self, data_api: DataApi):
        """ """
        self._data_api = data_api
    
    def get_all_tournaments(self) -> list[Tournament]:
        """ """
        return self._data_api.read_all_tournaments()

    def get_tournament_name_list(self) -> list[str]:
        """ """
        tournaments = self.get_all_tournaments()
        return [t.name for t in tournaments]
    
    def get_tournament_by_index(self, index: int) -> Tournament:
        """ """
        tournaments = self.get_all_tournaments()
        if index < 0 or index >= len(tournaments):
            raise IndexError('...')
        return tournaments[index]
    

