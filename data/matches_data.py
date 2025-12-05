import csv
from models.modelMatch import Match


class MatchesData:
    """Les og skrifar upplýsingar um matches úr matches.csv skránni"""

    def __init__(self, file_path: str):
        self.file_path = file_path

    def read_all(self) -> list[Match]:
        with open(self.file_path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            matches: list[Match] = []

            for line in reader:
                match = Match(
                    match_id = int(line["match_id"]),
                    tournament_id = int(line["tournament_id"]),
                    match_number = int(line["match_number"]),
                    team_name_a = line["team_name_a"],
                    team_name_b = line["team_name_b"],
                    match_date = line["match_date"],
                    match_time = line["match_time"],
                    server_id = line["server_id"],
                    score_a = int(line["score_a"]),
                    score_b = int(line["score_b"]),
                    winner_team_name = line["winner_team_name"],
                    completed = line["completed"] == "TRUE",
                )
                matches.append(match)

            return matches

    def write_all(self, matches: list[Match]) -> None:
        with open(self.file_path, "w", newline = "", encoding = "utf-8") as file:
            fieldnames = [
                "match_id",
                "tournament_id",
                "match_number",
                "team_a_name",
                "team_b_name",
                "match_date",
                "match_time",
                "server_id",
                "score_a",
                "score_b",
                "winner_team_name",
                "completed",
            ]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for match in matches:
                writer.writerow({
                    "match_id": match.match_id,
                    "tournament_id": match.tournament_id,
                    "match_number": match.match_number,
                    "team_name_a": match.team_name_a,
                    "team_name_b": match.team_name_b,
                    "match_date": match.match_date,
                    "match_time": match.match_time,
                    "server_id": match.server_id,
                    "score_a": match.score_a,
                    "score_b": match.score_b,
                    "winner_team_name": match.winner_team_name,
                    "completed": "TRUE" if match.completed else "FALSE",
                })

