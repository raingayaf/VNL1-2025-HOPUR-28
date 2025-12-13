from logic.LLApi import LLApi

class ScheduleUI:
    """Create schedule for tournament"""

    WIDTH = 60

    def __init__(self, logic_api):
        self._logic_api: LLApi = logic_api

    def displey_schedule_menu(self, tournament, schedule, day_to_show=1, round_filter=None):
        """Display schedule for tournament"""

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
            try:
                match_day = int(m["day"])
            except (TypeError, ValueError): 
                continue
        
            if match_day != int(day_to_show):
                continue
            if round_filter is not None and m["round"] != round_filter:
                continue
            day_matches.append(m)
        
        if not day_matches:
            print()
            print(f"Engir leikir fundust fyrir dag {day_to_show}" + (f" ({round_filter})" if round_filter else "")  )
            return

        session_title = day_matches[0].get("session", "")
        round_title = round_filter if round_filter else day_matches[0]["round"]
        
        print(f"{session_title} | Riðill {round_title}".center(self.WIDTH))
        print()
        for match in day_matches:
            time = match["time"]
            team_a = match["team_a"]
            team_b = match["team_b"]
            line = f"{time}  | {(round_title)}  {team_a} vs {team_b}"
            print(line)
        print("\n" + "*" * self.WIDTH + "\n")

