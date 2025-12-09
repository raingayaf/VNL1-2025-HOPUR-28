import random

GAME_TIMES = ["08:00", "10:00", "12:00", "14:00", "16:00", "18:00", "20:00"]
MAX_GAMES_PER_DAY = 7


class Schedule:
    """Generates matchups and assign's times for matchup's"""

    def __init__(self, data_api):
        self._data = data_api

    def generate_matchups(self, team_names: str) -> list[tuple[str, str]]:
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

        return matchups

    def assign_times(self, matchups):
        """Assign matchups at random times throughout a single day"""
        schedule = []
        day = 1  # virtual day 1
        games_today = 0

        previous_day_pairs = (
            set()
        )  # store match pairs from previous day prevent repeat matchups

        for team_a, team_b in matchups:  # if today has maximum games, move to next day
            if games_today == MAX_GAMES_PER_DAY:
                day += 1
                games_today = 0

                # get all matchups played on the previous day
                previous_day_pairs = {
                    (m["team_a"], m["team_b"]) for m in schedule if m["day"] == day - 1
                }
            # prevent same matchup on back to back days
            if (team_a, team_b) in previous_day_pairs or (
                team_b,
                team_a,
            ) in previous_day_pairs:

                matchups.append(
                    (team_a, team_b)
                )  # make this matchup later in the list and try -
                continue  # again another day.

            time_slot = random.choice(GAME_TIMES)  # random choice for matchups

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

    def generate_schedule(self, tournament, teams):

        team_names = [team.team_name for team in teams]

        matchups = self.generate_matchups(team_names)

        schedule = self.assign_times(matchups)

        return schedule
