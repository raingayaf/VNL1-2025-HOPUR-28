import random
from data.tournament_data import TournamentData
from data.Team_data import TeamData

GAME_TIMES = ["08:00", "10:00", "12:00", "14:00", "16:00", "18:00", "20:00"]
MAX_GAMES_PER_DAY = 3


class Schedule:
    def __init__(self, data_api):
        self._data = data_api

    def generate_matchups(self, team_names: str) -> list[tuple[str, str]]:
        """Create matchup where no team competes against the same team twice"""
        data_list = self._data.read_all_teams()
        team_names = [row["team_name"] for row in data_list]

        matchups = []
        a = len(team_names)

        for i in range(a):
            for j in range(i + 1, a):
                matchups.append((team_names[i], team_names[j]))

        return matchups

    def assign_times(self, matchups):
        """Assign matchups at random times throughout a single day"""
        schedule = []
        day = 1
        games_today = 0

        previous_day_pairs = set()

        for team_a, team_b in matchups:
            if games_today == MAX_GAMES_PER_DAY:
                day += 1
                games_today = 0
                previous_day_pairs = {
                    (m["team_a"], m["team_b"]) for m in schedule if m["day"] == day - 1
                }

            if (team_a, team_b) in previous_day_pairs or (
                team_b,
                team_a,
            ) in previous_day_pairs:
                matchups.append((team_a, team_b))
                continue

            time_slot = random.choice(GAME_TIMES)

            schedule.append(
                {
                    "day": day,
                    "team_a": team_a,
                    "team_b": team_b,
                    "time": time_slot,
                }
            )

            games_today += 1

        return schedule
