from typing import List
from data.tournament_data import TournamentData
from models.model_tournament import Tournament

class TournamentLogic:
    """Logic layer for tournaments."""
    def __init__(self, tournament_data: TournamentData | None = None):
        """ """
        self._tournament_data = tournament_data or TournamentData()
    
    def get_all_tournaments(self) -> list[Tournament]:
        """ """
        return self._tournament_data.ReadTournamentData()

    def get_tournament_name_list(self) -> list[str]:
        """ """
        tournaments = self.get_all_tournaments()
        return [t.name for t in tournaments]
    
    def get_tournament_by_index(self, index: int) -> Tournament:
        """ """
        tournaments = self.get_all_tournaments()
        if index < 0 or index >= len(tournaments):
            raise IndexError('Tournament index out of range.')
        return tournaments[index]
    

