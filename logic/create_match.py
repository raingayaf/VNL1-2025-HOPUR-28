def create_match():
    match_id = input("Enter match ID: ")
    tournament_id = input("Enter tournament ID: ")
    match_number = input("Enter match number: ")
    team_name_a = input("Enter name of Team A: ")
    team_name_b = input("Enter name of Team B: ")
    match_date = input("Enter date of match (formatted YYYY-MM-DD): ")
    match_time = input("Enter time of match (formatted as for example 00:00): ")
    server_id = input("Enter server ID: ")
    score_a = input("Enter Team A's score: ")
    score_b = input("Enter Team B's score: ")
    winner_team_name = input("Enter the winning team's name: ")
    completed = input("Veit ekki hvað þetta á að vera: ")
    print(f"{match_id}, {tournament_id}, {match_number}, {team_name_a}, {team_name_b}, {match_date}, {match_time}, {server_id}, {score_a}, {score_b}, {winner_team_name}, {completed}")
    return match_id, tournament_id, match_number, team_name_a, team_name_b, match_date, match_time, server_id, score_a, score_b, winner_team_name, completed 

create_player()