from typing import List
from logic.menu_logic import MenuLogic
from models.menu import Menu
from data.data_api import DataAPI


class LogicAPI:
    """Entry point for UI to call domain logic."""

    def __init__(self) -> None:
        data_api: DataAPI = DataAPI()
        self._menu_logic = MenuLogic(data_api)

    def list_menus(self) -> List[Menu]:
        return self._menu_logic.list_menus()

    def create_menu(self, main: str, vegan: str, soup: str) -> Menu:
        return self._menu_logic.create_menu(main, vegan, soup)
