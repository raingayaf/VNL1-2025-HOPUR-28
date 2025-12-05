from models.excpetions import DataAccessError
from models.modelTeam import Team
import csv
import os

TEAM_CSV_PATH = "data/data_base/teams.csv"


class TeamData:
    """Read team CSV file and return list with team info"""

    def read_team_data(self):
        try:
            team_list: list[Team] = []
            if not os.path.exists(TEAM_CSV_PATH):
                return team_list

            with open(TEAM_CSV_PATH, mode="r", encoding="utf-8", newline="") as file:
                reader: csv.DictReader = csv.DictReader(file)
                for row in reader:
                    try:
                        team_id: int = int(row["id"])
                        team_name: str = row.get("team_name")
                        captain_handle: str = row.get("captain_handle")
                        website: str = row.get("website")
                        logo: str = row.get("logo")
                        team: Team = Team(
                            team_id, team_name, captain_handle, website, logo
                        )
                        team_list.append(team)
                    except (KeyError, ValueError) as KVerror:
                        print("fake print fall")
                        # TODO: senda í ui error message
            return team_list
        except OSError as exc:
            raise  # DataAccessError(f"ekki tókst að lesa skrána)

    def update_team_info(self, team_list: list[Team]) -> None:
        with open(TEAM_CSV_PATH, mode="w", encoding="utf-8", newline="") as file:
            fieldnames = [
                "team_id",
                "team_name",
                "captain_handle",
                "website",
                "logo",
            ]

            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for team in team_list:
                writer.writerow(
                    {
                        "team_id": team.team_id,
                        "team_name": team.team_name,
                        "captain_handle": team.captain_handle,
                        "website": team.website,
                        "logo": team.logo,
                    }
                )
