# TODO: þarf að fara yfir og laga
import csv
import os

# from data_api import DataApi
from models.match import Tournaments


class TournamentData:
    def ReadTournamentData(self) -> list[Tournaments]:
        """Read tournament csv file and return a list with tournament data"""
        try:
            tournamentData: list[Tournaments] = []
            if not os.path.exists("data/data_base/tournaments.csv"):
                return tournamentData

            with open(
                "data/data_base/tournaments.csv", "r", encoding="utf-8", newline=""
            ) as file:
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
                        tournament: Tournaments = Tournaments(
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
            # TODO: Her vantar mögulega raise "DataAccessError"
            f"Tókst ekki að lesa skrána"
