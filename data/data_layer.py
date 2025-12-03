class DataLayer:
    # TODO: create DataApi

    def __init__(self):
        pass

    def __str__(self):
        pass

    def ReadAll(self):
        filename = "data/matches.csv"
        try:
            with open(filename, "r", encoding="utf-8") as file:
                data = file.read
        except FileNotFoundError:
            print("file not found, please try again")

    def TournamentData(self):
        pass

    def TeamData(self):
        pass

    def MatchData(self):
        pass

    def PlayerData(self):
        pass
