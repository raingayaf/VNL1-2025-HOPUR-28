# ORGANIZER!

WIDTH = 60

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
    user_input = input('sláðu inn númer aðgerðar:')


def display_tournament_options(): 
    """Display options for organizer to look at tournaments""" 
    print('*' * WIDTH) 
    print('E-SORTS'.center(WIDTH))
    print('*' * WIDTH + '\n')
    print('Mótaskrá'.center(WIDTH))
    print('1.Virk mót')
    print('2.Komandi mót')
    print('3.lokin mót')
    print('*' * WIDTH + '\n')
    user_input = input('sláðu inn númer aðgerðar:')

def display_competing_teams():
    """Display for organizer to choose tournaments"""
    print('*' * WIDTH)
    print('E-SPORTS'.center(WIDTH))
    print('*' * WIDTH + '\n')
    print('Mótaskrá-Virk mót'.center(WIDTH))
    print('1.mót 1')
    print('2.mót 2')
    print('3.mót 3')
    print('*' * WIDTH + '\n')
    user_input = input('sláðu inn númer móts:')

def display_competition_results():
    """Display for organizer to choose to put in results from match"""
    print('*' * WIDTH)
    print('E-SPORTS'.center(WIDTH))
    print('*' * WIDTH + '\n')
    print('mót 1'.center(WIDTH))
    print('1.færa inn úrslit')
    print('*' * WIDTH + '\n')
    user_input = input('sláðu inn númer aðgerðar:')

def display_tournament_creation():
    """Display for organizer to regester a tournament"""
    print('*' * WIDTH)
    print('E-SPROTS'.center(WIDTH))
    print('*' * WIDTH + '\n')
    print('Skrá mót'.center(WIDTH))
    organizer_input = input('Sláðu inn nafn móts:')
    organizer_input = input('Sláðu inn upphafsdagsetningu:')
    organizer_input = input('Sláðu inn endadagsetningu:')
    organizer_input = input('Sláðu inn staðsetningu:')
    organizer_input = input('Sláðu inn nafn tengiliðs:')
    organizer_input = input('Sláðu inn símanúmer tengiliðs:')
    print('*' * WIDTH + '\n')
    organizer_input = input('S: Vista upplýsingar:')
    
def display_results_input():
    """Display for organizer to register results from match"""
    print('*' * WIDTH)
    print('E-SPORTS'.center(WIDTH))
    print('*' * WIDTH + '\n')
    print('Færa inn úsrslit'.center(WIDTH))
    print('mót 1'.center(WIDTH))
    organizer_input = input('Sláðu inn netþjóns auðkenni leiks:')
    organizer_input = input('Sláðu inn nafn sigurliðs:')
    organizer_input = input('Sláðu inn nafn tapliðs:')
    print('*' * WIDTH + '\n')
    organizer_input = input('S: Vista upplýsingar:') 

def display_team_information1():
    """Display for organizer to see a teams information"""
    print('*' * WIDTH)
    print('E-SPORTS'.center(WIDTH))
    print('*' * WIDTH + '\n')
    print('Upplýsingar um lið'.center(WIDTH))
    print('1.Lið 1')
    print('2.Lið 2')
    print('3.Lið 3')
    print('4.Lið 4')
    print('5.Lið 5')
    print('6.Lið 6')
    print('7.Lið 7')
    print('*' * WIDTH + '\n')
    user_input = input('Sláðu inn númer liðs:')

def display_team_information2():
    """Display for organizer to choose a player to see their information"""
    print('*' * WIDTH)
    print('E-SPORTS'.center(WIDTH))
    print('*' * WIDTH + '\n')
    print('Upplýsingar um lið'.center(WIDTH))
    print('lið 1'.center)
    print('1.Leikmaður 1')
    print('2.Leikmaður 2')
    print('3.Leikmaður 3')
    print('4.Leikmaður 4')
    print('*' * WIDTH + ' \n')
    user_input = input('Sláðu inn númer leikmanns:')

def display_team_information3():
    """Display for organizer that shows a players information"""
    print('*' * WIDTH)
    print('E-SPORTS'.center(WIDTH))
    print('*' * WIDTH + '\n')
    print('Upplýsingar um lið'.center(WIDTH))
    print('Lið 1'.center)
    print('Leikmaður 2')
    print('Notendanafn:xxxxx')
    print('Fullt nafn: xxxxxxx')
    print('Fæðingardagur: xxxxxxx')
    print('Heimilisfang: xxxxxxxx')
    print('Netfang: xxxx@xxxxx.is')
    print('Vefslóð: xxxxxxx')
    print('*' * WIDTH + '\n')
    user_input = input('Q: Til baka:')

def display_Scheldule():
    """Display for organizer to make a schedule"""
    print('*' * WIDTH)
    print('E-SPORTS'.center(WIDTH))
    print('*' * WIDTH + '\n')
    print('Útfæra mótsdagskrá'.center(WIDTH))
    organizer_input = input('Sláðu inn leik/leiki:')
    organizer_input = input('Skrá keppnislið:')
    print('*' * WIDTH + '\n')
    organizer_input = input('S: Vista upplýsingar:')

def display_tournament_creation_done():
    """Display that shows organizer that regestering a tournament worked"""
    print('*' * WIDTH)
    print('E-SPORTS'.center(WIDTH))
    print('*' * WIDTH + '\n')
    print('Skrá mót'.center(WIDTH))
    print('SKRÁNING TÓKST')
    print('*' * WIDTH + '\n')
    user_input = input('Q: Til baka:')

def display_results_input_done():
    """Display that show organizer that regestering results worked"""
    print('*' * WIDTH)
    print('E-SPORTS'.center(WIDTH))
    print('*' * WIDTH + '\n')
    print('Færa inn úrslit'.center(WIDTH))
    print('ÚRSLIT SKRÁð')
    print('*' * WIDTH + '\n')
    user_input = input('Q: Til baka:')

def display_schedule_done():
    print('*' * WIDTH)
    print('E-SPORTS'.center(WIDTH))
    print('*' * WIDTH + '\n')
    print('Útfæra dagskrá'.center(WIDTH))
    print('ÚTFÆRSLA TÓKST')
    print('*' * WIDTH + '\n')
    user_input = input('Q: Til baka:')

