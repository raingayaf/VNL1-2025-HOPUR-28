import csv
import os
from models.exceptions import DataAccessError
from models.model_tournament import Tournament


class TournamentData:
    """Repository class for reading and writing tournaments.csv"""

    def __init__(self, file_path: str):
        # DataApi passes e.g. "data_base/tournaments.csv"
        self.file_path = file_path

    def read_all_tournaments(self) -> list[Tournament]:
        """Read tournament CSV file and return a list of Tournament objects."""
        tournaments: list[Tournament] = []

        if not os.path.exists(self.file_path):
            return tournaments

        try:
            with open(self.file_path, "r", encoding="utf-8", newline="") as file:
                reader: csv.DictReader = csv.DictReader(file)
                for row in reader:
                    try:
                        # CSV column is "tournament_id"
                        tournament_id: int = int(row["tournament_id"])
                        name: str = row.get("name", "")
                        venue: str = row.get("venue", "")
                        start_date: str = row.get("start_date", "")
                        end_date: str = row.get("end_date", "")
                        contact_name: str = row.get("contact_name", "")
                        contact_email: str = row.get("contact_email", "")
                        contact_phone: str = row.get("contact_phone", "")
                        max_servers_raw = row.get("max_servers", "") or "0"
                        max_servers: int = int(max_servers_raw)

                        tournament = Tournament(
                            tournament_id,
                            name,
                            venue,
                            start_date,
                            end_date,
                            contact_name,
                            contact_email,
                            contact_phone,
                            max_servers,
                        )
                        tournaments.append(tournament)
                    except (KeyError, ValueError):
                        # Skip invalid rows silently (no prints in data layer)
                        continue

            return tournaments

        except OSError as exc:
            raise DataAccessError(f"Ekki tókst að lesa skrá: {self.file_path}: {exc}")

    def write_all(self, tournaments: list[Tournament]) -> None:
        """Overwrite tournaments.csv with the given list of Tournament objects."""
        with open(self.file_path, mode="w", encoding="utf-8", newline="") as file:
            fieldnames = [
                "tournament_id",
                "name",
                "venue",
                "start_date",
                "end_date",
                "contact_name",
                "contact_email",
                "contact_phone",
                "max_servers",
            ]

            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for tournament in tournaments:
                writer.writerow(
                    {
                        # Here we assume your Tournament model stores this as .id_value
                        # or .tournament_id — adjust as needed:
                        "tournament_id": (
                            tournament.id_value
                            if hasattr(tournament, "id_value")
                            else tournament.tournament_id
                        ),
                        "name": tournament.name,
                        "venue": tournament.venue,
                        "start_date": tournament.start_date,
                        "end_date": tournament.end_date,
                        "contact_name": tournament.contact_name,
                        "contact_email": tournament.contact_email,
                        "contact_phone": tournament.contact_phone,
                        "max_servers": tournament.max_servers,
                    }
                )
