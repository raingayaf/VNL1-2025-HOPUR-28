class TournamentLogic:
    # TODO: búa til DataApi

    def __init__(self):
        pass

    def __str__(self):
        pass

    def create_team():
        """Smá menu til að' búa til lið, nafn fyrir það og bæta við 3-5 spilara  
        """
        team_name = input("Enter team name: ")
        print(f"Created team with team name '{team_name}'")

        players: list = []

        while len(players) < 5: 
            player_name = input(f"Enter player name {len(players+1)} (or press Enter to finish): ")

            if player_name == "":
                break

            players.append(player_name)
            print(f"Added {player_name} to Team {team_name}.")
            print(f"Players in Team {team_name}: {players}")
        
        if len(players) < 3: 
            print("A team must have at least 3 players")
            return
        else: 
            print(f"Team {team_name} registered with {len(players)} players.")
# create_team()            

    def admin_processes(self):
        pass

    def create_match(self):
        pass

    def create_player(self):
        pass

    def create_tournament(self):
        pass
