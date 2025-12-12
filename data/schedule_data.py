# import csv
# from pathlib import Path

# SCHEDULE_FILE = Path("data/data_base/schedules.csv")

# class ScheduleData:
#     def write_schedule_csv(self, rows):
#         """Overwrite the schedule CSV with given rows"""
#         SCHEDULE_FILE.parent.mkdir(parents=True, exist_ok=True)
#         fieldnames = ["tournament_name", "day", "time", "team_a", "team_b"]

#         with SCHEDULE_FILE.open(mode="w", newline="", encoding="utf-8") as file:
#             writer = csv.DictWriter(file, fieldnames=fieldnames)
#             writer.writeheader()
#             writer.writerows(rows)
    
#     def read_schedule_csv(self):
#         """Read all schedule rows"""
#         if not SCHEDULE_FILE.exists():
#             return []
        
#         with SCHEDULE_FILE.open(mode="r", newline="", encoding="utf-8") as file:
#             reader = csv.DictReader(file)
#             return list(reader)