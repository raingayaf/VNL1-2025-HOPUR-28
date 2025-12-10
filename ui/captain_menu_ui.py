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
        #team_name = input('Sláðu inn heiti á liðinu þínu: ')
        #captain_handle = input('Sláðu inn leikmanna nafn þitt: ')

    def display_team_information_menu(self, team_name: str):
        """Display information on team players to team captain and provide options to make changes or go back."""
        print('\n' * 2 + '*' * self.WIDTH)
        print('E-SPORTS'.center(self.WIDTH))                                                          
        print('*' * self.WIDTH + '\n')
        print(team_name.center(self.WIDTH))
        print('Leikmenn'.center(self.WIDTH) + '\n')
        # Hér á að koma listi yfir leikmenn liðsins og upplýsingarnar um þá
        print('Tafla með upplýsingum um leikmenn' + '\n') # dæmi
        print('Aðgerðir:')
        print('1. Breyta upplýsingum um einstaka leikmenn')
        print('h: Fara aftur á heimasvæði' + '\n')
        print('*' * self.WIDTH + '\n')
        #user_input = input('Sláðu inn númer aðgerðar: ')
    

    def display_select_player_menu(self, team_name: str):
        """Display information on team players and prompt user to choose player to make changes on."""
        print('\n' * 2 + '*' * self.WIDTH)
        print('E-SPORTS'.center(self.WIDTH))                                                          
        print('*' * self.WIDTH + '\n')
        print(team_name.center(self.WIDTH))
        print('Breyta upplýsingum um leikmenn'.center(self.WIDTH) + '\n')
        # Hér á að koma listi yfir leikmenn liðsins og upplýsingarnar um þá
        print('Tafla með upplýsingum um leikmenn' + '\n') # dæmi
        print('*' * self.WIDTH + '\n')
        #user_input = input('Sláðu inn númer leikmanns sem á að breyta: ')
        

    def display_player_information_menu(self):
        """Display information on selected player and provide options to change information."""
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
 

