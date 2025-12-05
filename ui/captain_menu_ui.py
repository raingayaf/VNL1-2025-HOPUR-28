class CaptainMenuUI:
    
    WIDTH = 60
    
    def display_captain_menu(self):
        """Display menu options to team captain."""
        print('*' * self.WIDTH)
        print('E-SPORTS'.center(self.WIDTH))                                                          
        print('*' * self.WIDTH + '\n')
        print('Velkominn fyrirliði'.center(self.WIDTH) + '\n')
        print(' 1. Skrá lið')
        print(' 2. Upplýsingar um lið' + '\n')
        print('*' * self.WIDTH + '\n')
        user_input = input('Sláðu inn númer aðgerðar: ')
        return user_input
    

    def register_team_menu(self):
        """ """
        print('*' * self.WIDTH)
        print('E-SPORTS'.center(self.WIDTH))                                                          
        print('*' * self.WIDTH + '\n')
        print('Skrá lið'.center(self.WIDTH) + '\n')
        team_name = input('Skráðu heiti liðsins: ')
        number_of_players = int(input('skráðu fjölda leikmanna: '))
        print()


    def register_team_players_menu(self):
        """ """
        print('*' * self.WIDTH)
        print('E-SPORTS'.center(self.WIDTH))                                                          
        print('*' * self.WIDTH + '\n')
        print('XXXX'.center(self.WIDTH)) # XXXX er heitið á liðinu
        print('Skrá upplýsingar um leikmenn'.center(self.WIDTH) + '\n')

        # kannski að hafa e-ð 'Leikmaður 1'
        player_id = '' # Það er playerID í database...
        player_name = input('Skráðu fullt nafn: ')
        player_date_of_birth = input('Skráðu fæðingardag og ár: ')
        player_address = input('Skráðu heimilisfang: ')
        player_phone = input('Skráðu símanúmer: ')
        player_email = input('Skráðu netfang: ')
        player_link = input('Skráðu vefslóð: ')
        player_handle = input('Skráðu leikmanna nafn: ')
        print()


    def verify_team_captain(self):
        """ """
        print('*' * self.WIDTH)
        print('E-SPORTS'.center(self.WIDTH))                                                          
        print('*' * self.WIDTH + '\n')
        print('Upplýsingar um lið'.center(self.WIDTH) + '\n')
        team_name = input('Sláðu inn heiti á liðinu þínu: ')
        captain_handle = input('Sláðu inn leikmanna nafn þitt: ')
        print()


    def information_on_team_players(self):
        """ Display information to captain on team players."""
        print('*' * self.WIDTH)
        print('E-SPORTS'.center(self.WIDTH))                                                          
        print('*' * self.WIDTH + '\n')
        print('XXXX'.center(self.WIDTH)) # XXXX er heitið á liðinu
        print('Leikmenn'.center(self.WIDTH) + '\n')
        # Hér á að koma listi yfir leikmenn liðsins og upplýsingarnar um þá
        print('Table with team player information' + '\n') # dæmi
        print('Aðgerðir:')
        print('1. Breyta upplýsingum um einstaka leikmenn')
        print('2. Fara aftur á heimasvæði' + '\n')
        print('*' * self.WIDTH + '\n')
        user_input = input('Sláðu inn númer aðgerðar: ')
        return user_input
    

    def choosing_player_to_change(self):
        """ """
        print('*' * self.WIDTH)
        print('E-SPORTS'.center(self.WIDTH))                                                          
        print('*' * self.WIDTH + '\n')
        print('XXXX'.center(self.WIDTH)) # XXXX er heitið á liðinu
        print('Breyta leikmönnum'.center(self.WIDTH) + '\n')
        # Hér á að koma listi yfir leikmenn liðsins og upplýsingarnar um þá
        print('Table with team player information' + '\n') # dæmi
        print('*' * self.WIDTH + '\n')
        user_input = input('Sláðu inn númer leikmanns sem að þú vilt breyta upplýsingum um: ')
        return user_input
    

    def changing_player_information(self):
        """ """
        print('*' * self.WIDTH)
        print('E-SPORTS'.center(self.WIDTH))                                                          
        print('*' * self.WIDTH + '\n')
        print('XXXX'.center(self.WIDTH)) # XXXX er heitið á liðinu
        print('Breyta Leikmanni'.center(self.WIDTH) + '\n')
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
    #c_menu.register_team_menu()
    #c_menu.register_team_players_menu()
    #c_menu.verify_team_captain()
    #c_menu.information_on_team_players()
    #c_menu.choosing_player_to_change()
    #c_menu.changing_player_information()
 

