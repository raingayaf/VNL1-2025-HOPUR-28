from models.excpetions import DataAccessError
from datetime import date
from models.modelPlayer import Player
import csv
import os

PLAYER_CSV_PATH = "data/data_base/players.csv"


class playerData:
    def read_player_data(self) -> list[Player]:
        """Read player CSV file and return a list with player info"""
        try:
            PlayerData: list[Player] = []
            if not os.path.exists(PLAYER_CSV_PATH):
                return PlayerData

            with open(PLAYER_CSV_PATH, mode="r", encoding="utf-8", newline="") as file:
                reader: csv.DictReader = csv.DictReader(file)
                for row in reader:
                    try:
                        player_id: int = int(row["id"])
                        name: str = row.get("name")
                        date_of_birth: date = row.get("date_of_birth")
                        address: str = row.get("address")
                        phone: str = row.get("phone")
                        email: str = row.get("email")
                        link: str = row.get("link")
                        handle: str = row.get("handle")
                        team_name: str = row.get("team_name")
                        Players: Player = Player(
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
                        PlayerData.append(Players)
                    except (KeyError, ValueError) as KVerror:
                        print("fake print fall")
                        # TODO: kalla í print í UI fall sem segir error(KVerror)
            return PlayerData
        except OSError as exc:
            raise DataAccessError(f"ekki tókst að lesa skrá {PLAYER_CSV_PATH}: {exc}")
            # TODO: mögulega gera print skipun í UI til að framkalla þessi skilaboð.

    def update_player_info(self, PlayerData: list[Player]) -> None:
        with open(PLAYER_CSV_PATH, mode="w", encoding="utf-8", newline="") as file:
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

            for player in PlayerData:
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
