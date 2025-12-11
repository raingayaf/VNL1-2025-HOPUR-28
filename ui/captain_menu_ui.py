class CaptainMenuUI:
    """UI class for displaying menu screens and options to team captains. """
    
    WIDTH: int = 60

    def display_captain_menu(self):
        """Display menu options to team captain."""
        print('\n' * 2 + '*' * self.WIDTH)
        print('E-SPORTS'.center(self.WIDTH))                                                          
        print('*' * self.WIDTH + '\n')
        print('Velkominn fyrirliði'.center(self.WIDTH) + '\n')
        print(' 1. Skrá lið')
        print(' 2. Liðið mitt' + '\n')
        print(' b: Til baka' + '\n')
        print('*' * self.WIDTH + '\n')

    def display_team_registration_menu(self):
        """Display team registration menu to captain."""
        print('\n' * 2 + '*' * self.WIDTH)
        print('E-SPORTS'.center(self.WIDTH))                                                          
        print('*' * self.WIDTH + '\n')
        print("ATH! Sláðu inn 'b' til að fara til baka eða".center(self.WIDTH)) 
        print("'q' til að hætta í skráningarferlinu.".center(self.WIDTH) + '\n')
        print('Skrá lið'.center(self.WIDTH))

    def display_player_registration_menu(self, team_name: str, player_index: int):
        """Display player registration menu."""
        print('\n' * 2 + '*' * self.WIDTH)
        print('E-SPORTS'.center(self.WIDTH))                                                          
        print('*' * self.WIDTH + '\n')
        print("ATH! Sláðu inn 'b' til að fara til baka eða".center(self.WIDTH)) 
        print("'q' til að hætta í skráningarferlinu.".center(self.WIDTH) + '\n')
        print(team_name.center(self.WIDTH))
        subhead = f'Skrá upplýsingar um leikmann {player_index}'
        print(subhead.center(self.WIDTH) + '\n')

    def display_captain_verification_menu(self):
        """Display team captain verification menu."""
        print('\n' * 2 + '*' * self.WIDTH)
        print('E-SPORTS'.center(self.WIDTH))                                                          
        print('*' * self.WIDTH + '\n')
        print('Liðið mitt'.center(self.WIDTH) + '\n')

    def display_team_players_menu(self, team_name: str):
        """Display team players to team captain."""
        print('\n' * 2 + '*' * self.WIDTH)
        print('E-SPORTS'.center(self.WIDTH))                                                          
        print('*' * self.WIDTH + '\n')
        print(team_name.center(self.WIDTH))
        print('Leikmenn:'.center(self.WIDTH))

    def display_player_information_menu(self, selected_player: str):
        """Display information on selected team player to team captain."""
        print('\n' * 2 + '*' * self.WIDTH)
        print('E-SPORTS'.center(self.WIDTH))                                                          
        print('*' * self.WIDTH + '\n')
        title = f"Upplýsingar um {selected_player}"
        print(title.center(self.WIDTH) + '\n')
        

    def display_players(self):
        """Display players in selected team."""
        print('\n' * 2 + '*' * self.WIDTH)
        print('E-SPORTS'.center(self.WIDTH))                                                          
        print('*' * self.WIDTH + '\n')
        print('XXXX'.center(self.WIDTH)) # XXXX er heitið á liðinu
        print('Breyta leikmanni'.center(self.WIDTH) + '\n')
        print('Table with player information' + '\n') # dæmi
        print('*' * self.WIDTH + '\n')
        #user_input = input('Sláðu inn númer þess sem þú vilt breyta: ')
    

    # sé fyrir mér að notandinn fer í númer þess sem hann vill breyta, breytir því og þegar hann ýtir á enter fer hann aftur til baka og hefur valmöguleikann á að breyta einhverju öðru eða fara tilbaka eða á heimasvæði.


# ------------------------------------
#        TIL AÐ PRUFU KEYRA
# ------------------------------------

if __name__ == "__main__":
    c_menu = CaptainMenuUI()

    #c_menu.display_captain_menu()
    #c_menu.display_team_registration_menu()
    #c_menu.display_player_registration_menu()
    #c_menu.display_captain_verification_menu()
    #c_menu.display_team_information_menu()
    #c_menu.display_select_player_menu()
    #c_menu.display_player_information_menu()
 

