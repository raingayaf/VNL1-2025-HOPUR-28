import random

GAME_TIMES = ["08:00", "10:00", "12:00", "14:00", "16:00", "18:00", "20:00"]
MAX_GAMES_PER_DAY = 7


class Schedule:
    """Generates matchups and assign's times for matchup's"""

    def __init__(self, data_api):
        self._data = data_api

    def generate_matchups(self, team_names: list[str]) -> list[tuple[str, str]]:
        """Create matchup where no team competes against the same team twice(including against itself)"""
        # gets names of every team in tournament

        matchups = []
        a = len(team_names)

        for i in range(a):
            for j in range(i + 1, a):
                matchups.append(
                    (team_names[i], team_names[j])
                )  # makes sure every matchup is -
            # correct i.e no team competes against the same team twice
        random.shuffle(matchups)
        return matchups

    def assign_times(self, matchups):
        """Assign matchups at random times throughout a single day"""
        schedule = []
        day = 1
        games_today = 0

        for team_a, team_b in matchups:
            if games_today == MAX_GAMES_PER_DAY:
                day += 1
                games_today = 0

            time_slot = random.choice(GAME_TIMES)

            schedule.append({
                "day": day,
                "team_a": team_a,
                "team_b": team_b,
                "time": time_slot,
            })

            games_today += 1

        return schedule

    def generate_schedule(self, teams):

        team_names = [team.team_name for team in teams]

        matchups = self.generate_matchups(team_names)

        schedule = self.assign_times(matchups)

        return schedule
