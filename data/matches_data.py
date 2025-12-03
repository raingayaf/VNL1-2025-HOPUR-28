import csv

class MatchesData:
    def read_all(self) -> list[matches]:
        with open ("matches.csv", mode = "r", encoding = "utf-8") as file:
            reader: csv.DictReader (file)
            for line in reader:
                menu_data: str = line.get("date", "")
                menu_data: str = line.get("date", "")
                menu_data: str = line.get("date", "")


