from ui.main_menu_ui import MainMenuUI
from ui.team_menu_ui import TeamMenuUI
from ui.captain_menu_ui import CaptainMenuUI
from ui.organizer_menu_ui import OrganizerMenuUI
from ui.tournament_menu_ui import TournamentMenuUI
from ui.input_handler import InputHandler

from logic.LLApi import LogicApi

def main():
    """
    entry point for esports management system
    initializes logic layer, api ui handlers and main menu
    """

# reperesents logic layer api implementation
api = LogicApi()

# shared input handler
input_handler = InputHandler()

# represents ui modules
main_menu_ui = MainMenuUI(api, input_handler)
team_menu_ui = TeamMenuUI(api, input_handler)
tournament_ui = TournamentMenuUI(api, input_handler)

# submenus for UI
main_menu_ui.team_menu_ui = team_menu_ui
main_menu_ui.tournament_ui = tournament_ui 

main_menu_ui.display_main_menu()


#if __name__ == "__main__": 
    #main()