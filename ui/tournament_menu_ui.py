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
            for index, name in enumerate(tournament_names, start=1):
                print(f'{index}. {name}')
            print()
        print('\n' + '*' * self.WIDTH + '\n')
        #user_input = input('Sláðu inn númer móts: ')


    def display_tournament_menu(self):
        """Display menu options for the selected tournament."""
        print('*' * self.WIDTH)
        print('E-SPORTS'.center(self.WIDTH))                                                          
        print('*' * self.WIDTH + '\n')
        print('XXXX'.center(self.WIDTH) + '\n')   # XXXX á að vera heiti á móti
        print(' 1. Dagskrá')
        print(' 2. Stöðutafla')
        print(' 3. Keppnislið' + '\n')
        print('*' * self.WIDTH + '\n')
        #user_input = input('Sláðu inn númer aðgerðar: ')



    def display_tournament_schedule(self):
        """Display tournament schedule."""
        print('*' * self.WIDTH)
        print('E-SPORTS'.center(self.WIDTH))                                                          
        print('*' * self.WIDTH + '\n')
        print('Dagskrá'.center(self.WIDTH) + '\n')
        # Hér mun dagskrá mótsins vera


    def display_tournament_scoreboard(self):
        """Display tournament scoreboard."""
        print('*' * self.WIDTH)
        print('E-SPORTS'.center(self.WIDTH))                                                          
        print('*' * self.WIDTH + '\n')
        print('Stöðutafla'.center(self.WIDTH) + '\n')
        # Hér mun stöðutafla mótsins vera


    def display_tournament_teams(self):
        """Display tournament teams."""
        print('*' * self.WIDTH)
        print('E-SPORTS'.center(self.WIDTH))                                                          
        print('*' * self.WIDTH + '\n')
        print('Keppnislið'.center(self.WIDTH) + '\n')
        # Hér mun listi yfir keppnislið mótsins vera
        print('1. Team#1')   # dæmi
        print('2. Team#2')
        print('3. Team#3' + '\n')
        print('*' * self.WIDTH + '\n')
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
    