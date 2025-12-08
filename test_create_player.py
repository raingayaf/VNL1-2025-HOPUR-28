from data.data_api import DataApi
from logic.player_logic import PlayerLogic
from models.exceptions import ValidationError


def test_create_player():
    data_api = DataApi()
    player_logic = PlayerLogic(data_api)

    print("=== Testing create_player ===")

    try:
        new_player = player_logic.create_player(
            name="Test Player 1",
            date_of_birth="1990-01-01",
            address="Test Street 1",
            phone="1234567",
            email="test@example.com",
            link="http://example.com",
            handle="TestHandle999",        
            team_name="SegFault Spartans",  
        )

        print("Player created successfully:")
        print(vars(new_player))

    except ValidationError as e:
        print("Validation error:", e)

    # Show all players currently in the CSV
    print("\nPlayers currently in players.csv:")
    all_players = data_api.read_all_players()
    for p in all_players:
        print(f"- {p.player_id}: {p.name} ({p.handle}) -> {p.team_name}")


if __name__ == "__main__":
    test_create_player()
