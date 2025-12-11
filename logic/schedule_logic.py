import random

GAME_TIMES = ["08:00", "10:00", "12:00", "14:00", "16:00", "18:00", "20:00"]
MAX_GAMES_PER_DAY = len(GAME_TIMES)


class ScheduleLogic:
    """Generates matchups and assign's times for matchup's"""

    def __init__(self, data_api):
        self._data_api = data_api

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

            time_slot = GAME_TIMES[games_today]

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
    
    def organizer_save_schedule(self, tournament, schedule: list[dict]):
        rows_to_save = []
        for match in schedule:
            rows_to_save.append({
                "tournament_name": tournament.name,
                "day": match["day"],
                "time": match["time"],
                "team_a": match["team_a"],
                "team_b": match["team_b"],
            })

        return self._data_api.save_schedule(rows_to_save)

    def find_saved_schedule(self, tournament):
        all_rows = self._data_api.load_schedule()

        schedule = []
        for row in all_rows:
            if row["tournament_name"] != tournament.name:
                continue
        
        schedule.append({
            "day": int(row["day"]),
            "time": row["time"],
            "team_a": row["team_a"],
            "team_b": row["team_b"],
        })
    
        def schedule_sort_key(row):
            return row["day"], row["time"]
        
        schedule.sort(key=schedule_sort_key)

        return schedule