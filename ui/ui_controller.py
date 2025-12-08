from ui.main_menu_ui import MainMenuUI
from ui.tournament_menu_ui import TournamentMenuUI
from ui.captain_menu_ui import CaptainMenuUI
from ui.organizer_menu_ui import OrganizerMenuUI
from ui.input_handler import InputHandler

from data.data_api import DataApi
from logic.tournament_logic import TournamentLogic
from logic.team_logic import TeamLogic
from logic.player_logic import PlayerLogic
from models.model_tournament import Tournament
from models.model_team import Team
from models.model_player import Player

class UIController:
    """Handles all UI flow and navigation between screens."""
    def __init__(self):
        self.main_menu = MainMenuUI()
        self.tournament_menu = TournamentMenuUI()
        self.captain_menu = CaptainMenuUI()
        self.organizer_menu = OrganizerMenuUI()
        self.input_handler = InputHandler()

        self.data_api = DataApi()

        self.tournament_logic = TournamentLogic(self.data_api)
        self.team_logic = TeamLogic(self.data_api)
        self.player_logic = PlayerLogic(self.data_api)
    
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
                self.tournaments_flow()
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
        tournament_names = self.tournament_logic.get_tournament_name_list()
        
        if not tournament_names:
            self.input_handler.clear_screen()
            self.tournament_menu.display_tournaments(tournament_names)
            input('Engin mót í kerfi. Ýttu á enter til þess að fara til baka.')
            return
        
        in_tournament_menu = True

        while in_tournament_menu:
            self.input_handler.clear_screen()
            self.tournament_menu.display_tournaments(tournament_names)

            valid_input = {str(i) for i in range(1, len(tournament_names) + 1)} | {'b'}

            user_input = self.input_handler.get_menu_input(
                'Sláðu inn númer móts eða til baka: ',
                valid_input
            )

            if user_input == 'b':
                in_tournament_menu = False
            else:
                index = int(user_input) - 1
                selected_tournament = self.tournament_logic.get_tournament_by_index(index)
                self.tournament_options_flow(selected_tournament)



    def tournament_options_flow(self, tournament: Tournament):
        """  """
        in_tournament_options = True
        while in_tournament_options:
            self.input_handler.clear_screen()
            self.tournament_menu.display_tournament_menu(tournament.name)

            user_input = self.input_handler.get_menu_input(
                'Sláðu inn númer aðgerðar eða til baka: ',
                {'1', '2', '3', 'b'}
            )

            if user_input == '1':
                self.tournament_schedule_flow(tournament)

            elif user_input == '2':
                self.tournament_scoreboard_flow(tournament)

            elif user_input == '3':
                self.tournament_teams_flow(tournament)

            elif user_input == 'b':
                in_tournament_options = False    

    def tournament_schedule_flow(self, tournament: Tournament):
        """  """
        in_tournament_schedule = True
        while in_tournament_schedule:
            self.input_handler.clear_screen()
            self.tournament_menu.display_tournament_schedule(tournament.name)

            user_input = self.input_handler.get_menu_input(
                'Sláðu inn b til að fara til baka: ',
                {'b'}
            )

            if user_input == 'b':
                in_tournament_schedule = False

    def tournament_scoreboard_flow(self, tournament: Tournament):
        """  """
        in_tournament_scoreboard = True
        while in_tournament_scoreboard:
            self.input_handler.clear_screen()
            self.tournament_menu.display_tournament_scoreboard(tournament.name)

            user_input = self.input_handler.get_menu_input(
                'Sláðu inn b til að fara til baka: ',
                {'b'}
            )

            if user_input == 'b':
                in_tournament_scoreboard = False

    def tournament_teams_flow(self, tournament: Tournament):
        """  """
        in_tournament_teams = True
        while in_tournament_teams:
            teams = self.team_logic.get_teams_for_tournament(tournament.tournament_id)
            self.input_handler.clear_screen()
            self.tournament_menu.display_tournament_teams(tournament.name, teams)

            valid_input = {str(i) for i in range(1, len(teams) + 1)} | {'b'}

            user_input = self.input_handler.get_menu_input(
                'Sláðu inn númer liðs eða til baka: ',
                valid_input
            )

            if user_input == 'b':
                in_tournament_teams = False
            else:
                index = int(user_input) - 1
                selected_team: Team = teams[index]
                self.tournament_team_players_flow(tournament, selected_team)


    def tournament_team_players_flow(self, tournament: Tournament, team: Team):
        """  """
        players: list[Player] = self.player_logic.get_players_for_team(team.team_name)

        self.input_handler.clear_screen()
        self.tournament_menu.display_team_players(tournament.name, team.team_name, players)
        input('Ýttu á enter til að fara til baka: ')



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