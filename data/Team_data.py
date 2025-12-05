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
<<<<<<< HEAD
=======


# self.team_id = team_id
# self.team_name = team_name
# self.captain_handle = captain_handle
# self.website = website
# self.logo = logo
>>>>>>> 80ebbbeb2082cc8a33091c3ab239eb095a164d18
