from models.model_tournament import Tournament
from models.model_team import Team
from models.model_player import Player

class TournamentMenuUI:
    """UI class for displaying tournament-related information to general users."""

    WIDTH: int = 60

    def display_tournaments(self, tournament_names: list[str]) -> None:
        """Display all tournaments in the system to general users."""
        print('*' * self.WIDTH)
        print('E-SPORTS'.center(self.WIDTH))                                                          
        print('*' * self.WIDTH + '\n')
        print('Mót'.center(self.WIDTH) + '\n')
        if not tournament_names:
            print('Engin mót skráð í kerfið.\n')
        else:
            for number, name in enumerate(tournament_names, start=1):
                print(f'{number}. {name}')
        print('\nb: Til baka\n')
        print('*' * self.WIDTH + '\n')

    def display_tournament_menu(self, tournament_name: str) -> None:
        """Display menu options for the selected tournament."""
        print('*' * self.WIDTH)
        print('E-SPORTS'.center(self.WIDTH))                                                          
        print('*' * self.WIDTH + '\n')
        print(tournament_name.center(self.WIDTH) + '\n') 
        print(' 1. Dagskrá')
        print(' 2. Stöðutafla')
        print(' 3. Keppnislið' + '\n')
        print('b: Til baka\n')
        print('*' * self.WIDTH + '\n')

    def display_tournament_schedule(self, tournament_name: str) -> None:
        """Display tournament schedule."""
        print('*' * self.WIDTH)
        print('E-SPORTS'.center(self.WIDTH))                                                          
        print('*' * self.WIDTH + '\n')
        print(tournament_name.center(self.WIDTH)) 
        print('Dagskrá'.center(self.WIDTH) + '\n')
        # Hér mun dagskrá mótsins vera
        print('\n' + '*' * self.WIDTH + '\n')

    def display_tournament_scoreboard(self, tournament_name: str) -> None:
        """Display tournament scoreboard."""
        print('*' * self.WIDTH)
        print('E-SPORTS'.center(self.WIDTH))                                                          
        print('*' * self.WIDTH + '\n')
        print(tournament_name.center(self.WIDTH)) 
        print('Stöðutafla'.center(self.WIDTH) + '\n')
        # Hér mun stöðutafla mótsins vera
        print('\n' + '*' * self.WIDTH + '\n')

    def display_tournament_teams(self, tournament_name: str, teams: list[Team]) -> None:
        """Display tournament teams."""
        print('*' * self.WIDTH)
        print('E-SPORTS'.center(self.WIDTH))                                                          
        print('*' * self.WIDTH + '\n')
        print(tournament_name.center(self.WIDTH)) 
        print('Keppnislið'.center(self.WIDTH) + '\n')
        if not teams:
            print('Engin lið skráð á þetta mót.\n')
        else:
            for number, team in enumerate(teams, start=1):
                print(f'{number}. {team.team_name}')
        print('\nb: Til baka')
        print('\n' + '*' * self.WIDTH + '\n')

    def display_team_players(
        self,
        current_tournament: Tournament | None = None, #Since these are optional
        team: Team | None = None,
        players: list[Player] | None = None,
        captain: Player | None = None,
        tournaments: list[Tournament] | None = None,
        tournament_name: str = "",
        team_name: str = "",
    ) -> None:
        """Display players on a selected team who participate in a tournament,
        or all players in system."""

        if players is None:
            players = []
        if tournaments is None:
            tournaments = []

        print('*' * self.WIDTH)
        print('E-SPORTS'.center(self.WIDTH))
        print('*' * self.WIDTH + '\n')

        # Checks which function is utilizing the function
        if current_tournament is not None:
            title_tournament = current_tournament.name
        else:
            title_tournament = tournament_name

        if title_tournament:
            print(title_tournament.center(self.WIDTH))

        # Team title 
        if team is not None:
            title_team = team.team_name
        else:
            title_team = team_name

        if title_team:
            print(title_team.center(self.WIDTH))

        print('\nLeikmenn:')
        for i, player in enumerate(players, start=1):
            print(f'{i}. {player.handle}')

        # Checks if captain exists
        if current_tournament is not None and team is not None:
            if captain is not None:
                print(f"\nFyrirliði: {captain.handle}")
            else:
                print("\nFyrirliði finnst ekki í kerfi.")

        # Tournaments the team has played
        if current_tournament is not None and team is not None and tournaments:
            print("\nMót sem lið hefur keppt á:")
            for i, t in enumerate(tournaments, start=1):
                print(f"{i}. {t.name}")

        print('\n' + '*' * self.WIDTH + '\n')


# ------------------------------------
#        TIL AÐ PRUFU KEYRA
# ------------------------------------

if __name__ == '__main__':
    t_menu = TournamentMenuUI()

    # t_menu.display_tournaments()
    # t_menu.display_tournament_menu()
    # t_menu.display_tournament_schedule()
    # t_menu.display_tournament_scoreboard()
    # t_menu.display_tournament_teams()
    # t_menu.display_team_players()
    