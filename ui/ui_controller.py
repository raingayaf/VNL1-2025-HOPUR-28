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

    def run_tournament_scoreboard(self, tournament: Tournament) -> None:
        """Displays the tournament scoreboard until the user chooses to return to the previous menu."""
        in_tournament_scoreboard = True

        while in_tournament_scoreboard:
            self.input_handler.clear_screen()
            self.tournament_menu.display_tournament_scoreboard(tournament.name)
            user_input = self.input_handler.get_user_input("Sláðu inn 'b' til að fara til baka: ", {"b"})
            if user_input == "b":
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
            self.input_handler.clear_screen()
            self.tournament_menu.display_team_players(
                tournament.name, team.team_name, players
            )
            user_input = self.input_handler.get_user_input("Sláðu inn númer liðs eða farðu til baka: ", {"b"})
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
                print(f"Skráðu leikmanna nafn fyrirliðans: {captain_handle}")
            if number_of_players:
                print(f"Skráðu fjölda leikmanna (3-5): {number_of_players}")
            if team_website or step == 5:
                print(
                    "\n"
                    + "Valkvæðar upplýsingar um lið.".center(self.input_handler.WIDTH)
                )
                print("Ýtir á ENTER til að sleppa.".center(self.input_handler.WIDTH))
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
                if self.logic_api.team_name_exists(user_input):
                    team_exists_message = f"Liðið '{user_input}' er nú þegar á skrá!"
                    print("\n" + team_exists_message.center(self.input_handler.WIDTH))
                    print(
                        "Vinsamlegast veldu nafn sem er ekki í notkun.".center(
                            self.input_handler.WIDTH
                        )
                    )
                    input(
                        "Ýttu á ENTER og reyndu aftur.".center(self.input_handler.WIDTH)
                    )
                    continue
                team_name = user_input
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
                if self.logic_api.handle_exists(user_input):
                    handle_exists_message = (
                        f"Leikmanna nafnið '{user_input}' er nú þegar á skrá."
                    )
                    print("\n" + handle_exists_message.center(self.input_handler.WIDTH))
                    print(
                        "Vinsamlegast veldu leikmanna nafn (handle) sem er ekki í notkun.".center(
                            self.input_handler.WIDTH
                        )
                    )
                    input(
                        "Ýttu á ENTER og reyndu aftur.".center(self.input_handler.WIDTH)
                    )
                    continue
                captain_handle = user_input
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
                        "\nÓgilur innsláttur! Vinsamlegast sláðu inn heiltölu frá 3-5.".center(
                            self.input_handler.WIDTH
                        )
                    )
                    input(
                        "Ýttu á ENTER og reyndu aftur.".center(self.input_handler.WIDTH)
                    )
                    continue
                number = int(user_input)
                if number < 3:
                    num_below = f"Fjöldinn má ekki vera minni en 3!"
                    print("\n" + num_below.center(self.input_handler.WIDTH))
                    input(
                        "Ýttu á ENTER og reyndu aftur.".center(self.input_handler.WIDTH)
                    )
                    continue
                if number > 5:
                    num_above = f"Fjöldinn má ekki vera meiri en 5!"
                    print("\n" + num_above.center(self.input_handler.WIDTH))
                    input(
                        "Ýttu á ENTER og reyndu aftur.".center(self.input_handler.WIDTH)
                    )
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
                print("Ýtir á ENTER til að sleppa.".center(self.input_handler.WIDTH))
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
                team_website = user_input
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
                team_logo = user_input
                step = 6
                continue

            # Step 6 - Player registration
            if step == 6:
                players_on_team = self.run_player_registration(
                    team_name, number_of_players
                )

                if players_on_team == "QUIT":
                    in_team_registration = False
                    continue
                if players_on_team == "BACK":
                    team_logo = ""
                    step = 5
                    continue

                player_handles = [player["handle"] for player in players_on_team]

                if captain_handle not in player_handles:
                    print("Fyrirliði þarf að vera einn af leikmönnunum.")
                    input("Ýttu á ENTER til að halda áfram.")
                    step = 2
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
                        registered_team_players=players_on_team,
                        website=team_website,
                        logo=team_logo,
                    )
                    print(f"Liðið '{team_name}' hefur verið skráð!")
                    input("Ýttu á ENTER til að fara aftur á heimasvæðið.")
                    in_team_registration = False
                    continue
                except ValidationError:
                    print(f"Óvænt villa við skráningu liðs!")
                    input("Ýttu á ENTER til að reyna aftur.")
                    in_team_registration = False
                    continue

    def run_player_registration(self, team_name: str, number_of_players: int):
        """Runs registration on each player in team (collects data)."""
        in_player_registration = True
        current_player = 1
        players_on_team: list[dict[str, str]] = []

        while in_player_registration:
            if current_player > number_of_players:
                break

            player_name = ""
            player_date_of_birth = ""
            player_address = ""
            player_phone = ""
            player_email = ""
            player_link = ""
            player_handle = ""

            # If information already collected
            if current_player <= len(players_on_team):
                existing = players_on_team[current_player - 1]
                player_name = existing["name"]
                player_date_of_birth = existing["date_of_birth"]
                player_address = existing["address"]
                player_phone = existing["phone"]
                player_email = existing["email"]
                player_link = existing["link"]
                player_handle = ""
                step = 7
            else:
                step = 1

            while step <= 7 and in_player_registration:
                
                self.input_handler.clear_screen()
                self.captain_menu.display_player_registration_menu(team_name, current_player)

                # Shows previous entered input when user goes back
                if player_name:
                    print(f"Skráðu fullt nafn: {player_name}")
                if player_date_of_birth:
                    print(f"Skráðu fæðingardag og ár: {player_date_of_birth}")
                if player_address:
                    print(f"Skráðu heimilisfang: {player_address}")
                if player_phone:
                    print(f"Skráðu símanúmer: {player_phone}")
                if player_email:
                    print(f"Skráðu netfang: {player_email}")
                if player_link:
                    print(f"Skráðu vefslóð: {player_link}")
                if player_handle:
                    print(f"Skráðu leikmanna nafn: {player_handle}")

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
                    player_name = user_input
                    step = 2
                    continue

                # Step 2 - Date of birth
                if step == 2:
                    user_input = self.input_handler.get_input_with_nav(
                        "Skráðu fæðingardag og ár: "
                    )
                    if user_input == "QUIT":
                        return "QUIT"
                    if user_input == "BACK":
                        player_name = ""
                        step = 1
                        continue
                    player_date_of_birth = user_input
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
                    player_address = user_input
                    step = 4
                    continue

                # Step 4 - Phone
                if step == 4:
                    user_input = self.input_handler.get_input_with_nav(
                        "Skráðu símanúmer: "
                    )
                    if user_input == "QUIT":
                        return "QUIT"
                    if user_input == "BACK":
                        player_address = ""
                        step = 3
                        continue
                    player_phone = user_input
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
                    player_email = user_input
                    step = 6
                    continue

                # Step 6 - Link
                if step == 6:
                    user_input = self.input_handler.get_input_with_nav(
                        "Skráðu vefslóð: ", allow_empty=True
                    )
                    if user_input == "QUIT":
                        return "QUIT"
                    if user_input == "BACK":
                        player_email = ""
                        step = 5
                        continue
                    player_link = user_input
                    step = 7
                    continue

                # Step 7 - Handle
                if step == 7:
                    user_input = self.input_handler.get_input_with_nav(
                        "Skráðu leikmanna nafn: "
                    )
                    if user_input == "QUIT":
                        return "QUIT"
                    if user_input == "BACK":
                        player_link = ""
                        step = 6
                        continue
                    if self.logic_api.handle_exists(user_input):
                        handle_exists_message = (
                            f"Leikmanna nafnið '{user_input}' er nú þegar á skrá."
                        )
                        print("\n" + handle_exists_message.center(self.input_handler.WIDTH))
                        print(
                            "Vinsamlegast veldu leikmanna nafn (handle) sem er ekki í notkun.".center(
                                self.input_handler.WIDTH
                            )
                        )
                        input(
                            "Ýttu á ENTER og reyndu aftur.".center(self.input_handler.WIDTH)
                        )
                        continue
                    player_handle = user_input

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
            elif user_input !="b":
                print()
            choice = int(user_input)
            if choice == 1:
                field_name = "name"
                prompt = "Skráðu nýtt nafn: "
            elif choice == 2:
                field_name = "date_of_birth"
                prompt = "Skráðu nýjan fæðingardag: "
            elif choice == 3:
                field_name = "address"
                prompt = "Skráðu nýtt heimilisfang: "
            elif choice == 4:
                field_name = "phone"
                prompt = "Skráðu nýtt símanúmer: "
            elif choice == 5:
                field_name = "email"
                prompt = "Skráðu nýtt netfang: "
            elif choice == 6:
                field_name = "link"
                prompt = "Skráðu nýja vefslóð: "
            else:
                continue

            new_value = input(prompt).strip()

            setattr(player, field_name, new_value)

            try:
                self.logic_api.update_player(player)
                print("\n" + "Upplýsingunum hefur verið breytt.".center(WIDTH))
            except Exception as exc:
                error_updating = f"Tókst ekki að uppfæra leikmann: {exc}"
                print("\n"+ error_updating.center(WIDTH))
            input("Ýttu á ENTER til að halda áfram.".center(WIDTH))



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
                self.run_display_menu()

            elif organizer_input == "3":
                self.run_all_teams_view()
            # See all available players and info
            elif organizer_input == "4":
                self.run_all_players_view()
            elif organizer_input == "b":

                in_orginizer_menu = False

    def run_display_menu(self):
        in_display_menu = True

        tournaments = self.logic_api.get_all_tournaments()
        teams = self.logic_api.get_all_teams()
        tournament = tournaments[0]
        schedule = self.logic_api.generate_schedule(teams)

        while in_display_menu:
            self.input_handler.clear_screen()
            self.schedule_menu.displey_schedule_menu(tournament, teams)

            organizer_input = self.input_handler.get_user_input(
                messages.ACTION_OR_BACK_PROMPT, {"b", "s"}
            )

            if organizer_input == "s":
                self.logic_api.organizer_save_schedule(tournament, schedule)
                print("Dagskrá vistuð!")
                self.input_handler.wait_for_enter()
            elif organizer_input == "b":
                in_display_menu = False

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

