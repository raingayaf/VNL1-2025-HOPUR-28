from logic.LLApi import LLApi

class ScheduleUI:

    WIDTH = 60

    def __init__(self, logic_api):
        self._logic_api: LLApi = logic_api

    def displey_schedule_menu(self, tournament, schedule, day_to_show=1, round_filter=None):
        """Display schedule to organizer"""

        print("*" * self.WIDTH)
        print("E-SPORTS".center(self.WIDTH))
        print("*" * self.WIDTH + "\n")
        print(f"{tournament.name}".center(self.WIDTH))
        print("Dagskrá".center(self.WIDTH) + "\n")
        print(f"Venue: {tournament.venue}")
        print(f"Start: {tournament.start_date}")
        print(f"End: {tournament.end_date}")
              
        day_matches = []
        for m in schedule:
            if m["day"] != day_to_show:
                continue
            if round_filter is not None and m["round"] != round_filter:
                continue
            day_matches.append(m)
        session_title = ""
        if day_matches:
            session_title = day_matches[0].get("session", "")
        round_title = round_filter if round_filter else ""
        print(f"{session_title} | Riðill {round_title}".center(self.WIDTH))
        print()
        for match in day_matches:
            time = match["time"]
            team_a = match["team_a"]
            team_b = match["team_b"]
            line = f"{time}  | {(round_title)}  {team_a} vs {team_b}"
            print(line)
        print("\n" + "*" * self.WIDTH + "\n")
    
    # def display_user_schedule(self, tournament, schedule, day_to_show=1):
    #     """Display saved schedule to user schedule"""

    #     print("*" * self.WIDTH)
    #     print("E-SPORTS".center(self.WIDTH))
    #     print("*" * self.WIDTH + "\n")
    #     print(f"{tournament.name}".center(self.WIDTH))
    #     print("Dagskrá".center(self.WIDTH) + "\n")
    #     print(
    #         f"Venue: {tournament.venue}\nStart: {tournament.start_date}\nEnd: {tournament.end_date}".center(
    #             self.WIDTH
    #         )
    #     )

    #     if not schedule:
    #         print("Enginn vistuð dagskrá fyrir þetta mót".center(self.WIDTH))
    #         print("\n" + "*" * self.WIDTH)
    #         print("b: Til baka")
        
    #     day_matches = [m for m in schedule if m["day"] == day_to_show]
    #     print(f"Dagur {day_to_show}".center(self.WIDTH))
    #     print()
    #     for match in day_matches:
    #         time = match["time"]
    #         team_a = match["team_a"]
    #         team_b = match["team_b"]
    #         line = f"{time}  |  {team_a} vs {team_b}"
    #         print(line)
    #     print("\n" + "*" * self.WIDTH)
    #     print("b: Til baka")
        



