import csv
from models.modelMatch import Match


class MatchesData:
    """Reads and writes match information into matches.csv"""
    #(Henda fyrir skil) Þessi klasi er bara að .csv read/write. Hann fær
    #.csv slóðina sína frá DataApi, í línu 20 og 21. Þetta er það sem er kallað
    #repo eða repository class. 

    def __init__(self, file_path: str):
        self.file_path = file_path

#    (Henda fyrir skil)  Flæði:
#         DataApi.read_all_matches() 
#             kallar á read_all() 
#                 read_all() opnar .csv 
#                 breytir öllum röðum í skránni í Match model   
#                 skilar lista [Match] inn á logic Layer

    def read_all(self) -> list[Match]:
        with open(self.file_path, mode = "r", encoding = "utf-8") as file:
            #Dictreader skilar dict úr skránni, sem notar header línuna (sumsé efstu línu)
            #sem keys fyrir öll values sem eru skilgreind hérna aðeins neðar.
            reader = csv.DictReader(file)

            #matches er listinn sem heldur utan um tilbúin Match objects.
            matches: list[Match] = []

            for line in reader:
                match = Match(
                    match_id = int(line["match_id"]),
                    tournament_id = int(line["tournament_id"]),
                    match_number = int(line["match_number"]),
                    round = line["round"],
                    team_a_name = line["team_a_name"],
                    team_b_name = line["team_b_name"],
                    match_date = line["match_date"],
                    match_time = line["match_time"],
                    server_id = line["server_id"],
                    score_a = int(line["score_a"]),
                    score_b = int(line["score_b"]),
                    winner_team_name = line["winner_team_name"],
                    completed = line["completed"] == "TRUE",
                )
                matches.append(match) #Hérna bætum við Match objects sem eru til
                #á skránni fyrir, inn á tóma listan á línu 28.
        
            return matches
#write_all á að yfirskrifa allt, og það er í lagi því við erum að lesa skránna fyrst
#append nýjum match object og svo skrifa hana í heild sinni. Nýjum matches úr kerfi er bætt inn
#með data api ef kerfið kallar á hann: write_all(matches) á línu 41. 

    def write_all(self, matches: list[Match]) -> None:
        with open(self.file_path, "w", newline = "", encoding = "utf-8") as file:
            fieldnames = [
                "match_id",
                "tournament_id",
                "match_number",
                "round",
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

            writer = csv.DictWriter(file, fieldnames = fieldnames)
            writer.writeheader() #Skrifar header í .Csv skránna

            for match in matches:
                writer.writerow(
                    {
                        "match_id": match.match_id,
                        "tournament_id": match.tournament_id,
                        "match_number": match.match_number,
                        "round": match.round,
                        "team_a_name": match.team_a_name,
                        "team_b_name": match.team_b_name,
                        "match_date": match.match_date,
                        "match_time": match.match_time,
                        "server_id": match.server_id,
                        "score_a": match.score_a,
                        "score_b": match.score_b,
                        "winner_team_name": match.winner_team_name,
                        "completed": "TRUE" if match.completed else "FALSE",
                    }
                )
