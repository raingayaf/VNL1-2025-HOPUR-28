import csv

class MenuData:
    def read_all(self) -> list(menu):
        with open (DATA_PATH, mode = "r", encoding = "utf-8") as file:
            reader: csv.DictReader (file)
            for line in reader:
                menu_data: str = line.get("date", "")
                menu_data: str = line.get("date", "")
                menu_data: str = line.get("date", "")


