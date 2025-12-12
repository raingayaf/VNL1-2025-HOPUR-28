# UI imports
from ui.schedule_menu_ui import ScheduleUI
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
        # Logic layer
        self.logic_api: LLApi = LLApi()
        # UI menus
        self.main_menu = MainMenuUI()
        self.tournament_menu = TournamentMenuUI()
        self.captain_menu = CaptainMenuUI()
        self.organizer_menu = OrganizerMenuUI()
        self.schedule_menu = ScheduleUI(self.logic_api)

        # Input handling
        self.input_handler = InputHandler()

    # -----------------------------MAIN-MENU-------------------------------
    def run_main_menu(self) -> None:
        """Runs the main menu and routes the user based on their selection."""
        in_main_menu = True
        error_message = None

        while in_main_menu:
            self.input_handler.clear_screen()

            # Show error message from previous iteration
            if error_message is not None:
                print("\n" + error_message.center(self.input_handler.WIDTH) + "\n")
                error_message = None

            # Show menu and handle user selection
            self.main_menu.display_main_menu()
            user_input = self.input_handler.get_user_input(
                "Sláðu inn númer aðgerðar: ", {"1", "2", "3", "q"}
            )
            # Routes user to chosen submenu or closes program
            if user_input == "1":
                has_tournaments = self.run_tournaments_menu()
                if not has_tournaments:
                    # Generates error message that is shown before next iteration
                    error_message = messages.NO_TOURNAMENTS
            elif user_input == "2":
                self.run_captain_menu()
            elif user_input == "3":
                self.input_handler.clear_screen()
                self.orginizer_menu_flow()
            elif user_input == "q":
                in_main_menu = False

    # ----------------------------GENERAL-USER-MENUS-------------------------
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
            valid_input = {str(i) for i in range(1, len(tournament_names) + 1)} | {"b"}
            user_input = self.input_handler.get_user_input(
                'Sláðu inn númer móts eða farðu til baka: ', valid_input
            )
            if user_input == "b":
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
                "Sláðu inn númer aðgerðar eða farðu til baka: ", {"1", "2", "3", "b"}
            )
            # Routes user to chosen submenu
            if user_input == "1":
                self.run_tournament_schedule(tournament)
            elif user_input == "2":
                self.run_tournament_scoreboard(tournament)
            elif user_input == "3":
                self.run_tournament_teams(tournament)
            elif user_input == "b":
                # Return to the previous menu
                in_tournament_options = False

    def run_tournament_schedule(self, tournament: Tournament) -> None:
        """Displays the tournament schedule until the user chooses to return to the previous menu."""
        in_tournament_schedule = True

        while in_tournament_schedule:
            self.input_handler.clear_screen()
            schedule = self.logic_api.get_saved_schedule(tournament)
            self.schedule_menu.display_user_schedule(tournament, schedule)
            
            #self.tournament_menu.display_tournament_schedule(tournament.name)
            user_input = self.input_handler.get_user_input("Sláðu inn 'b' til að fara til baka: ", {"b"})
            if user_input == "b":
                # Return to the previous menu
                in_tournament_schedule = False

    # def run_tournament_scoreboard(self, tournament: Tournament) -> None:
    #     """Displays the tournament scoreboard until the user chooses to return to the previous menu."""
    #     in_tournament_scoreboard = True

    #     while in_tournament_scoreboard:
    #         self.input_handler.clear_screen()
    #         self.tournament_menu.display_tournament_scoreboard(tournament.name)
    #         user_input = self.input_handler.get_user_input("Sláðu inn 'b' til að fara til baka: ", {"b"})
    #         if user_input == "b":
    #             # Return to the previous menu
    #             in_tournament_scoreboard = False

    def run_tournament_teams(self, tournament: Tournament) -> None:
        """Displays the teams in the chosen tournament and routes the user based on their selection."""
        in_tournament_teams = True
        # Show tournament teams and handle user selection
        while in_tournament_teams:
            teams = self.logic_api.get_teams_for_tournament(tournament.tournament_id)
            self.input_handler.clear_screen()
            self.tournament_menu.display_tournament_teams(tournament.name, teams)
            valid_input = {str(i) for i in range(1, len(teams) + 1)} | {"b"}
            user_input = self.input_handler.get_user_input(
                "Sláðu inn númer liðs eða farðu til baka: ", valid_input
            )
            if user_input == "b":
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
            captain: Player | None = self.logic_api.get_team_captain(team)
            team_tournaments: list[Tournament] = self.logic_api.get_tournaments_for_team(team.team_name)

            self.input_handler.clear_screen()
            self.tournament_menu.display_team_players(
                current_tournament=tournament, team = team, players = players, captain = captain, tournaments = team_tournaments,)
            
            user_input = self.input_handler.get_user_input("Sláðu inn 'b' til að fara til baka: ", {"b"})
            if user_input == "b":
                # Return to the previous menu
                in_team_players_menu = False

    # ------------------------CAPTAIN-MENU-FLOW------------------------------
    def run_captain_menu(self):
        """Runs the captain menu and routes the user based on their selection."""
        in_captain_menu = True
        while in_captain_menu:
            self.input_handler.clear_screen()
            self.captain_menu.display_captain_menu()
            captain_input = self.input_handler.get_user_input(
                "Sláðu inn númer aðgerðar eða farðu til baka: ", {"1", "2", "b"}
            )
            if captain_input == "1":
                self.run_team_registration()
            elif captain_input == "2":
                self.run_captain_verification()
            elif captain_input == "b":
                in_captain_menu = False

    def run_team_registration(self) -> None:
        """Run the team registration for a team captain."""
        in_team_registration = True
        step = 1
        players_on_team: list[str] = []
        registered_team_players: list[dict[str, str]] = []

        team_name = ""
        captain_handle = ""
        number_of_players = 0
        team_website = ""
        team_logo = ""
        
        while in_team_registration:
            self.input_handler.clear_screen()
            self.captain_menu.display_team_registration_menu()

            # Shows previous entered input when user goes back
            if team_name:
                print(f"Skráðu heiti liðsins: {team_name}")
            if captain_handle:
                print(f"Skráðu leikmanna nafn fyrirliðans(handle): {captain_handle}")
            if number_of_players:
                print(f"Skráðu fjölda leikmanna (3-5): {number_of_players}")
            if team_website or step == 5:
                print(
                    "\n"
                    + "Valkvæðar upplýsingar um lið.".center(self.input_handler.WIDTH)
                )
                print("Ýttu á ENTER til að sleppa.".center(self.input_handler.WIDTH))
                print(f"Vefslóð liðsins: {team_website or ''}")
            if team_logo or step == 6:
                print(f"Logo liðsins: {team_logo or ''}")

            # Step 1 - Team name
            if step == 1:
                user_input = self.input_handler.get_input_with_nav(
                    "Skráðu heiti liðsins: "
                )
                if user_input == "QUIT":
                    in_team_registration = False
                    continue
                if user_input == "BACK":
                    in_team_registration = False
                    continue
                try: 
                    validated_name = self.logic_api.validate_team_name_format(user_input)
                except ValidationError as exception:
                    print("\n" + str(exception).center(self.input_handler.WIDTH))
                    self.input_handler.try_again_enter()
                    continue

                if self.logic_api.team_name_exists(validated_name):
                    team_exists_message = f"Liðið '{validated_name}' er nú þegar á skrá!"
                    print("\n" + team_exists_message.center(self.input_handler.WIDTH))
                    print(
                        "Vinsamlegast veldu nafn sem er ekki í notkun.".center(
                            self.input_handler.WIDTH
                        )
                    )
                    self.input_handler.try_again_enter()
                    continue
                team_name = validated_name
                step = 2
                continue

            # Step 2 - Captain handle
            if step == 2:
                user_input = self.input_handler.get_input_with_nav(
                    "Skráðu leikmanna nafn fyrirliðans(handle): "
                )
                if user_input == "QUIT":
                    in_team_registration = False
                    continue
                if user_input == "BACK":
                    team_name = ""
                    step = 1
                    continue
        
                try:
                    validated_handle = self.logic_api.validate_captain_handle_format(user_input)
                except ValidationError as exception:
                    print("\n" + str(exception).center(self.input_handler.WIDTH))
                    self.input_handler.try_again_enter()
                    continue
                
                if self.logic_api.handle_exists(validated_handle):
                    handle_exists_message = (
                        f"Leikmanna nafnið '{user_input}' er nú þegar á skrá."
                    )
                    print("\n" + handle_exists_message.center(self.input_handler.WIDTH))
                    print(
                        "Vinsamlegast veldu leikmanna nafn (handle) sem er ekki í notkun.".center(
                            self.input_handler.WIDTH
                        )
                    )
                    self.input_handler.try_again_enter()
                    continue
                captain_handle = validated_handle
                step = 3
                continue

            # Step 3 - Number of players
            if step == 3:
                user_input = self.input_handler.get_input_with_nav(
                    "Skráðu fjölda leikmanna (3-5): "
                )
                if user_input == "QUIT":
                    in_team_registration = False
                    continue
                if user_input == "BACK":
                    captain_handle = ""
                    step = 2
                    continue
                if not user_input.isdigit():
                    print(
                        "\nÓgildur innsláttur! Vinsamlegast sláðu inn heiltölu frá 3-5.".center(
                            self.input_handler.WIDTH
                        )
                    )
                    self.input_handler.try_again_enter()
                    continue
                number = int(user_input)
                if number < 3:
                    num_below = f"Fjöldinn má ekki vera minni en 3!"
                    print("\n" + num_below.center(self.input_handler.WIDTH))
                    self.input_handler.try_again_enter()
                    continue
                if number > 5:
                    num_above = f"Fjöldinn má ekki vera meiri en 5!"
                    print("\n" + num_above.center(self.input_handler.WIDTH))
                    self.input_handler.try_again_enter()
                    continue
                number_of_players = number
                step = 4
                continue

            # Step 4 - Optional website
            if step == 4:
                print(
                    "\n"
                    + "Valkvæðar upplýsingar um lið.".center(self.input_handler.WIDTH)
                )
                print("Ýttu á ENTER til að sleppa.".center(self.input_handler.WIDTH))
                user_input = self.input_handler.get_input_with_nav(
                    "Vefslóð liðsins: ", allow_empty=True
                )
                if user_input == "QUIT":
                    in_team_registration = False
                    continue
                if user_input == "BACK":
                    number_of_players = 0
                    step = 3
                    continue
                try:
                    team_website = self.logic_api.validate_team_website(user_input)
                except ValidationError as exception:
                    print("\n" + str(exception).center(self.input_handler.WIDTH))
                    self.input_handler.try_again_enter()
                    continue

                step = 5
                continue

            # Step 5 - Optional logo
            if step == 5:
                user_input = self.input_handler.get_input_with_nav(
                    "Logo liðsins: ", allow_empty=True
                )
                if user_input == "QUIT":
                    in_team_registration = False
                    continue
                if user_input == "BACK":
                    team_website = ""
                    step = 4
                    continue
                try: 
                    team_logo = self.logic_api.validate_team_logo(user_input)
                except ValidationError as exception:
                    print("\n" + str(exception).center(self.input_handler.WIDTH))
                    self.input_handler.try_again_enter()
                    continue

                step = 6
                continue

            # Step 6 - Player registration
            if step == 6:
                players_on_team = self.run_player_registration(
                    team_name, number_of_players, captain_handle
                )

                if players_on_team == "QUIT":
                    in_team_registration = False
                    continue
                if players_on_team == "BACK":
                    team_logo = ""
                    step = 5
                    continue

                registered_team_players = players_on_team
                step = 7
                continue

            # Step 7 - Create team
            if step == 7:
                try:
                    self.logic_api.create_team_with_players(
                        name=team_name,
                        captain_handle=captain_handle,
                        registered_team_players=registered_team_players,
                        website=team_website,
                        logo=team_logo,
                    )
                except ValidationError as exception:
                    print("\n" + "Óvænt villa við skráningu liðs :(".center(self.input_handler.WIDTH))
                    print(str(exception))
                    self.input_handler.try_again_enter()
                    step = 1
                    team_name = ""
                    captain_handle = ""
                    number_of_players = ""
                    team_website = ""
                    team_logo = ""
                    registered_team_players = []
                    continue
                
                self.input_handler.clear_screen()
                self.captain_menu.display_team_registration_done(team_name)
                self.input_handler.back_home_enter()
                in_team_registration = False
                continue

    def run_player_registration(self, team_name: str, number_of_players: int, captain_handle: str):
        """Runs registration on each player in team (collects data)."""
        in_player_registration = True
        current_player = 1
        players_on_team: list[dict[str, str]] = []

        while in_player_registration:
            if current_player > number_of_players:
                player_handles = [p["handle"] for p in players_on_team]

                if captain_handle not in player_handles:
                    self.input_handler.clear_screen()
                    print("Fyrirliði þarf að vera einn af leikmönnunum!".center(self.input_handler.WIDTH))
                    print(f"Vinsamlegast breyttu leikmanna nafni (handle) hjá einum leikmanni í '{captain_handle}'.".center(self.input_handler.WIDTH))
                    self.input_handler.try_again_enter()
                    current_player = number_of_players
                    continue
                break 

            # If information already collected
            if current_player <= len(players_on_team):
                existing = players_on_team[current_player - 1]
                player_name = existing["name"]
                player_date_of_birth = existing["date_of_birth"]
                player_address = existing["address"]
                player_phone = existing["phone"]
                player_email = existing["email"]
                player_link = existing["link"]
                player_handle = ["handle"]
                step = 7
            else:
                player_name = ""
                player_date_of_birth = ""
                player_address = ""
                player_phone = ""
                player_email = ""
                player_link = ""
                player_handle = ""
                step = 1

            while step <= 7 and in_player_registration:
                
                self.input_handler.clear_screen()
                self.captain_menu.display_player_registration_menu(team_name, current_player)

                # Shows previous entered input when user goes back
                if player_name:
                    print(f"Skráðu fullt nafn: {player_name}")
                if player_date_of_birth:
                    print(f"Skráðu fæðingardag(YYYY-MM-DD): {player_date_of_birth}")
                if player_address:
                    print(f"Skráðu heimilisfang: {player_address}")
                if player_phone:
                    print(f"Skráðu símanúmer(XXXXXXX): {player_phone}")
                if player_email:
                    print(f"Skráðu netfang: {player_email}")
                if player_link:
                    print(f"Skráðu vefslóð(valkvætt): {player_link}")
                if player_handle:
                    print(f"Skráðu leikmanna nafn(handle): {player_handle}")

                # Step 1 - Name
                if step == 1:
                    user_input = self.input_handler.get_input_with_nav(
                        "Skráðu fullt nafn: "
                    )
                    if user_input == "QUIT":
                        return "QUIT"
                    if user_input == "BACK":
                        if current_player == 1:
                            return "BACK"
                        current_player -= 1
                        break # Goes back to previous player
                    try:
                        player_name = self.logic_api.validate_player_name(user_input)
                    except ValidationError as exception:
                        print("\n" + str(exception).center(self.input_handler.WIDTH))
                        self.input_handler.try_again_enter()
                        continue
                
                    step = 2
                    continue

                # Step 2 - Date of birth
                if step == 2:
                    user_input = self.input_handler.get_input_with_nav(
                        "Skráðu fæðingardag(YYYY-MM-DD): "
                    )
                    if user_input == "QUIT":
                        return "QUIT"
                    if user_input == "BACK":
                        player_name = ""
                        step = 1
                        continue
                    try:
                        player_date_of_birth = self.logic_api.validate_player_date_of_birth(user_input)
                    except ValidationError as exception:
                        print("\n" + str(exception).center(self.input_handler.WIDTH))
                        self.input_handler.try_again_enter()
                        continue

                    step = 3
                    continue

                # Step 3 - Address
                if step == 3:
                    user_input = self.input_handler.get_input_with_nav(
                        "Skráðu heimilisfang: "
                    )

                    if user_input == "QUIT":
                        return "QUIT"
                    if user_input == "BACK":
                        player_date_of_birth = ""
                        step = 2
                        continue
                    try: 
                        player_address = self.logic_api.validate_player_address(user_input)
                    except ValidationError as exception:
                        print("\n" + str(exception).center(self.input_handler.WIDTH))
                        self.input_handler.try_again_enter()
                        continue
                    step = 4
                    continue

                # Step 4 - Phone
                if step == 4:
                    user_input = self.input_handler.get_input_with_nav(
                        "Skráðu símanúmer(XXXXXXX): "
                    )
                    if user_input == "QUIT":
                        return "QUIT"
                    if user_input == "BACK":
                        player_address = ""
                        step = 3
                        continue
                    try:
                        player_phone = self.logic_api.validate_player_phone(user_input)
                    except ValidationError as exception:
                        print("\n" + str(exception).center(self.input_handler.WIDTH))
                        self.input_handler.try_again_enter()
                        continue
                    step = 5
                    continue

                # Step 5 - Email
                if step == 5:
                    user_input = self.input_handler.get_input_with_nav(
                        "Skráðu netfang: "
                    )
                    if user_input == "QUIT":
                        return "QUIT"
                    if user_input == "BACK":
                        player_phone = ""
                        step = 4
                        continue
                    try:
                        player_email = self.logic_api.validate_player_email(user_input)
                    except ValidationError as exception:
                        print("\n" + str(exception).center(self.input_handler.WIDTH))
                        self.input_handler.try_again_enter()
                        continue
                    step = 6
                    continue

                # Step 6 - Link
                if step == 6:
                    user_input = self.input_handler.get_input_with_nav(
                        "Skráðu vefslóð(valkvætt): ", allow_empty=True
                    )
                    if user_input == "QUIT":
                        return "QUIT"
                    if user_input == "BACK":
                        player_email = ""
                        step = 5
                        continue
                    try:
                        player_link = self.logic_api.validate_player_link(user_input)
                    except ValidationError as exception:
                        print("\n" + str(exception).center(self.input_handler.WIDTH))
                        self.input_handler.try_again_enter()
                        continue
                    step = 7
                    continue

                # Step 7 - Handle
                if step == 7:
                    user_input = self.input_handler.get_input_with_nav(
                        "Skráðu leikmanna nafn(handle): "
                    )
                    if user_input == "QUIT":
                        return "QUIT"
                    if user_input == "BACK":
                        player_link = ""
                        step = 6
                        continue
                    try:
                        validated_handle = self.logic_api.validate_player_handle(user_input)
                    except ValidationError as exception:
                        print("\n" + str(exception).center(self.input_handler.WIDTH))
                        self.input_handler.try_again_enter()
                        continue
                    if self.logic_api.handle_exists(validated_handle):
                        handle_exists_message = (
                            f"Leikmanna nafnið '{validated_handle}' er nú þegar á skrá."
                        )
                        print("\n" + handle_exists_message.center(self.input_handler.WIDTH))
                        print(
                            "Vinsamlegast veldu leikmanna nafn (handle) sem er ekki í notkun.".center(
                                self.input_handler.WIDTH
                            )
                        )
                        self.input_handler.try_again_enter()
                        continue
                    player_handle = validated_handle

                    # Save current player
                    player_data = {
                        "name": player_name,
                        "date_of_birth": player_date_of_birth,
                        "address": player_address,
                        "phone": player_phone,
                        "email": player_email,
                        "link": player_link,
                        "handle": player_handle
                    }
                    if current_player <= len(players_on_team):
                        players_on_team[current_player - 1] = player_data
                    else: 
                        players_on_team.append(player_data)

                    current_player += 1
                    break
        return players_on_team

    def run_captain_verification(self):
        """ """
        in_captain_verification = True
        step = 1

        captain_handle = ""
        team_name = ""

        while in_captain_verification:
            self.input_handler.clear_screen()
            self.captain_menu.display_captain_verification_menu()

            if captain_handle:
                print(f"Sláðu inn leikmanna nafn þitt(handle): {captain_handle}")

            if team_name:
                print(f"Sláðu inn heiti á liðinu þínu: {team_name}")

            if step == 1:
                user_input = self.input_handler.get_input_with_nav(
                    "Sláðu inn leikmanna nafn þitt(handle): "
                )
                if user_input == "BACK":
                    return
                captain_handle = user_input
                step = 2
                continue

            if step == 2:
                user_input = self.input_handler.get_input_with_nav(
                    "Sláðu inn heiti á liðinu þínu: "
                )
                if user_input == "BACK":
                    captain_handle = ""
                    step = 1
                    continue

                team_name = user_input

                try: 
                    team_info = self.logic_api.get_team_info_for_captain(
                        captain_handle, team_name
                    )
                except ValueError as exc:
                    print(f"\n{exc}")
                    input("Ýttu á ENTER og reyndu aftur.")
                    step = 1
                    continue
                self.run_team_information(team_info)
                return


    def run_team_information(self, team_info: dict):
        """ """
        WIDTH: int = 60

        in_team_information = True
        team = team_info["team"]
        players = team_info["players"]

        if not players:
            self.input_handler.clear_screen()
            self.captain_menu.display_team_players_menu(team.team_name)
            print("Engir leikmenn eru skráðir í liðið.")
            input("Ýttu á ENTER til að fara til baka.")
            return

        while in_team_information:
            self.input_handler.clear_screen()
            self.captain_menu.display_team_players_menu(team.team_name)

            for number, player in enumerate(players, start = 1):
                    print(f"{number}. {player.handle}")
            print('\nb: Til baka\n')
            print('*' * WIDTH + '\n')
            print('Sláðu inn númer leikmanns til að skoða persónuupplýsingarnar')

            valid_input = {str(i) for i in range(1, len(players) + 1)} | {"b"}
            user_input = self.input_handler.get_user_input(
                "hans eða farðu til baka: ",
                valid_input,
            )

            if user_input == "b":
                in_team_information = False
            else:
                index = int(user_input) - 1
                selected_player = players[index]
                self.run_player_information(selected_player)


    def run_player_information(self, player):
        """Shows information for a player and allows editing."""
        WIDTH: int = 60
        in_player_info = True
        while in_player_info:
            self.input_handler.clear_screen()
            self.captain_menu.display_player_information_menu(player.handle)

            print(f"1. Nafn: {player.name}")
            print(f"2. Fæðingardagur: {player.date_of_birth}")
            print(f"3. Heimilisfang: {player.address}")
            print(f"4. Sími: {player.phone}")
            print(f"5. Netfang: {player.email}")
            print(f"6. Vefslóð: {player.link}")
            print('\nb: Til baka\n')
            print('*' * WIDTH + '\n')
            print("Ef að þú vilt breyta einstökum upplýsingum sláðu þá")

            valid_input = {str(i) for i in range(1, 7)} | {"b"}
            user_input = self.input_handler.get_user_input(
                "inn númer þess sem þú vilt breyta eða farðu til baka: ",
                valid_input
            )

            if user_input == "b":
                in_player_info = False
                continue
            choice = int(user_input)

            if choice == 1:
                field_name = "name"
                prompt = "Skráðu nýtt nafn: "
                validator = self.logic_api.validate_player_name
                allow_empty = False
            elif choice == 2:
                field_name = "date_of_birth"
                prompt = "Skráðu nýjan fæðingardag(YYYY-MM-DD): "
                validator = self.logic_api.validate_player_date_of_birth
                allow_empty = False
            elif choice == 3:
                field_name = "address"
                prompt = "Skráðu nýtt heimilisfang: "
                validator = self.logic_api.validate_player_address
                allow_empty = False
            elif choice == 4:
                field_name = "phone"
                prompt = "Skráðu nýtt símanúmer(XXXXXXX): "
                validator = self.logic_api.validate_player_phone
                allow_empty = False
            elif choice == 5:
                field_name = "email"
                prompt = "Skráðu nýtt netfang: "
                validator = self.logic_api.validate_player_email
                allow_empty = False
            elif choice == 6:
                field_name = "link"
                prompt = "Skráðu nýja vefslóð: "
                validator = self.logic_api.validate_player_link
                allow_empty = True
            else:
                continue

            if allow_empty:
                new_value = input("\n" + prompt).strip()
            else:
                new_value = input("\n" + prompt).strip()
                if not new_value:
                    print("\n" + "Þú verður að skrá þessar upplýsingar.".center(WIDTH))
                    self.input_handler.try_again_enter()
                    continue
            try: 
                changed_info = validator(new_value)
            except ValidationError as exception:
                print("\n" + str(exception).center(WIDTH))
                self.input_handler.try_again_enter()
                continue
            
            setattr(player, field_name, changed_info)

            try:
                self.logic_api.update_player(player)
                print("\n" + "Upplýsingunum hefur verið breytt.".center(WIDTH))
            except Exception as exc:
                error_updating = f"Tókst ekki að uppfæra leikmann: {exc}"
                print("\n"+ error_updating.center(WIDTH))
            self.input_handler.try_again_enter()



    # -----------------------ORGANIZER-MENU-FLOW------------------------------

    def orginizer_menu_flow(self):
        """Operations for displaying orginizer menu"""
        in_orginizer_menu = True
        while in_orginizer_menu:
            self.input_handler.clear_screen()
            self.organizer_menu.display_organizer_menu()

            organizer_input = self.input_handler.get_user_input(
                messages.ACTION_OR_BACK_PROMPT,
                
                {'1', '2', '3', '4', 'b'})
            

            # Register tournament
            if organizer_input == "1":
                self.tournament_creation_flow()
            # Schedule tournament
            elif organizer_input == "2":
                self.run_tournament_displey_selection() 

            elif organizer_input == "3":
                self.run_all_teams_view()
            # See all available players and info
            elif organizer_input == "4":
                self.run_all_players_view()
            elif organizer_input == "b":

                in_orginizer_menu = False

    def run_display_menu(self, tournament):
        """Organizer schedule/bracket workflow."""
        print(f"DEBUG: run_display_menu for {tournament.name}, id={tournament.tournament_id}")
        in_display_menu = True

        teams = self.logic_api.get_all_teams()

        while in_display_menu:
            self.input_handler.clear_screen()

            self.organizer_menu.display_tournament_schedule_menu(tournament)

            choice = self.input_handler.get_user_input(
                "Sláðu inn númer aðgerðar eða 'b' til að fara til baka: ",
                {"1", "2", "3", "4", "5", "6", "b"},
            )

            if choice == "1":
                # Generate schedule for day 1 (R16)
                try:
                    self.logic_api.generate_round_of_16(tournament, teams)
                    matches = self.logic_api.get_matches_for_tournament(tournament)
                    print("Dagskrá fyrir dag 1 (R16) hefur verið búin til.")
                    print(f"fjöldi leikja: {len(matches)}")
                except Exception as e:
                    print(f"Villa: {e}")
                self.input_handler.wait_for_enter()

            elif choice == "2":
                # Generate schedule for day 2 morning (QF)
                try:
                    self.logic_api.generate_quarterfinals(tournament)
                    print("Dagskrá fyrir dag 2 (QF) hefur verið búin til.")
                except Exception as e:
                    print(f"Villa: {e}")
                self.input_handler.wait_for_enter()

            elif choice == "3":
                # Generate schedule for day 2 evening (SF)
                try:
                    self.logic_api.generate_semifinals(tournament)
                    print("Dagskrá fyrir dag 2 (SF) hefur verið búin til.")
                except Exception as e:
                    print(f"Villa: {e}")
                self.input_handler.wait_for_enter()

            elif choice == "4":
                # Generate schedule for day 3 (Finals)
                try:
                    self.logic_api.generate_final(tournament)
                    print("Dagskrá fyrir dag 3 (úrslitaleik) hefur verið búin til.")
                except Exception as e:
                    print(f"Villa: {e}")
                self.input_handler.wait_for_enter()

            elif choice == "5":
                # View schedule – ask which day to show
                self.show_schedule_for_tournament(tournament)

            elif choice == "6":
                # Enter result for a match
                self.enter_match_result(tournament)

            elif choice == "b":
                in_display_menu = False
    
    def show_schedule_for_tournament(self, tournament):
        schedule = self.logic_api.get_schedule_for_tournament(tournament)

        if not schedule:
            print("Engin dagskrá til fyrir þetta mót")
            self.input_handler.wait_for_enter()
            return
        
        days = sorted(set(row["day"] for row in schedule))

        print("\nTiltækir dagar í dagskrá:", ",".join(str(d) for d in days))
        day_input = input("Veldu dag til að skoða (t.d. 1): ").strip()

        try:
            day_to_show = int(day_input)
        except ValueError:
            print("Ógilt gildi fyrir dag, veldu tölu")
            self.input_handler.wait_for_enter()
            return
        
        self.input_handler.clear_screen()
        self.schedule_menu.displey_schedule_menu(tournament, schedule, day_to_show)
        self.input_handler.wait_for_enter()
    
    def enter_match_result(self, tournament):
        """Enter match results on loop until finished or input b to quit"""
        in_enter_match_result = True

        while in_enter_match_result:
            self.input_handler.clear_screen()
            schedule = self.logic_api.get_schedule_for_tournament(tournament)

            incomplete = [row for row in schedule if not row["completed"]]

            if not incomplete:
                print("Allir leikir hafa verið skráðir fyrir þetta mót.")
                self.input_handler.wait_for_enter()
                return

            print("\nLeikir sem á eftir að skrá úrslit fyrir:")
            for row in incomplete:
                status = "✓" if row["completed"] else " "
                print(
                    f"[{status}] ID {row['match_id']} - ({row['round']}) "
                    f"{row['team_a']} vs {row['team_b']} kl. {row['time']} (dagur {row['day']})"
                )

            user_input = input("\nSláðu inn ID leiks eða 'b~' til að hætta: ").strip()
            if user_input.lower() == "b~":
                return

            try:
                match_id = int(user_input)
            except ValueError:
                print("Ógilt gildi fyrir ID.")
                self.input_handler.wait_for_enter()
                continue

            valid_ids = {row["match_id"] for row in incomplete}
            if match_id not in valid_ids:
                print("Þetta ID tilheyrir ekki ókláruðum leik.")
                self.input_handler.wait_for_enter()
                continue

            try:
                score_a = int(input("Sláðu inn stig liðs A: ").strip())
                score_b = int(input("Sláðu inn stig liðs B: ").strip())
            except ValueError:
                print("Ógilt gildi fyrir stig.")
                self.input_handler.wait_for_enter()
                continue

            try:
                self.logic_api.record_match_result(match_id, score_a, score_b)
                print("Úrslit hafa verið skráðar.")
            except Exception as e:
                print(f"Villa: {e}")

            self.input_handler.wait_for_enter()
            

        
    def run_tournament_displey_selection(self):
        """Show available tournaments"""
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
            valid_input = {str(i) for i in range(1, len(tournament_names) + 1)} | {"b"}
            user_input = self.input_handler.get_user_input(
                messages.TOURNAMENT_SELECTION_PROMPT, valid_input
            )
            if user_input == "b":
                # Return to main menu
                in_tournament_menu = False
            else:
                # Open options for selected tournament
                index = int(user_input) - 1
                selected_tournament = self.logic_api.get_tournament_by_index(index)
                self.run_display_menu(selected_tournament)

    def run_all_players_view(self):
        """Show all players in system. Reuses display_team_players code without the team filters"""
        in_players_menu = True

        while in_players_menu:
            all_players: list[Player] = self.logic_api.get_all_players()

            self.input_handler.clear_screen()

            self.tournament_menu.display_team_players(
                tournament_name="Skráðir leikmenn", team_name="", players=all_players
            )

            valid_inputs = {str(i) for i in range(1, len(all_players) + 1)} | {"b"}
            user_input = self.input_handler.get_user_input(
                "Sláðu inn númer leikmanns til að skoða nánar eða 'b' til að fara til baka: ",
                valid_inputs,
            )

            if user_input == "b":
                in_players_menu = False
            else:
                # Goes into a function for viewing single player info
                index = int(user_input) - 1
                selected_player = all_players[index]
                self.run_single_player_information(selected_player)

            # Creates new tournament
    def tournament_creation_flow(self):
        """Run the tournament registration flow for an organizer."""
        self.input_handler.clear_screen()
        self.organizer_menu.display_organizer_registration_menu()

        # Name
        tournament_name = self.input_handler.get_input_with_nav(
            "Sláðu inn nafn móts: ")
        if tournament_name == "QUIT" or tournament_name == "BACK":
            return

        # Venue
        tournament_venue = self.input_handler.get_input_with_nav(
            "Sláðu inn staðsetningu: ")
        if tournament_venue == "QUIT" or tournament_venue == "BACK":
            return

        # Start date
        tournament_start_date = self.input_handler.get_input_with_nav(
            "Sláðu inn upphafsdagsetningu: ")
        if tournament_start_date == "QUIT" or tournament_start_date == "BACK":
            return

        # End date
        tournament_end_date = self.input_handler.get_input_with_nav(
            "Sláðu inn endadagsetningu: ")
        if tournament_end_date == "QUIT" or tournament_end_date == "BACK":
            return

        # Contact name
        tournament_contact_name = self.input_handler.get_input_with_nav(
            "Sláðu inn nafn tengiliðs: ")
        if tournament_contact_name == "QUIT" or tournament_contact_name == "BACK":
            return

        # Contact email
        tournament_contact_email = self.input_handler.get_input_with_nav(
            "Sláðu inn netfang tengiliðs: ")
        if tournament_contact_email == "QUIT" or tournament_contact_email == "BACK":
            return
        
        # Contact phone
        tournament_contact_phone = self.input_handler.get_input_with_nav(
            "Sláðu inn símanúmer tengiliðs: ")
        if tournament_contact_phone == "QUIT" or tournament_contact_phone == "BACK":
            return

        max_servers = 3

        self.logic_api.create_tournament(
            name=tournament_name,
            venue=tournament_venue,
            start_date=tournament_start_date,
            end_date=tournament_end_date,
            contact_name=tournament_contact_name,
            contact_email=tournament_contact_email,
            contact_phone=tournament_contact_phone,
            max_servers=max_servers,
        )

        self.organizer_menu.display_tournament_creation_done()
        self.input_handler.wait_for_enter()

    def run_single_player_information(self, player: Player) -> None:
        """Shows information about a single player."""
        in_player_info = True

        while in_player_info:
            self.input_handler.clear_screen()
            width = self.input_handler.WIDTH

            print("*" * width)
            print("E-SPORTS".center(width))
            print("*" * width + "\n")

            print("Upplýsingar um leikmann".center(width) + "\n")
            # Shows handle as main title
            print(player.handle.center(width) + "\n")

            print(f"Nafn: {player.name}")
            print(f"Fæðingardagur: {player.date_of_birth}")
            print(f"Heimilisfang: {player.address}")
            print(f"Sími: {player.phone}")
            print(f"Netfang: {player.email}")

            print("\n" + "*" * width + "\n")
            
            user_input = self.input_handler.get_user_input(messages.BACK_PROMPT, {"b"})

            if user_input == "b":
                in_player_info = False

    def run_all_teams_view(self) -> None:
        """Shows a list of all teams in the system and allows for selecting one for information"""
        in_teams_menu = True

        while in_teams_menu:
            teams: list[Team] = self.logic_api.get_all_teams()

            self.input_handler.clear_screen()

            self.tournament_menu.display_tournament_teams(
                tournament_name = "Skráð lið",   
                teams = teams,
            )

            # allows organizer to pick a team by number
            valid_inputs = {str(i) for i in range(1, len(teams) + 1)} | {"b"}
            user_input = self.input_handler.get_user_input(
                "Sláðu inn númer liðs til að skoða leikmenn eða 'b' til að fara til baka: ",
                valid_inputs,
            )

            if user_input == "b":
                in_teams_menu = False
            else:
                index = int(user_input) - 1
                selected_team = teams[index]
                self.run_team_players_for_team(selected_team)


    def run_team_players_for_team(self, team: Team) -> None:
        """Show all players in a given team from the organizer view."""
        in_players_menu = True

        while in_players_menu:
            players: list[Player] = self.logic_api.get_players_for_team(team.team_name)

            self.input_handler.clear_screen()

            self.tournament_menu.display_team_players(
                tournament_name = "Lið",
                team_name = team.team_name,
                players = players,
            )

            # Let user pick a player or go back
            valid_inputs = {str(i) for i in range(1, len(players) + 1)} | {"b"}
            user_input = self.input_handler.get_user_input(
                "Sláðu inn númer leikmanns til að skoða nánar eða 'b' til að fara til baka: ",
                valid_inputs,
            )

            if user_input == "b":
                in_players_menu = False
            else:
                index = int(user_input) - 1
                selected_player = players[index]
                self.run_single_player_information(selected_player)

#---------------Scoreboard--------------------------
    def run_tournament_scoreboard(self, tournament: Tournament) -> None:
        """Displays the tournament scoreboard."""
        in_tournament_scoreboard = True

        while in_tournament_scoreboard:
            self.input_handler.clear_screen()

            matches = self.logic_api.get_matches_for_tournament(tournament.tournament_id)

            width = self.input_handler.WIDTH

            print("*" * width)
            print("E-SPORTS".center(width))
            print("*" * width + "\n")

            print(f"\033[3m\033[4m\033[1mStöðutafla - {tournament.name}\033[0m\n".center(width))

            if not matches:
                print("Engir leikir skráðir fyrir þetta mót.\n")
            else:
                for match in matches:
                    status = "-> Á áætlun"
                    score_str = ""
                    if match.completed:
                        status = "-> Leik lokið"
                        score_str = f"{match.score_a} - {match.score_b}"
                    else:
                        score_str = "vs."
                    
                    print(
                        f"\033[1m{match.round} #{match.match_number} þann {match.match_date} "
                        f"klukkan: {match.match_time} [{match.server_id}]\033[0m")                   
                    line = f"  {match.team_a_name}  {score_str}  {match.team_b_name}  ({status})"
                    print(f"\033[36m{line.ljust(width)}\033[0m")
            user_input = self.input_handler.get_user_input("Sláðu inn 'b' til að fara til baka: ", {"b"})
            if user_input == "b":
                in_tournament_scoreboard = False
