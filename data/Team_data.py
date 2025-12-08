from models.exceptions import DataAccessError
from models.model_team import Team
import csv
import os


class TeamData:
    """Repository class for reading and writing teams.csv"""

    def __init__(self, file_path: str):
        # DataApi passes e.g. "data_base/teams.csv"
        self.file_path = file_path

    def read_all_teams(self) -> list[Team]:
        """Read team CSV file and return list of Team objects."""
        team_list: list[Team] = []

        if not os.path.exists(self.file_path):
            return team_list

        try:
            with open(self.file_path, mode="r", encoding="utf-8", newline="") as file:
                reader: csv.DictReader = csv.DictReader(file)
                for row in reader:
                    try:
                        team_id: int = int(row["team_id"])
                        team_name: str = row.get("team_name", "")
                        captain_handle: str = row.get("captain_handle", "")
                        website: str = row.get("website", "")
                        logo: str = row.get("logo", "")

                        team = Team(team_id, team_name, captain_handle, website, logo)
                        team_list.append(team)
                    except (KeyError, ValueError):
                        continue

            return team_list

        except OSError as exc:
            raise DataAccessError(f"Ekki tókst að lesa skrá: {self.file_path}: {exc}")

    def write_all(self, team_list: list[Team]) -> None:
        """Overwrite teams.csv with the given list of Team objects."""
        with open(self.file_path, mode="w", encoding="utf-8", newline="") as file:
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
