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
from models.exceptions import ValidationError

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
                self.orginizer_menu_flow()
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
                self.run_team_registration()
            elif captain_input == '2':
                self.run_captain_verification()
            elif captain_input == 'b':
                in_captain_menu = False
    
    def run_team_registration(self) -> None:
        """Run the team registratiom for a team captain."""
        in_team_registration = True
        step = 1

        team_name = ''
        captain_handle = ''
        number_of_players = 0
        team_website = ''
        team_logo = ''
        player_handles: list[str] = [] 

        while in_team_registration:
            self.input_handler.clear_screen()
            self.captain_menu.display_team_registration_menu()

            # Show all already entered values as context
            if team_name:
                print(f'Skráðu heiti liðsins: {team_name}')
            if captain_handle:
                print(f'Skráðu leikmanna nafn fyrirliðans: {captain_handle}')
            if number_of_players:
                print(f'Skráðu fjölda leikmanna (3-5): {number_of_players}')
            if team_website or team_logo:
                print('Valkvæðar upplýsingar um lið:')
                print(f'Vefslóð liðsins: {team_website or ''}')
                print(f'Vefslóð liðsins: {team_logo or ''}')

            # Step 1 - Team name
            if step == 1:
                user_input = self.input_handler.get_input_with_nav('Skráðu heiti liðsins: ')
                if user_input == 'QUIT':
                    in_team_registration = False
                    continue
                if user_input == 'BACK':
                    in_team_registration = False
                    continue
                if self.logic_api.team_name_exists(user_input):
                    print(f"Liðið '{user_input}' er nú þegar á skrá.")
                    input('Ýttu á ENTER til að reyna aftur.')
                    continue
                team_name = user_input
                step = 2
                continue

            # Step 2 - Captain handle
            if step == 2:
                user_input = self.input_handler.get_input_with_nav('Skráðu leikmanna nafn fyrirliðans: ')
                if user_input == 'QUIT':
                    in_team_registration = False
                    continue
                if user_input == 'BACK':
                    team_name = ''
                    step = 1
                    continue
                if self.logic_api.handle_exists(user_input):
                    print(f"Leikmanna nafnið '{user_input}' er nú þegar á skrá.")
                    input('Ýttu á ENTER til að halda áfram.')
                    continue
                captain_handle = user_input
                step = 3
                continue

            # Step 3 - Number of players
            if step == 3:
                user_input = self.input_handler.get_input_with_nav('Skráðu fjölda leikmanna (3-5): ')
                if user_input == 'QUIT':
                    in_team_registration = False
                    continue
                if user_input == 'BACK':
                    captain_handle = ''
                    step = 2
                    continue
                if not user_input.isdigit():
                    print('Sláðu inn númer 3 til 5.')
                    continue
                number = int(user_input)
                if number < 3 or number > 5:
                    print('Lið má bara hafa 3-5 leikmenn.')
                    continue
                number_of_players = number
                step = 4
                continue

            # Step 4 - Optional website and logo
            if step == 4:
                print('Valkvæðar upplýsingar um lið (sleppir með því að ýta á ENTER).')
                team_website = input('Vefslóð liðsins: ').strip()
                team_logo = input('Logo liðsins: ').strip()

                step = 5
                continue

            # Step 5 - Player registration
            if step == 5:
                player_handles = self.run_player_registration(team_name, number_of_players)

                if player_handles == 'QUIT':
                    in_team_registration = False
                    continue
                if captain_handle not in player_handles:
                    print('Fyrirliði þarf að vera einn af leikmönnunum.')
                    input('Ýttu á ENTER til að halda áfram.')
                    step = 2
                    continue
                step = 6
                continue

            # Step 6 - Create team
            if step == 6:
                try:
                    self.logic_api.create_team(
                        name = team_name, 
                        captain_handle = captain_handle,
                        player_handles = player_handles,
                        website = team_website,
                        logo = team_logo,
                        )
                    print(f"Liðið '{team_name}' hefur verið skráð!")
                except ValidationError as e:
                    print(f'Villa við skráningu liðs: {e}')
                input('Ýttu á ENTER til að halda áfram.')
                in_team_registration = False
                continue
    
    def run_player_registration(self, team_name: str, number_of_players: int) -> list[str]:
        """  """
        in_player_registration = True
        current_player = 1
        player_handles: list[str] = []

        while in_player_registration:
            if current_player > number_of_players:
                break

            self.input_handler.clear_screen()
            self.captain_menu.display_player_registration_menu(team_name, current_player)

            player_name = ''
            player_date_of_birth = ''
            player_address = ''
            player_phone = ''
            player_email = ''
            player_link = ''
            player_handle = ''

            step = 1

            while step <= 7 and in_player_registration:
                # Step 1 - Name
                if step == 1:
                    user_input = self.input_handler.get_input_with_nav('Skráðu fullt nafn: ')
                    if user_input == 'QUIT':
                        return 'QUIT'
                    if user_input == 'BACK':
                        if current_player == 1:
                            return 'QUIT'
                        current_player -= 1
                        if player_handles:
                            player_handles.pop()
                        break
                    player_name = user_input
                    step = 2
                    continue

                # Step 2 - Date of birth
                if step == 2:
                    user_input = self.input_handler.get_input_with_nav('Skráðu fæðingardag og ár: ')
                    if user_input == 'QUIT':
                        return 'QUIT'
                    if user_input == 'BACK':
                        step = 1
                        continue
                    player_date_of_birth = user_input
                    step = 3
                    continue

                # Step 3 - Address
                if step == 3:
                    user_input = self.input_handler.get_input_with_nav('Skráðu heimilisfang: ')

                    if user_input == 'QUIT':
                        return 'QUIT'
                    if user_input == 'BACK':
                        step = 2
                        continue
                    player_address = user_input
                    step = 4
                    continue

                # Step 4 - Phone
                if step == 4:
                    user_input = self.input_handler.get_input_with_nav('Skráðu símanúmer: ')
                    if user_input == 'QUIT':
                        return 'QUIT'
                    if user_input == 'BACK':
                        step = 3
                        continue
                    player_phone = user_input
                    step = 5
                    continue

                # Step 5 - Email
                if step == 5:
                    user_input = self.input_handler.get_input_with_nav('Skráðu netfang: ')
                    if user_input == 'QUIT':
                        return 'QUIT'
                    if user_input == 'BACK':
                        step = 4
                        continue
                    player_email = user_input
                    step = 6
                    continue

                # Step 6 - Link
                if step == 6:
                    user_input = self.input_handler.get_input_with_nav('Skráðu vefslóð: ', allow_empty = True)
                    if user_input == 'QUIT':
                        return 'QUIT'
                    if user_input == 'BACK':
                        step = 5
                        continue
                    player_link = user_input
                    step = 7
                    continue

                # Step 7 - Handle
                if step == 7:
                    user_input = self.input_handler.get_input_with_nav('Skráðu leikmanna nafn: ')
                    if user_input == 'QUIT':
                        return 'QUIT'
                    if user_input == 'BACK':
                        step = 6
                        continue
                    player_handle = user_input

                    if self.logic_api.handle_exists(player_handle):
                        print('Þetta leikmanna nafn er nú þegar í notkun.')
                        input('Ýttu á ENTER til að reyna aftur.')
                        continue
            
                #player_team_name --> Það er team_name í database...

                    try:
                        self.logic_api.create_player(
                            name = player_name,
                            date_of_birth = player_date_of_birth,
                            address = player_address,
                            phone = player_phone,
                            email = player_email,
                            link = player_link,
                            handle = player_handle,
                            team_name = '', # team is assigned when team is created
                        )
                    
                    except ValidationError as e:
                        print(f'Villa við skráningu leikmanns: {e}')
                        self.input_handler.wait_for_enter()
                        continue

                    player_handles.append(player_handle)
                    current_player += 1
                    break
        return player_handles

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
            

            organizer_input = self.input_handler.get_user_input(
                messages.ACTION_OR_BACK_PROMPT,
                
                {'1', '2', '3', 'b'})
            
            if organizer_input == '1':
                    self.tournament_creation_flow()
            elif organizer_input == '2':
                pass
            elif organizer_input == '3':
                pass
            elif organizer_input == 'b':

                in_orginizer_menu = False
                
    def tournament_creation_flow(self):
        tournament_name = self.input_handler.get_non_empty_string("Sláðu inn nafn móts:")
        tournament_venue = self.input_handler.get_non_empty_string("Sláðu inn staðsetningu:")
        tournament_start_date = self.input_handler.get_non_empty_string("Sláðu inn upphafsdagsetningu:")
        tournament_end_date = self.input_handler.get_non_empty_string("Sláðu inn endadagsetningu:")
        tournament_contact_name = self.input_handler.get_non_empty_string("Sláðu inn nafn tengiliðs:")
        tournament_contact_email = self.input_handler.get_non_empty_string("Sláðu inn netfang tengiliðs: ")
        tournament_contact_phone = self.input_handler.get_non_empty_string("Sláðu inn símanúmer tengiliðs:")
        
        max_servers = 3

        new_tournament = self.logic_api.create_tournament(
            name = tournament_name,
            venue = tournament_venue,
            start_date = tournament_start_date,
            end_date = tournament_end_date,
            contact_name = tournament_contact_name,
            contact_email = tournament_contact_email,
            contact_phone = tournament_contact_phone,
            max_servers = max_servers
    
        )

    
