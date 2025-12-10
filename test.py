from logic.LLApi import LLApi
from ui.schedule_menu_ui import ScheduleUI

if __name__ == "__main__":
    logic_api = LLApi()
    d_menu = ScheduleUI(logic_api)
    tournaments = logic_api.get_all_tournaments()
    teams = logic_api.get_all_teams()
    tournament = tournaments[0]
    d_menu.displey_schedule_menu(tournament, teams, day_to_show=1)
    # controller = UIController(data_api)