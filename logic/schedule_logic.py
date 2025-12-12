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

            day = int(m.match_date)
            if day == 1:
                session = "Dagur 1"
            elif day == 2 and m.round == ("QF"):
                session = "Dagur 2 (morgun)"
            elif day == 2 and m.round == ("SF"):
                session = "Dagur 2 (kvöld)"
            elif day == 3:
                session = "Dagur 3"
            else:
                session = f"Dagur {day}"
                
            schedule.append({
                "match_id": m.match_id,
                "day": day,
                "session": session,
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
    




    