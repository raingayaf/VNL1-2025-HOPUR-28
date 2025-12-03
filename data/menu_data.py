import csv
import os
from typing import List
from models.menu import Menu
from models.exceptions import DataAccessError

MENU_CSV_PATH: str = "menus.csv"
FIELDNAMES: List[str] = ["id", "main_course", "vegan_course", "soup", "created_at"]


class MenuData:
    """Low-level CSV access for Menu objects."""

    def read_all(self) -> list[Menu]:
        """Read all menus from CSV and return as a list of Menu."""
        try:
            menus: list[Menu] = []
            if not os.path.exists(MENU_CSV_PATH):
                # Treat missing file as "no menus yet"
                return menus

            with open(MENU_CSV_PATH, mode="r", encoding="utf-8", newline="") as f:
                reader: csv.DictReader = csv.DictReader(f)
                for row in reader:
                    try:
                        id_value: int = int(row["id"])
                        main_course: str = row.get("main_course", "")
                        vegan_course: str = row.get("vegan_course", "")
                        soup: str = row.get("soup", "")
                        created_at: str = row.get("created_at", "")
                        menu: Menu = Menu(
                            id_value, main_course, vegan_course, soup, created_at
                        )
                        menus.append(menu)
                    except (KeyError, ValueError) as exc:
                        print(f"Warning: invalid row in CSV: {row} ({exc})")
            return menus
        except OSError as exc:
            raise DataAccessError(
                f"Ekki tókst að lesa skrána {MENU_CSV_PATH}: {exc}"
            )

    def append(self, menu: Menu) -> None:
        """Append a single Menu row to CSV."""
        try:
            file_exists: bool = os.path.exists(MENU_CSV_PATH)
            with open(MENU_CSV_PATH, mode="a", encoding="utf-8", newline="") as f:
                writer: csv.DictWriter = csv.DictWriter(f, fieldnames=FIELDNAMES)
                if not file_exists:
                    writer.writeheader()
                writer.writerow(menu.to_dict())
        except OSError as exc:
            raise DataAccessError(
                f"Ekki tókst að vista í skrána {MENU_CSV_PATH}: {exc}"
            )
