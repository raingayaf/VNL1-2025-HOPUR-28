import csv
from models.match import Match


class MatchesData:
    """Les og skrifar upplýsingar um matches úr matches.csv skránni"""
    def read_all(self, file_path: str) -> list[Match]:
        with open (file_path, mode = "r", encoding = "utf-8") as file:
            reader = csv.DictReader (file)
            matches: list[Match] = []
            for line in reader:
                match = Match(
                    match_id = int(line["match_id"]),
                    tournament_id = int(line["tournament_id"]),
                    match_number = int(line["match_number"]),
                    team_a_name = line["team_a_name"],
                    team_b_name = line["team_b_name"],
                    match_date = line["match_date"],
                    match_time = line["match_time"],
                    server_id = line["server_id"],
                    score_a = int(line["score_a"]),
                    score_b = int(line["score_b"]),
                    winner_team_name = line["winner_team_name"],
                    completed = line["completed"] == "TRUE"
                )
                matches.append(match)

            return matches

