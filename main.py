from ui.main_menu_ui import MainMenuUI
from ui.input_handler import InputHandler
from ui.tournament_menu_ui import TournamentMenuUI
from ui.captain_menu_ui import CaptainMenuUI
from ui.organizer_menu_ui import OrganizerMenuUI

def main():
    main_menu_ui = MainMenuUI()
    input_handler = InputHandler()
    tournament_menu = TournamentMenuUI()
    captain_menu = CaptainMenuUI()
    organizer_menu = OrganizerMenuUI()

    while True:
        input_handler.clear_screen()
        main_menu_ui.display_main_menu()

        user_input = input_handler.get_menu_input(
            'Sláðu inn númer aðgerðar: ',
            {'1', '2', '3'}
        )

        if user_input is None:
            input('Ýttu á enter til að reyna aftur.')
            continue

        if user_input == '1':
            input_handler.clear_screen()
            tournament_menu.display_tournaments()
        elif user_input == '2':
            input_handler.clear_screen()
            captain_menu.display_captain_menu()
        elif user_input == '3':
            input_handler.clear_screen()
            organizer_menu.display_organizer_menu()


if __name__ == '__main__':
    main()






#from logic.LLApi import LogicApi

#def main():
#"""
#entry point for esports management system
#initializes logic layer, api ui handlers and main menu
#"""

# reperesents logic layer api implementation
#api = LogicApi()

# shared input handler
#input_handler = InputHandler()

# represents ui modules
#main_menu_ui = MainMenuUI(api, input_handler)
#team_menu_ui = TeamMenuUI(api, input_handler)
#tournament_ui = TournamentMenuUI(api, input_handler)

# submenus for UI
#main_menu_ui.team_menu_ui = team_menu_ui
#main_menu_ui.tournament_ui = tournament_ui 

#main_menu_ui.display_main_menu()


#if __name__ == "__main__": 
    #main()