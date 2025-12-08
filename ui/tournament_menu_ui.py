class TournamentMenuUI:
    """UI class for displaying tournament-related information to general users."""

    WIDTH = 60

    def display_tournaments(self, tournament_names: list[str]):
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


    def display_tournament_menu(self, tournament_name: str):
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
        #user_input = input('Sláðu inn númer aðgerðar: ')



    def display_tournament_schedule(self, tournament_name: str):
        """Display tournament schedule."""
        print('*' * self.WIDTH)
        print('E-SPORTS'.center(self.WIDTH))                                                          
        print('*' * self.WIDTH + '\n')
        print(tournament_name.center(self.WIDTH)) 
        print('Dagskrá'.center(self.WIDTH) + '\n')
        # Hér mun dagskrá mótsins vera
        print('\n' + '*' * self.WIDTH + '\n')


    def display_tournament_scoreboard(self, tournament_name: str):
        """Display tournament scoreboard."""
        print('*' * self.WIDTH)
        print('E-SPORTS'.center(self.WIDTH))                                                          
        print('*' * self.WIDTH + '\n')
        print(tournament_name.center(self.WIDTH)) 
        print('Stöðutafla'.center(self.WIDTH) + '\n')
        # Hér mun stöðutafla mótsins vera
        print('\n' + '*' * self.WIDTH + '\n')


    def display_tournament_teams(self, tournament_name: str):
        """Display tournament teams."""
        print('*' * self.WIDTH)
        print('E-SPORTS'.center(self.WIDTH))                                                          
        print('*' * self.WIDTH + '\n')
        print(tournament_name.center(self.WIDTH)) 
        print('Keppnislið'.center(self.WIDTH) + '\n')
        # Hér mun listi yfir keppnislið mótsins vera
        #if not teams:
            #print('Engin lið skráð á þetta mót.\n')
        #else:
            #for number, team in enumerate(teams, start=1):
                #print(f'{number}. {team.name}')
        #print('\n' + '*' * self.WIDTH + '\n')
        #ser_input = input('Sláðu inn númer liðs: ')


    def display_team_players(self):
        """Display players on a selected team who participate/d in the tournament."""
        print('*' * self.WIDTH)
        print('E-SPORTS'.center(self.WIDTH))                                                          
        print('*' * self.WIDTH + '\n')
        print('XXXXX'.center(self.WIDTH) + '\n') # XXXXXX á að vera heiti á liði
        # Hér á að koma listi yfir leikmenn liðsins
        print('1. Player#1')   # dæmi
        print('2. Player#2')
        print('3. Player#3' + '\n')
        print('*' * self.WIDTH + '\n')


# ------------------------------------
#        TIL AÐ PRUFU KEYRA
# ------------------------------------

if __name__ == '__main__':
    t_menu = TournamentMenuUI()

    #t_menu.display_tournaments()
    #t_menu.display_tournament_menu()
    #t_menu.display_tournament_schedule()
    #t_menu.display_tournament_scoreboard()
    #t_menu.display_tournament_teams()
    #t_menu.display_team_players()
    