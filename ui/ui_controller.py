# UI imports
from ui.main_menu_ui import MainMenuUI
from ui.tournament_menu_ui import TournamentMenuUI
from ui.captain_menu_ui import CaptainMenuUI
from ui.organizer_menu_ui import OrganizerMenuUI
from ui.input_handler import InputHandler
from ui import messages

# Data layer
from logic.LLApi import LLApi

# Models
from models.model_tournament import Tournament
from models.model_team import Team
from models.model_player import Player

class UIController:
    """Manages navigation between UI screens based on user selection."""
    
    def __init__(self) -> None:
        """Initializes UI menus, input handling, data API and logic layers."""
        # UI menus
        self.main_menu = MainMenuUI()
        self.tournament_menu = TournamentMenuUI()
        self.captain_menu = CaptainMenuUI()
        self.organizer_menu = OrganizerMenuUI()

        # Input handling
        self.input_handler = InputHandler()

        # Logic layer
        self.logic_api = LLApi()

    #-----------------------------MAIN-MENU-------------------------------
    def run_main_menu(self) -> None:
        """Runs the main menu and routes the user based on their selection."""
        in_main_menu = True
        error_message = None

        while in_main_menu:
            self.input_handler.clear_screen()
            
            # Show error message from previous iteration
            if error_message is not None:
                print('\n' + error_message.center(self.input_handler.WIDTH) + '\n')
                error_message = None

            # Show menu and handle user selection
            self.main_menu.display_main_menu()
            user_input = self.input_handler.get_user_input(
                messages.MENU_PROMPT,
                {'1', '2', '3', 'q'}
            )
            # Routes user to chosen submenu or closes program
            if user_input == '1':
                has_tournaments = self.run_tournaments_menu()
                if not has_tournaments:
                    # Generates error message that is shown before next iteration
                    error_message = messages.NO_TOURNAMENTS
            elif user_input == '2':
                self.run_captain_menu()
            elif user_input == '3':
                self.input_handler.clear_screen()
                self.organizer_menu.display_organizer_menu()
            elif user_input == 'q':
                in_main_menu = False

    #----------------------------GENERAL-USER-MENUS-------------------------
    def run_tournaments_menu(self) -> bool:
        """Runs the tournaments menu and routes the user based on their selection.
        Returns False if no tournament exists.
        """
        # Get all tournaments in system
        tournament_names = self.logic_api.get_tournament_name_list()
        # If none, user goes back to main menu and error message is shown
        if not tournament_names:
            return False
        
        in_tournament_menu = True

        # Show menu with tournaments and handle user selection
        while in_tournament_menu:
            self.input_handler.clear_screen()
            self.tournament_menu.display_tournaments(tournament_names)
            # Valid options, each tournament number and b to go back
            valid_input = {str(i) for i in range(1, len(tournament_names) + 1)} | {'b'}
            user_input = self.input_handler.get_user_input(
                messages.TOURNAMENT_SELECTION_PROMPT,
                valid_input
            )
            if user_input == 'b':
                # Return to main menu
                in_tournament_menu = False
            else:
                # Open options for selected tournament
                index = int(user_input) - 1
                selected_tournament = self.logic_api.get_tournament_by_index(index)
                self.run_tournament_options(selected_tournament)

        return True

    def run_tournament_options(self, tournament: Tournament) -> None:
        """Runs the options menu for chosen tournament and routes the user based on their selection."""
        in_tournament_options = True

        # Show tournament options and handle user selection
        while in_tournament_options:
            self.input_handler.clear_screen()
            self.tournament_menu.display_tournament_menu(tournament.name)
            user_input = self.input_handler.get_user_input(
                messages.ACTION_OR_BACK_PROMPT,
                {'1', '2', '3', 'b'}
            )
            # Routes user to chosen submenu 
            if user_input == '1':
                self.run_tournament_schedule(tournament)
            elif user_input == '2':
                self.run_tournament_scoreboard(tournament)
            elif user_input == '3':
                self.run_tournament_teams(tournament)
            elif user_input == 'b':
                # Return to the previous menu
                in_tournament_options = False    

    def run_tournament_schedule(self, tournament: Tournament) -> None:
        """Displays the tournament schedule until the user chooses to return to the previous menu."""
        in_tournament_schedule = True

        while in_tournament_schedule:
            self.input_handler.clear_screen()
            self.tournament_menu.display_tournament_schedule(tournament.name)
            user_input = self.input_handler.get_user_input(
                messages.BACK_PROMPT,
                {'b'}
            )
            if user_input == 'b':
                # Return to the previous menu
                in_tournament_schedule = False

    def run_tournament_scoreboard(self, tournament: Tournament) -> None:
        """Displays the tournament scoreboard until the user chooses to return to the previous menu."""
        in_tournament_scoreboard = True

        while in_tournament_scoreboard:
            self.input_handler.clear_screen()
            self.tournament_menu.display_tournament_scoreboard(tournament.name)
            user_input = self.input_handler.get_user_input(
                messages.BACK_PROMPT,
                {'b'}
            )
            if user_input == 'b':
                # Return to the previous menu
                in_tournament_scoreboard = False

    def run_tournament_teams(self, tournament: Tournament) -> None:
        """Displays the teams in the chosen tournament and routes the user based on their selection."""
        in_tournament_teams = True
        # Show tournament teams and handle user selection
        while in_tournament_teams:
            teams = self.logic_api.get_teams_for_tournament(tournament.tournament_id)
            self.input_handler.clear_screen()
            self.tournament_menu.display_tournament_teams(tournament.name, teams)
            valid_input = {str(i) for i in range(1, len(teams) + 1)} | {'b'}
            user_input = self.input_handler.get_user_input(
                messages.TEAM_SELECTION_PROMPT,
                valid_input
            )
            if user_input == 'b':
                # Return to the previous menu
                in_tournament_teams = False
            else:
                # Open the player list for the selected team
                index = int(user_input) - 1
                selected_team: Team = teams[index]
                self.run_tournament_team_players(tournament, selected_team)

    def run_tournament_team_players(self, tournament: Tournament, team: Team) -> None:
        """Displays the players in chosen team until user chooses to return to the previous menu."""
        in_team_players_menu = True

        while in_team_players_menu:
            players: list[Player] = self.logic_api.get_players_for_team(team.team_name)
            self.input_handler.clear_screen()
            self.tournament_menu.display_team_players(tournament.name, team.team_name, players)
            user_input = self.input_handler.get_user_input(
                messages.BACK_PROMPT,
                {'b'}
            )
            if user_input == 'b':
                # Return to the previous menu
                in_team_players_menu = False

    #------------------------CAPTAIN-MENU-FLOW------------------------------            
    def run_captain_menu(self):
        """Runs the captain menu and routes the user based on their selection."""
        in_captain_menu = True
        while in_captain_menu:
            self.input_handler.clear_screen()
            self.captain_menu.display_captain_menu()
            captain_input = self.input_handler.get_user_input(
                messages.ACTION_OR_BACK_PROMPT,
                {'1', '2', 'b'}
            )
            if captain_input == '1':
                self.team_registration()
            elif captain_input == '2':
                self.run_captain_verification()
            elif captain_input == 'b':
                in_captain_menu = False
    
    def team_registration(self):
        """Run the team registratiom for a team captain."""
        self.input_handler.clear_screen()
        self.captain_menu.display_team_registration_menu()
        #team_id?
        team_name = self.input_handler.get_non_empty_string('Skráðu heiti liðsins: ')
        captain_handle = self.input_handler.get_non_empty_string('Skráðu leikmanna nafn fyrirliðans: ')
        number_of_players = self.input_handler.get_int('Skráðu fjölda leikmanna: ', 3, 5)
        #team_website?
        #team_logo?
        # TODO: Senda í logic/data layer
        self.run_player_registration(team_name, number_of_players)
    
    def run_player_registration(self, team_name: str, number_of_players: int):
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


    def run_captain_verification(self):
        """  """
        self.input_handler.clear_screen()
        self.captain_menu.display_captain_verification_menu()

        team_name = self.input_handler.get_non_empty_string('Sláðu inn heiti á liðinu þínu: ')
        captain_handle = self.input_handler.get_non_empty_string('Sláðu inn leikmanna nafn þitt: ')
        # TODO: kalla á logic/data layer til að staðfesta að fyrirliði tilheyri þessu liði
        
        # dæmi!
        players = ['Leikmaður 1', 'Leikmaður 2', 'Leikmaður 3']

        self.run_team_information(team_name, players)


    def run_team_information(self, team_name: str, players: list[str]):
        """  """
        in_team_info = True

        while in_team_info:
            self.input_handler.clear_screen()
            self.captain_menu.display_team_information_menu(team_name)
            # TODO: Falleg tafla yfir leikmenn liðs

            user_input = self.input_handler.get_user_input(
                'Sláðu inn númer aðgerðar: ',
                {'1', 'h'}
            )

            if user_input == '1':
                self.run_player_indformation_selection(team_name, players)
            
            elif user_input == 'b':
                in_team_info = False


    def run_player_indformation_selection(self, team_name: str, players: list[str]):
        """  """
        pass


    def run_player_information(self):
        """  """
        pass

#-----------------------ORGANIZER-MENU-FLOW------------------------------

    def orginizer_menu_flow(self):
        """Operations for displaying orginizer menu"""
        in_orginizer_menu = True

        while in_orginizer_menu:
            self.input_handler.clear_screen()
            self.organizer_menu.display_organizer_menu()
            
            user_input = self.input_handler.get_user_input(
                'Sláðu inn númer aðgerðar: ',
                {'1', '2', '3', 'b'})
            
            if user_input == '1':
                self.organizer_menu.display_tournament_creation()
                tournament_name = self.input_handler.get_non_empty_string("Sláðu inn nafn móts:")
                tournament_start_date = self.input_handler.get_non_empty_string("Sláðu inn upphafsdagsetningu:")
                tournament_end_date = self.input_handler.get_non_empty_string("Sláðu inn endadagsetningu:")
                tournament_venue = self.input_handler.get_non_empty_string("Sláðu inn staðsetningu:")
                tournament_contact_name = self.input_handler.get_non_empty_string("Sláðu inn nafn tengiliðs:")
                tournament_contact_email = self.input_handler.get_non_empty_string("Sláðu inn netfang tengiliðs: ")
                tournament_contact_phone = self.input_handler.get_non_empty_string("Sláðu inn símanúmer tengiliðs:")
                
                max_servers = 3

            #try:
                #new_tournament = 