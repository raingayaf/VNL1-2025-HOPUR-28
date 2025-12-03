from typing import List
from datetime import datetime
from data.data_api import DataAPI
from models.menu import Menu
from models.exceptions import ValidationError


class MenuLogic:
    """Business logic for menus."""

    _data_api: DataAPI

    def __init__(self, data_api: DataAPI) -> None:
        self._data_api = data_api

    def list_menus(self) -> List[Menu]:
        """Return all menus."""
        return self._data_api.read_all_menus()

    def create_menu(self, main: str, vegan: str, soup: str) -> Menu:
        """
        Validate fields, create Menu, save via DataAPI, and return it.
        May raise ValidationError or DataAccessError.
        """
        main_stripped: str = main.strip()
        vegan_stripped: str = vegan.strip()
        soup_stripped: str = soup.strip()

        self._validate_menu_fields(main_stripped, vegan_stripped, soup_stripped)

        menus: List[Menu] = self._data_api.read_all_menus()
        max_id: int = 0
        for m in menus:
            if m.id > max_id:
                max_id = m.id
        next_id: int = max_id + 1

        created_at: str = datetime.now().isoformat(timespec="seconds")

        menu: Menu = Menu(next_id, main_stripped, vegan_stripped, soup_stripped, created_at)
        self._data_api.save_menu(menu)
        return menu

    def _validate_menu_fields(self, main: str, vegan: str, soup: str) -> None:
        """Raise ValidationError if any field is invalid."""
        if not main:
            raise ValidationError("Aðalréttur má ekki vera tómur.")
        if not vegan:
            raise ValidationError("Veganréttur má ekki vera tómur.")
        if not soup:
            raise ValidationError("Súpa má ekki vera tóm.")

        if len(main) > 100:
            raise ValidationError("Aðalréttur er of langur (max 100 stafir).")
        if len(vegan) > 100:
            raise ValidationError("Veganréttur er of langur (max 100 stafir).")
        if len(soup) > 100:
            raise ValidationError("Súpa er of löng (max 100 stafir).")
