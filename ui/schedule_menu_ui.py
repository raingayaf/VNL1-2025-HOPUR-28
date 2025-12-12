from logic.LLApi import LLApi


# from ui.ui_controller import UIController

# gera "next day" taka sem sýnir næsta dag á schedule


class ScheduleUI:

    WIDTH = 60

    def __init__(self, logic_api):
        self._logic_api: LLApi = logic_api

    def displey_schedule_menu(self, tournament, schedule, day_to_show=1):
        """Display schedule to organizer"""

        print("*" * self.WIDTH)
        print("E-SPORTS".center(self.WIDTH))
        print("*" * self.WIDTH + "\n")
        print(f"{tournament.name}".center(self.WIDTH))
        print("Dagskrá".center(self.WIDTH) + "\n")
        print(
            f"Venue: {tournament.venue}\nStart: {tournament.start_date}\nEnd: {tournament.end_date}".center(
                self.WIDTH
            )
        )
        day_matches = [m for m in schedule if m["day"] == day_to_show]
        if day_matches:
            round_name = day_matches[0]["round"]
        else:
            round_name = "Óþekkt"
        print(f"Dagur: {day_to_show} | Riðill {round_name}".center(self.WIDTH))
        print()
        for match in day_matches:
            time = match["time"]
            team_a = match["team_a"]
            team_b = match["team_b"]
            line = f"{time}  | {(round_name)}  {team_a} vs {team_b}"
            print(line)
        print("\n" + "*" * self.WIDTH)
        print("b: Til baka, s: Vista dagskrá.")
    
    def display_user_schedule(self, tournament, schedule, day_to_show=1):
        """Display saved schedule to user schedule"""

        print("*" * self.WIDTH)
        print("E-SPORTS".center(self.WIDTH))
        print("*" * self.WIDTH + "\n")
        print(f"{tournament.name}".center(self.WIDTH))
        print("Dagskrá".center(self.WIDTH) + "\n")
        print(
            f"Venue: {tournament.venue}\nStart: {tournament.start_date}\nEnd: {tournament.end_date}".center(
                self.WIDTH
            )
        )

        if not schedule:
            print("Enginn vistuð dagskrá fyrir þetta mót".center(self.WIDTH))
            print("\n" + "*" * self.WIDTH)
            print("b: Til baka")
        
        day_matches = [m for m in schedule if m["day"] == day_to_show]
        print(f"Dagur {day_to_show}".center(self.WIDTH))
        print()
        for match in day_matches:
            time = match["time"]
            team_a = match["team_a"]
            team_b = match["team_b"]
            line = f"{time}  |  {team_a} vs {team_b}"
            print(line)
        print("\n" + "*" * self.WIDTH)
        print("b: Til baka")
        



