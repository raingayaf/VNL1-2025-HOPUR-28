from data.data_api import DataApi
from logic.match_logic import MatchLogic
from models.exceptions import ValidationError


def test_create_match():
    # ✅ ONE DataApi instance, using the default base path
    data = DataApi()               # <--- important: no "data_base" here
    logic = MatchLogic(data)

    print("Teams visible to MatchLogic:")
    for t in data.read_all_teams():
        print("-", repr(t.team_name))

    try:
        new_match = logic.create_match(
            tournament_id=1,
            round="TestRound",
            match_number=99,
            team_a_name="SegFault Spartans",
            team_b_name="CacheHit Crusaders",
            match_date="2025-12-25",
            match_time="12:00",
            server_id="SRV-TEST",
        )
        print("Match created successfully:")
        print(new_match.__dict__)
    except ValidationError as e:
        print("Validation error:", e)


if __name__ == "__main__":
    test_create_match()
