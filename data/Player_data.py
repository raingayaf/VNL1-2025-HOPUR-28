from models.exceptions import DataAccessError
from datetime import date
from models.modelPlayer import Player
import csv
import os


class playerData:
    """Repository class for reading and writing players.csv"""

    def __init__(self, file_path: str):
        # DataApi passes in e.g. "data_base/players.csv"
        self.file_path = file_path

    def read_all(self) -> list[Player]:
        """Read player CSV file and return a list of Player objects."""
        try:
            players: list[Player] = []

            if not os.path.exists(self.file_path):
                # No file yet = no players
                return players

            with open(self.file_path, mode="r", encoding="utf-8", newline="") as file:
                reader: csv.DictReader = csv.DictReader(file)
                for row in reader:
                    try:
                        player_id: int = int(row["player_id"])
                        name: str = row.get("name", "")
                        date_of_birth: str = row.get("date_of_birth", "")
                        address: str = row.get("address", "")
                        phone: str = row.get("phone", "")
                        email: str = row.get("email", "")
                        link: str = row.get("link", "")
                        handle: str = row.get("handle", "")
                        team_name: str = row.get("team_name", "")

                        player = Player(
                            player_id,
                            name,
                            date_of_birth,
                            address,
                            phone,
                            email,
                            link,
                            handle,
                            team_name,
                        )
                        players.append(player)
                    except (KeyError, ValueError):
                        # Here you'd normally log or propagate, but don't print in data layer
                        # For now we just skip bad rows
                        continue

            return players

        except OSError as exc:
            raise DataAccessError(f"ekki tókst að lesa skrá {self.file_path}: {exc}")

    def write_all(self, players: list[Player]) -> None:
        """Overwrite players.csv with the given list of Player objects."""
        with open(self.file_path, mode="w", encoding="utf-8", newline="") as file:
            fieldnames = [
                "player_id",
                "name",
                "date_of_birth",
                "address",
                "phone",
                "email",
                "link",
                "handle",
                "team_name",
            ]

            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for player in players:
                writer.writerow(
                    {
                        "player_id": player.player_id,
                        "name": player.name,
                        "date_of_birth": player.date_of_birth,
                        "address": player.address,
                        "phone": player.phone,
                        "email": player.email,
                        "link": player.link,
                        "handle": player.handle,
                        "team_name": player.team_name,
                    }
                )
