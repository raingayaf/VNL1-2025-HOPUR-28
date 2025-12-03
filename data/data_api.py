from matches_data import MatchesData

class DataApi:
    def __init__(self, matches_data: MatchesData):
        self.matches_data = matches_data 

    def read_all_matches(self) -> list[Matches]:
        return self.matches_data.read_all()
    
    # TODO save_menu?

