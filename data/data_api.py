from typing import List
from data.menu_data import MenuData
from models.menu import Menu


class DataAPI:
    """Data facade used by logic layer."""

    def __init__(self) -> None:
        self._menu_data = MenuData()

    def read_all_menus(self) -> List[Menu]:
        return self._menu_data.read_all()

    def save_menu(self, menu: Menu) -> None:
        self._menu_data.append(menu)
