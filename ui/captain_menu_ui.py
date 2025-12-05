class CaptainMenuUI:
    """UI class for displaying menu screens and options to team captains. """
    
    WIDTH = 60
    
    def display_captain_menu(self):
        """Display menu options to team captain."""
        print('\n' * 2 + '*' * self.WIDTH)
        print('E-SPORTS'.center(self.WIDTH))                                                          
        print('*' * self.WIDTH + '\n')
        print('Velkominn fyrirliði'.center(self.WIDTH) + '\n')
        print(' 1. Skrá lið')
        print(' 2. Liðið mitt' + '\n')
        print('*' * self.WIDTH + '\n')
        user_input = input('Sláðu inn númer aðgerðar: ')
        return user_input
    

    def display_team_registration_menu(self):
        """Display team registration menu and obtain team name, captain handle and number of players."""
        print('\n' * 2 + '*' * self.WIDTH)
        print('E-SPORTS'.center(self.WIDTH))                                                          
        print('*' * self.WIDTH + '\n')
        print('Skrá lið'.center(self.WIDTH) + '\n')
        #team_id?
        team_name = input('Skráðu heiti liðsins: ')
        team_captain_handle = input('Skráðu leikmanna nafn fyrirliðans: ')
        number_of_players = int(input('skráðu fjölda leikmanna: '))
        #team_website?
        #team_logo?


    def display_player_registration_menu(self):
        """Display player registration menu and obtain information for each team player."""
        print('\n' * 2 + '*' * self.WIDTH)
        print('E-SPORTS'.center(self.WIDTH))                                                          
        print('*' * self.WIDTH + '\n')
        print('XXXX'.center(self.WIDTH)) # XXXX er heitið á liðinu
        print('Skrá upplýsingar um leikmenn'.center(self.WIDTH) + '\n')
        # kannski að hafa e-ð 'Leikmaður 1 í header?'
        #player_id --> Það er player_id í database...
        player_name = input('Skráðu fullt nafn: ')
        player_date_of_birth = input('Skráðu fæðingardag og ár: ')
        player_address = input('Skráðu heimilisfang: ')
        player_phone = input('Skráðu símanúmer: ')
        player_email = input('Skráðu netfang: ')
        player_link = input('Skráðu vefslóð: ')
        player_handle = input('Skráðu leikmanna nafn: ')
        #player_team_name --> Það er team_name í database...


    def display_captain_verification_menu(self):
        """Display team captain verification menu."""
        print('\n' * 2 + '*' * self.WIDTH)
        print('E-SPORTS'.center(self.WIDTH))                                                          
        print('*' * self.WIDTH + '\n')
        print('Liðið mitt'.center(self.WIDTH) + '\n')
        team_name = input('Sláðu inn heiti á liðinu þínu: ')
        captain_handle = input('Sláðu inn leikmanna nafn þitt: ')


    def display_team_information_menu(self):
        """Display information on team players to team captain and provide options to make changes or go back."""
        print('\n' * 2 + '*' * self.WIDTH)
        print('E-SPORTS'.center(self.WIDTH))                                                          
        print('*' * self.WIDTH + '\n')
        print('XXXX'.center(self.WIDTH)) # XXXX er heitið á liðinu
        print('Leikmenn'.center(self.WIDTH) + '\n')
        # Hér á að koma listi yfir leikmenn liðsins og upplýsingarnar um þá
        print('Tafla með upplýsingum um leikmenn' + '\n') # dæmi
        print('Aðgerðir:')
        print('1. Breyta upplýsingum um einstaka leikmenn')
        print('2. Fara aftur á heimasvæði' + '\n')
        print('*' * self.WIDTH + '\n')
        user_input = input('Sláðu inn númer aðgerðar: ')
        return user_input
    

    def display_select_player_menu(self):
        """Display information on team players and prompt user to choose player to make changes on."""
        print('\n' * 2 + '*' * self.WIDTH)
        print('E-SPORTS'.center(self.WIDTH))                                                          
        print('*' * self.WIDTH + '\n')
        print('XXXX'.center(self.WIDTH)) # XXXX er heitið á liðinu
        print('Breyta upplýsingum um leikmenn'.center(self.WIDTH) + '\n')
        # Hér á að koma listi yfir leikmenn liðsins og upplýsingarnar um þá
        print('Tafla með upplýsingum um leikmenn' + '\n') # dæmi
        print('*' * self.WIDTH + '\n')
        user_input = input('Sláðu inn númer leikmanns sem á að breyta: ')
        return user_input
    

    def display_player_information_menu(self):
        """Display information on selected player and provide options to change information."""
        print('\n' * 2 + '*' * self.WIDTH)
        print('E-SPORTS'.center(self.WIDTH))                                                          
        print('*' * self.WIDTH + '\n')
        print('XXXX'.center(self.WIDTH)) # XXXX er heitið á liðinu
        print('Breyta leikmanni'.center(self.WIDTH) + '\n')
        print('Table with player information' + '\n') # dæmi
        print('*' * self.WIDTH + '\n')
        user_input = input('Sláðu inn númer þess sem þú vilt breyta: ')
        return user_input
    
    # sé fyrir mér að notandinn fer í númer þess sem hann vill breyta, breytir því og þegar hann ýtir á enter fer hann aftur til baka og hefur valmöguleikann á að breyta einhverju öðru eða fara tilbaka eða á heimasvæði.


# ------------------------------------
#        TIL AÐ PRUFU KEYRA
# ------------------------------------

if __name__ == '__main__':
    c_menu = CaptainMenuUI()

    #c_menu.display_captain_menu()
    #c_menu.display_team_registration_menu()
    #c_menu.display_player_registration_menu()
    #c_menu.display_captain_verification_menu()
    #c_menu.display_team_information_menu()
    #c_menu.display_select_player_menu()
    c_menu.display_player_information_menu()
 

