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
    # user_input = input('Sláðu inn númer aðgerðar: ')