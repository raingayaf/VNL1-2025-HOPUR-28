# TODO: þarf að fara yfir og laga
import csv
import os
from models.excpetions import DataAccessError
from models.modelTournament import Tournament

TOURNAMENT_CSV_PATH = "data/data_base/tournaments.csv"


class TournamentData:
    def ReadTournamentData(self) -> list[Tournament]:
        """Read tournament csv file and return a list with tournament data"""
        try:
            tournamentData: list[Tournament] = []
            if not os.path.exists("data/data_base/tournaments.csv"):
                return tournamentData

            with open(TOURNAMENT_CSV_PATH, "r", encoding="utf-8", newline="") as file:
                reader: csv.DictReader = csv.DictReader(file)
                for row in reader:
                    try:
                        id_value: int = int(row["tournament_id"])
                        name: str = row.get("name")
                        venue: str = row.get("venue")
                        start_date: str = row.get("start_date")
                        end_date: str = row.get("end_date")
                        contact_name: str = row.get("contact_name")
                        contact_email: str = row.get("contact_email")
                        contact_phone: str = row.get("contact_phone")
                        max_servers: int = row.get("max_servers")
                        tournament: Tournament = Tournament(
                            id_value,
                            name,
                            venue,
                            start_date,
                            end_date,
                            contact_name,
                            contact_email,
                            contact_phone,
                            max_servers,
                        )
                        tournamentData.append(tournament)
                    except (KeyError, ValueError) as KVerror:
                        print("Invalid row in csv: {row} ({KVerror})")
            return tournamentData
        except OSError as KVerror:
            raise DataAccessError(f"Ekki tókst að lesa skrá: {TOURNAMENT_CSV_PATH}")

    def update_tournament_data(self, tournamentData: list[Tournament]) -> None:
        with open(TOURNAMENT_CSV_PATH, mode="w", encoding="utf-8", newline="") as file:
            fieldnames = [
                "id_value",
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

            for tournament in tournamentData:
                writer.writerow(
                    {
                        "id_value": tournament.id_value,
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
