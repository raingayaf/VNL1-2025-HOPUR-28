from logic.LLApi import LLApi
from logic.schedule_logic import Schedule


class ScheduleUI:

    WIDTH = 60

    def __init__(self, data_api):
        self._schedule_logic = Schedule(data_api)

    def displey_schedule_menu(self, tournament: str, teams: list[str]):
        """Display schedule to anyone"""

        schedule = self._schedule_logic.generate_schedule(tournament, teams)

        print("*" * self.WIDTH)
        print("E-SPORTS".center(self.WIDTH))
        print("*" * self.WIDTH + "\n")
        print("Mótsdagskrá dagur 1".center(self.WIDTH) + "\n")
        print(
            f"{tournament.venue} {tournament.start_date} {tournament.end_date} {tournament.name}".center(
                self.WIDTH
            )
        )
        print()

        current_day = None
        for match in schedule:
            day = match["day"]
            time = match["time"]
            team_a = match["team_a"]
            team_b = match["team_b"]
            #
            if day != current_day:
                current_day = day
                print()
                print(f"Dagur {day}".center(self.WIDTH))
                print("-" * self.WIDTH)

            line = f"{time}  |  {team_a} vs {team_b}"
            print(line.center(self.WIDTH))

        print("*" * self.WIDTH)
        input("Q: Til baka: ")


if __name__ == "__main__":
    data_api = LLApi()

    d_menu = ScheduleUI(data_api)

    tournaments = data_api.get_all_tournaments()
    teams = data_api.get_team_details()

    tournament = tournaments[0]

    d_menu.displey_schedule_menu(tournament, teams)
