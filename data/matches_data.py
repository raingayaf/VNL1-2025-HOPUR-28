import csv

class MatchesData:
    def read_all(self) -> list[matches]:
        with open ("matches.csv", mode = "r", encoding = "utf-8") as file:
            reader: csv.DictReader (file)
            for line in reader:
                match_data: str = line.get("match_id", "")
                match_data: str = line.get("tournament_id", "")
                match_data: str = line.get("round", "")
                match_data: str = line.get("match_number", "")
                match_data: str = line.get("team_a_name", "")
                match_data: str = line.get("team_b_name", "")
                match_data: str = line.get("match_date", "")
                match_data: str = line.get("match_time", "")
                match_data: str = line.get("server_id", "")
                match_data: str = line.get("score_a", "")
                match_data: str = line.get("score_b", "")
                match_data: str = line.get("winner_team_name", "")
                match_data: str = line.get("completed", "")


