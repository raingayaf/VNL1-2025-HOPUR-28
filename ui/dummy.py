# prufu file

WIDTH = 60

def display_main_menu():
    """Display main menu options to user."""
    print('*' * WIDTH)
    print('E-SPORTS'.center(WIDTH))                                                          
    print('*' * WIDTH + '\n')
    print('Velkomin'.center(WIDTH) + '\n')
    print(' 1. Notandi')
    print(' 2. Fyrirliði')
    print(' 3. Mótshaldari' + '\n')
    print('*' * WIDTH + '\n')
    # user_input = input('Sláðu inn númer aðgerðar: ')

# display_main_menu() 
# --> Ef þið viljið sjá hvernig þetta prentast út 

# GENERAL USER! -HELD AÐ ALLIR GLUGGAR SÉU KOMNIR

def display_tournaments():
    """Display all tournaments in the system to general users."""
    print('*' * WIDTH)
    print('E-SPORTS'.center(WIDTH))                                                          
    print('*' * WIDTH + '\n')
    print('Mót'.center(WIDTH) + '\n')
    print(' 1. XXXX' + '\n') # XXXX á að vera heiti á móti
    print('*' * WIDTH + '\n')
    # user_input = input('Sláðu inn númer móts: ')

# display_tournaments() 
#--> Ef þið viljið sjá hvernig þetta prentast út 


def display_tournament_menu():
    """Display menu options for the selected tournament."""
    print('*' * WIDTH)
    print('E-SPORTS'.center(WIDTH))                                                          
    print('*' * WIDTH + '\n')
    print('XXXX'.center(WIDTH) + '\n')   # XXXX á að vera heiti á móti
    print(' 1. Dagskrá')
    print(' 2. Stöðutafla')
    print(' 3. Keppnislið' + '\n')
    print('*' * WIDTH + '\n')
    # user_input = input('Sláðu inn númer aðgerðar: ')

# display_tournament_menu() 
#--> Ef þið viljið sjá hvernig þetta prentast út


def display_tournament_schedule():
    """Display tournament schedule."""
    print('*' * WIDTH)
    print('E-SPORTS'.center(WIDTH))                                                          
    print('*' * WIDTH + '\n')
    print('Dagskrá'.center(WIDTH) + '\n')
    # Hér mun dagskrá mótsins vera

def display_tournament_scoreboard():
    """Display tournament scoreboard."""
    print('*' * WIDTH)
    print('E-SPORTS'.center(WIDTH))                                                          
    print('*' * WIDTH + '\n')
    print('Stöðutafla'.center(WIDTH) + '\n')
    # Hér mun stöðutafla mótsins vera


def display_tournament_teams():
    """Display tournament teams."""
    print('*' * WIDTH)
    print('E-SPORTS'.center(WIDTH))                                                          
    print('*' * WIDTH + '\n')
    print('Keppnislið'.center(WIDTH) + '\n')
    # Hér mun listi yfir keppnislið mótsins vera
    print('1. Team#1')   # dæmi
    print('2. Team#2')
    print('3. Team#3' + '\n')
    print('*' * WIDTH + '\n')
    # user_input = input('Sláðu inn númer liðs: ')


def display_team_players():
    """Display players on a selected team who participate/d in the tournament."""
    print('*' * WIDTH)
    print('E-SPORTS'.center(WIDTH))                                                          
    print('*' * WIDTH + '\n')
    print('XXXXX'.center(WIDTH) + '\n') # XXXXXX á að vera heiti á liði
    # Hér á að koma listi yfir leikmenn liðsins
    print('1. Player#1')   # dæmi
    print('2. Player#2')
    print('3. Player#3' + '\n')
    print('*' * WIDTH + '\n')

# ORGANIZER!

def display_organizer_menu():
    """Display menu options to tournament organizer."""
    print('*' * WIDTH)
    print('E-SPORTS'.center(WIDTH))                                                          
    print('*' * WIDTH + '\n')
    print('Velkominn mótshaldari'.center(WIDTH) + '\n')
    print(' 1. Skrá mót')
    print(' 2. Útfæra mótsdagskrá')
    print(' 3. Upplýsingar um lið' + '\n')
    print('*' * WIDTH + '\n')
    # user_input = input('Sláðu inn númer aðgerðar: ')

# TEAM CAPTAIN!

def display_captain_menu():
    """Display menu options to team captain."""
    print('*' * WIDTH)
    print('E-SPORTS'.center(WIDTH))                                                          
    print('*' * WIDTH + '\n')
    print('Velkominn mótshaldari'.center(WIDTH) + '\n')
    print(' 1. Skrá lið')
    print(' 2. Skoða lið' + '\n')
    print('*' * WIDTH + '\n')
    # user_input = input('Sláðu inn númer aðgerðar: ')                               
                                 



