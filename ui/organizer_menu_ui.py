class OrganizerMenuUI:
    """All organizer display menus"""

    WIDTH: int = 60

    def display_organizer_menu(self):
        """Display menu options to tournament organizer."""
        print("*" * self.WIDTH)
        print("E-SPORTS".center(self.WIDTH))
        print("*" * self.WIDTH + "\n")
        print("Velkominn mótshaldari".center(self.WIDTH) + "\n")
        print(" 1. Skrá mót")
        print(" 2. Útfæra mótsdagskrá")
        print(" 3. Upplýsingar um lið")
        print(" 4. Leikmenn á skrá"+ "\n")
        print(' b: Til baka' + '\n')

        print("*" * self.WIDTH + "\n")

    def display_tournament_options(self):
        """Display options for organizer to look at tournaments"""
        print("*" * self.WIDTH)
        print("E-SORTS".center(self.WIDTH))
        print("*" * self.WIDTH + "\n")
        print("Mótaskrá".center(self.WIDTH))
        print("1.Virk mót")
        print("2.Komandi mót")
        print("3.lokin mót")
        print("*" * self.WIDTH + "\n")
        user_input = input("sláðu inn númer aðgerðar:")

    def display_competing_teams(self):
        """Display for organizer to choose tournaments"""
        print("*" * self.WIDTH)
        print("E-SPORTS".center(self.WIDTH))
        print("*" * self.WIDTH + "\n")
        print("Mótaskrá-Virk mót".center(self.WIDTH))
        print("1.mót 1")
        print("2.mót 2")
        print("3.mót 3")
        print("*" * self.WIDTH + "\n")
        user_input = input("sláðu inn númer móts:")

    def display_competition_results(self):
        """Display for organizer to choose to put in results from match"""
        print("*" * self.WIDTH)
        print("E-SPORTS".center(self.WIDTH))
        print("*" * self.WIDTH + "\n")
        print("mót 1".center(self.WIDTH))
        print("1.færa inn úrslit")
        print("*" * self.WIDTH + "\n")
        user_input = input("sláðu inn númer aðgerðar:")

    def display_tournament_creation(self):
        """Display for organizer to regester a tournament"""
        print("*" * self.WIDTH)
        print("E-SPROTS".center(self.WIDTH))
        print("*" * self.WIDTH + "\n")
        print("Skrá mót".center(self.WIDTH))
        organizer_input = input("Sláðu inn nafn móts:")
        organizer_input = input("Sláðu inn upphafsdagsetningu:")
        organizer_input = input("Sláðu inn endadagsetningu:")
        organizer_input = input("Sláðu inn staðsetningu:")
        organizer_input = input("Sláðu inn nafn tengiliðs:")
        organizer_input = input("Sláðu inn símanúmer tengiliðs:")
        print("*" * self.WIDTH + "\n")
        organizer_input = input("S: Vista upplýsingar:")

    def display_results_input(self):
        """Display for organizer to register results from match"""
        print("*" * self.WIDTH)
        print("E-SPORTS".center(self.WIDTH))
        print("*" * self.WIDTH + "\n")
        print("Færa inn úsrslit".center(self.WIDTH))
        print("mót 1".center(self.WIDTH))
        organizer_input = input("Sláðu inn netþjóns auðkenni leiks:")
        organizer_input = input("Sláðu inn nafn sigurliðs:")
        organizer_input = input("Sláðu inn nafn tapliðs:")
        print("*" * self.WIDTH + "\n")
        organizer_input = input("S: Vista upplýsingar:")

    def display_tournament_schedule_menu(self, tournament):
        print("*" * self.WIDTH)
        print("E-SPORTS".center(self.WIDTH))
        print("*" * self.WIDTH + "\n")
        print("Útfæra mótsdagskrá".center(self.WIDTH))
        print(f"Mót: {tournament.name}".center(self.WIDTH) + "\n")
        print(" 1. Búa til dagskrá fyrir dag 1 (R16)")
        print(" 2. Búa til dagskrá fyrir dag 2 (QF)")
        print(" 3. Búa til dagskrá fyrir dag 2 (SF)")
        print(" 4. Búa til dagskrá fyrir dag 3 (Úrslitaleikur)\n")
        print(" 5. Skoða dagskrá")
        print(" 6. Færa inn úrslit leiks\n")
        print(" b: Til baka\n")
        print("*" * self.WIDTH + "\n") 

    def display_team_information1(self):
        """Display for organizer to see a teams information"""
        print("*" * self.WIDTH)
        print("E-SPORTS".center(self.WIDTH))
        print("*" * self.WIDTH + "\n")
        print("Upplýsingar um lið".center(self.WIDTH))
        print("1.Lið 1")
        print("2.Lið 2")
        print("3.Lið 3")
        print("4.Lið 4")
        print("5.Lið 5")
        print("6.Lið 6")
        print("7.Lið 7")
        print("*" * self.WIDTH + "\n")
        user_input = input("Sláðu inn númer liðs:")

    def display_team_information2(self):
        """Display for organizer to choose a player to see their information"""
        print("*" * self.WIDTH)
        print("E-SPORTS".center(self.WIDTH))
        print("*" * self.WIDTH + "\n")
        print("Upplýsingar um lið".center(self.WIDTH))
        print("lið 1".center(self.WIDTH))
        print("1.Leikmaður 1")
        print("2.Leikmaður 2")
        print("3.Leikmaður 3")
        print("4.Leikmaður 4")
        print("*" * self.WIDTH + " \n")
        user_input = input("Sláðu inn númer leikmanns:")

    def display_team_information3(self):
        """Display for organizer that shows a players information"""
        print("*" * self.WIDTH)
        print("E-SPORTS".center(self.WIDTH))
        print("*" * self.WIDTH + "\n")
        print("Upplýsingar um lið".center(self.WIDTH))
        print("Lið 1".center(self.WIDTH))
        print("Leikmaður 2")
        print("Notendanafn:xxxxx")
        print("Fullt nafn: xxxxxxx")
        print("Fæðingardagur: xxxxxxx")
        print("Heimilisfang: xxxxxxxx")
        print("Netfang: xxxx@xxxxx.is")
        print("Vefslóð: xxxxxxx")
        print("*" * self.WIDTH + "\n")
        user_input = input("Q: Til baka:")

    def display_schedule(self):
        """Display for organizer to make a schedule"""
        print("*" * self.WIDTH)
        print("E-SPORTS".center(self.WIDTH))
        print("*" * self.WIDTH + "\n")
        print("Útfæra mótsdagskrá".center(self.WIDTH))
        organizer_input = input("Sláðu inn leik/leiki:")
        organizer_input = input("Skrá keppnislið:")
        print("*" * self.WIDTH + "\n")
        organizer_input = input("S: Vista upplýsingar:")

    def display_tournament_creation_done(self):
        """Display that shows organizer that regestering a tournament worked"""
        print("*" * self.WIDTH)
        print("E-SPORTS".center(self.WIDTH))
        print("*" * self.WIDTH + "\n")
        print("Skrá mót".center(self.WIDTH)+ "\n")
        print("SKRÁNING TÓKST!".center(self.WIDTH)+ "\n")
        print("ATH! Núna þurfa fyrirliðar að skrá 16 ný lið í kerfið".center(self.WIDTH))
        print("til að hægt sé að útfæra mótsdagskrá.".center(self.WIDTH))
        print("\n" + "*" * self.WIDTH + "\n")

    def display_results_input_done(self):
        """Display that show organizer that regestering results worked"""
        print("*" * self.WIDTH)
        print("E-SPORTS".center(self.WIDTH))
        print("*" * self.WIDTH + "\n")
        print("Færa inn úrslit".center(self.WIDTH))
        print("ÚRSLIT SKRÁð")
        print("*" * self.WIDTH + "\n")
        user_input = input("Q: Til baka:")

    def display_schedule_done(self):
        print("*" * self.WIDTH)
        print("E-SPORTS".center(self.WIDTH))
        print("*" * self.WIDTH + "\n")
        print("Útfæra dagskrá".center(self.WIDTH))
        print("ÚTFÆRSLA TÓKST")
        print("*" * self.WIDTH + "\n")
        user_input = input("Q: Til baka:")

    def display_organizer_registration_menu(self):
        """Display tournament registration menu to organizer."""
        print('\n' * 2 + '*' * self.WIDTH)
        print('E-SPORTS'.center(self.WIDTH))                                                          
        print('*' * self.WIDTH + '\n')
        print("ATH! Sláðu inn '/b' til að fara til baka eða".center(self.WIDTH)) 
        print("'/q' til að hætta í skráningarferlinu.".center(self.WIDTH) + '\n')
        print('Skrá mót'.center(self.WIDTH))
