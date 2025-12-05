def create_player():
        name = input("Enter player name: ")
        date_of_birth = input("Enter date of birth (YYYY-MM-DD): ")
        email = input("Enter email address: ")
        link = input("Enter social media link: ")
        handle = input("Enter gamer handle: ")
        team_name = input("Enter team name: ")
        print(f"{name}, {date_of_birth}, {email}, {link}, {handle}, {team_name}")
        return name, date_of_birth, email, link, handle, team_name

create_player()