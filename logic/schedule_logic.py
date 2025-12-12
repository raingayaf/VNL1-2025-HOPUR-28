import random

class ScheduleLogic:
    """Generates matchups and assign's times for matchup's"""

    def __init__(self, data_api):
        self._data_api = data_api

    def build_schedule_for_tournament(self, tournament) -> list[dict]:
        """Return a list of dicts representing the schedule for a tournament."""
        all_matches = self._data_api.read_all_matches()

        schedule: list[dict] = []
        for m in all_matches:
            if m.tournament_id != tournament.tournament_id:
                continue

            if m.round == "R16":
                day = 1
            elif m.round in ("QF", "SF"):
                day = 2
            else:
                day = 3
            
            schedule.append({
                "match_id": m.match_id,
                "day": day,
                "time": m.match_time,
                "team_a": m.team_a_name,
                "team_b": m.team_b_name,
                "match_number": m.match_number,
                "round": m.round,
                "completed": m.completed,
            })
        

        def schedule_sort_key(row):
            return (row["day"], row["time"])
    
        schedule.sort(key=schedule_sort_key)
        return schedule
    