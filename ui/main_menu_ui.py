class MainMenuUI:
    """UI class for displaying the main menu of the E-SPORT system."""
    
    WIDTH = 60

    def display_main_menu(self): 
        """Display main menu options to user."""
        print('*' * self.WIDTH)
        print('E-SPORTS'.center(self.WIDTH))                                                          
        print('*' * self.WIDTH + '\n')
        print('Velkomin'.center(self.WIDTH) + '\n')
        print(' 1. Notandi')
        print(' 2. Fyrirliði')
        print(' 3. Mótshaldari' + '\n')
        print('*' * self.WIDTH + '\n')

#main_menu = MainMenuUI()
#main_menu.display_main_menu()
# --> Ef þið viljið sjá hvernig þetta prentast út 