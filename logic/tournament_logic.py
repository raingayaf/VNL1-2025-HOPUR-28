from models.model_tournament import Tournament
from data.data_api import DataApi
from models.exceptions import ValidationError

class TournamentLogic:
    """Logic for accessing and managing tournament data."""
    def __init__(self, data_api: DataApi) -> None:
        """Initializes the logic class with refrence to the data API."""
        self._data_api = data_api

    def get_all_tournaments(self) -> list[Tournament]:
        """Gets a list of all tournaments,
        Retrieves a list of all tournaments from the data layer."""
        return self._data_api.read_all_tournaments()

    def get_tournament_name_list(self) -> list[str]:
        """Returns a list of tournament names."""
        tournaments = self.get_all_tournaments()
        return [tournament.name for tournament in tournaments]

    def get_tournament_by_index(self, index: int) -> Tournament:
        """Returns the tournament at the given index."""
        tournaments = self.get_all_tournaments()
        return tournaments[index]

    def create_tournament(self, 
                name: str, venue: str, 
                start_date: str, 
                end_date: str, 
                contact_name: str, 
                contact_email: str, 
                contact_phone: str,
                max_servers: int) -> Tournament:

        tournaments = self._data_api.read_all_tournaments()

        if any(t.name == name for t in tournaments):
            raise ValidationError(f'Mótið {name} er nú þegar á skrá')
        #Assigns new id to tournament
        existing_ids = [t.tournament_id for t in tournaments]
        new_id = max(existing_ids) + 1 if existing_ids else 1

        #Creates new tournament object
        new_tournament = Tournament(
        tournament_id = new_id,
        name = name,
        venue = venue,
        start_date = start_date,
        end_date = end_date,
        contact_name = contact_name,
        contact_email = contact_email,
        contact_phone = contact_phone,
        max_servers = max_servers)

        tournaments.append(new_tournament)
        self._data_api.save_all_tournaments(tournaments)

        return new_tournament 