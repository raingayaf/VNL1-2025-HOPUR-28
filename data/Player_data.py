from datetime import date 
from models.modelPlayer import Player
import csv
import os

CVS_PATH = "data/data_base/players.csv"

class playerData:
    def read_player_data(self) -> list[Player]:
        """Read player CSV file and return a list with player info"""
        try:
            PlayerData: list[Player] = []
            if not os.path.exists(CVS_PATH):
                return PlayerData
            
            with open(CVS_PATH, mode ="r", encoding="utf-8", newline="") as file
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
                        Players: Player = Player(player_id, 
                                                  name, 
                                                  date_of_birth, 
                                                  address, phone, 
                                                  email, link, 
                                                  handle, 
                                                  team_name
                                                  )
                        PlayerData.append(Players)
                    except (KeyError, ValueError) as KVerror:
                        print("fake print fall")
                        #TODO: kalla í print fall sem segir error(KVerror)
            return PlayerData
        except OSError as exc:
            #TODO: raise error hér, þarf að gera exceptions í annari skrá.
                f"ekki tókst að lesa skrá {CVS_PATH}: {exc}"



