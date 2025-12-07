from ui.main_menu_ui import MainMenuUI
from ui.tournament_menu_ui import TournamentMenuUI
from ui.captain_menu_ui import CaptainMenuUI
from ui.organizer_menu_ui import OrganizerMenuUI
from ui.input_handler import InputHandler

class UIController:
    """Handles all UI flow and navigation between menu screens."""
    def __init__(self):
        self.main_menu = MainMenuUI()
        self.tournament_menu = TournamentMenuUI()
        self.captain_menu = CaptainMenuUI()
        self.organizer_menu = OrganizerMenuUI()
        self.input_handler = InputHandler()
    
    def run(self):
        """  """
        running = True
        while running:
            self.input_handler.clear_screen()
            self.main_menu.display_main_menu()
            user_input = self.input_handler.get_menu_input(
                'Sláðu inn númer aðgerðar: ',
                {'1', '2', '3', 'q'}
            )
            if user_input is None:
                input('Ýttu á enter til að reyna aftur.')
                continue
            if user_input == '1':
                self.input_handler.clear_screen()
                self.tournament_menu.display_tournaments()
            elif user_input == '2':
                self.input_handler.clear_screen()
                self.captain_menu_flow()
            elif user_input == '3':
                self.input_handler.clear_screen()
                self.organizer_menu.display_organizer_menu()
            elif user_input == 'q':
                running = False

    #-----------------------GENERAL-USER-MENU-FLOW-------------------------
    def tournaments_flow(self):
        """  """
        pass

    def tournament_options_flow(self):
        """  """
        pass

    def tournament_schedule_flow(self):
        """  """
        pass

    def tournament_scoreboard_flow(self):
        """  """
        pass

    def tournament_teams_flow(self):
        """  """
        pass

    def tournament_team_players_flow(self):
        """  """
        pass


    #------------------------CAPTAIN-MENU-FLOW------------------------------            

    def captain_menu_flow(self):
        """  """
        in_captain_menu = True
        while in_captain_menu:
            self.input_handler.clear_screen()
            self.captain_menu.display_captain_menu()
            captain_input = self.input_handler.get_menu_input(
                'Sláðu inn númer aðgerðar: ',
                {'1', '2', 'b'}
            )
            if captain_input == '1':
                self.team_registration_flow()
            elif captain_input == '2':
                self.captain_verification_flow()
            elif captain_input == 'b':
                in_captain_menu = False
    
    def team_registration_flow(self):
        """  """
        self.input_handler.clear_screen()
        self.captain_menu.display_team_registration_menu()
        #team_id?
        team_name = self.input_handler.get_non_empty_string('Skráðu heiti liðsins: ')
        captain_handle = self.input_handler.get_non_empty_string('Skráðu leikmanna nafn fyrirliðans: ')
        number_of_players = self.input_handler.get_int('Skráðu fjölda leikmanna: ', 3, 5)
        #team_website?
        #team_logo?
        # TODO: Senda í logic/data layer
        self.player_registration_flow(team_name, number_of_players)
    
    def player_registration_flow(self, team_name: str, number_of_players: int):
        """  """
        players = []

        for i in range(1, number_of_players + 1):
            self.input_handler.clear_screen()
            self.captain_menu.display_player_registration_menu(team_name, i)

            #player_id --> Það er player_id í database...
            player_name = self.input_handler.get_non_empty_string('Skráðu fullt nafn: ')
            player_date_of_birth = self.input_handler.get_non_empty_string('Skráðu fæðingardag og ár: ')
            player_address = self.input_handler.get_non_empty_string('Skráðu heimilisfang: ')
            player_phone = self.input_handler.get_non_empty_string('Skráðu símanúmer: ')
            player_email = self.input_handler.get_non_empty_string('Skráðu netfang: ')
            player_link = self.input_handler.get_non_empty_string('Skráðu vefslóð: ')
            player_handle = self.input_handler.get_non_empty_string('Skráðu leikmanna nafn: ')
            #player_team_name --> Það er team_name í database...
        
        player_data = {
            'name': player_name,
            'date_of_birth': player_date_of_birth,
            'address': player_address,
            'phone': player_phone,
            'email': player_email,
            'link': player_link,
            'handle': player_handle
        }
        players.append(player_data)    
    # TODO: senda (team_name, players) í logic/data layer


    def captain_verification_flow(self):
        """  """
        self.input_handler.clear_screen()
        self.captain_menu.display_captain_verification_menu()

        team_name = self.input_handler.get_non_empty_string('Sláðu inn heiti á liðinu þínu: ')
        captain_handle = self.input_handler.get_non_empty_string('Sláðu inn leikmanna nafn þitt: ')
        # TODO: kalla á logic/data layer til að staðfesta að fyrirliði tilheyri þessu liði
        
        # dæmi!
        players = ['Leikmaður 1', 'Leikmaður 2', 'Leikmaður 3']

        self.team_information_flow(team_name, players)


    def team_information_flow(self, team_name: str, players: list[str]):
        """  """
        in_team_info = True

        while in_team_info:
            self.input_handler.clear_screen()
            self.captain_menu.display_team_information_menu(team_name)
            # TODO: Falleg tafla yfir leikmenn liðs

            user_input = self.input_handler.get_menu_input(
                'Sláðu inn númer aðgerðar: ',
                {'1', 'h'}
            )

            if user_input == '1':
                self.select_player_flow(team_name, players)
            
            elif user_input == 'b':
                in_team_info = False


    def select_player_flow(self, team_name: str, players: list[str]):
        """  """
        pass


    def player_information_flow(self):
        """  """
        pass

#-----------------------ORGANIZER-MENU-FLOW------------------------------