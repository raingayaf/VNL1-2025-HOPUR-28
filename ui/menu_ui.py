from typing import List
from logic.logic_api import LogicAPI
from models.menu import Menu
from models.exceptions import ValidationError, DataAccessError


class MenuUI:
    """All console UI for menus."""

    def __init__(self, logic_api: LogicAPI) -> None:
        self._logic_api = logic_api

    # ---------- Generic prompts ----------

    def _prompt_choice(self, valid_choices: List[str]) -> str:
        """Prompt until a valid choice from valid_choices is selected."""
        valid_lower: List[str] = [c.lower() for c in valid_choices]
        while True:
            choice: str = input("> ").strip().lower()
            if choice in valid_lower:
                return choice
            joined: str = "/".join(valid_choices)
            print(f"Ógilt val, reyndu aftur ({joined}).")

    def _prompt_non_empty(self, label: str) -> str:
        """Prompt until non-empty input is given."""
        while True:
            value: str = input(f"{label}: ").strip()
            if value:
                return value
            print("Þetta má ekki vera tómt, reyndu aftur.")

    # ---------- Main menu ----------

    def show_main_menu(self) -> str:
        """Print main menu and return 'LIST', 'CREATE' or 'QUIT'."""
        print("\n==== Aðalvalmynd ====")
        print("1. Skoða matseðla")
        print("2. Búa til nýjan matseðil")
        print("q. Hætta")

        choice: str = self._prompt_choice(["1", "2", "q"])
        if choice == "1":
            return "LIST"
        if choice == "2":
            return "CREATE"
        return "QUIT"

    # ---------- List menus flow ----------

    def show_menu_list_flow(self) -> str:
        """Show list of menus and return 'BACK', 'HOME' or 'QUIT'."""
        print("\n==== Matseðlar ====")
        try:
            menus: List[Menu] = self._logic_api.list_menus()
            if not menus:
                print("Engir matseðlar til í kerfinu.")
            else:
                self._print_menu_table(menus)
        except DataAccessError as exc:
            print(f"Villa við að sækja matseðla: {exc}")

        print("\nb. Til baka")
        print("h. Heim")
        print("q. Hætta")

        choice: str = self._prompt_choice(["b", "h", "q"])
        if choice == "b":
            return "BACK"
        if choice == "h":
            return "HOME"
        return "QUIT"

    def _print_menu_table(self, menus: List[Menu]) -> None:
        """Pretty-print list of Menu objects using Menu.__str__."""
        print("---- Matseðlar ----")
        for m in menus:
            print(m)

    # ---------- Create menu flow ----------

    def create_menu_flow(self) -> str:
        """
        Interactive create-menu flow.
        Returns: 'DONE', 'BACK', 'HOME', 'QUIT'.
        """
        print("\n==== Búa til nýjan matseðil ====")
        print("(Sláðu inn 'b' fyrir til baka, 'h' fyrir heim og 'q' til að hætta.)")

        action_or_main: str = self._prompt_menu_field("Aðalréttur")
        if action_or_main in ("BACK", "HOME", "QUIT"):
            return action_or_main
        main: str = action_or_main

        action_or_vegan: str = self._prompt_menu_field("Veganréttur")
        if action_or_vegan in ("BACK", "HOME", "QUIT"):
            return action_or_vegan
        vegan: str = action_or_vegan

        action_or_soup: str = self._prompt_menu_field("Súpa")
        if action_or_soup in ("BACK", "HOME", "QUIT"):
            return action_or_soup
        soup: str = action_or_soup

        while True:
            try:
                menu: Menu = self._logic_api.create_menu(main, vegan, soup)
                print("\nMatseðill vistaður!")
                print(menu)
                return "DONE"
            except ValidationError as exc:
                print(f"\nVilla í gögnum: {exc}")
                print("1. Reyna aftur (slá inn réttina upp á nýtt)")
                print("b. Til baka")
                print("h. Heim")
                print("q. Hætta")
                choice: str = self._prompt_choice(["1", "b", "h", "q"])
                if choice == "1":
                    return self.create_menu_flow()
                if choice == "b":
                    return "BACK"
                if choice == "h":
                    return "HOME"
                return "QUIT"
            except DataAccessError as exc:
                print(f"\nVilla við vistun: {exc}")
                print("b. Til baka")
                print("h. Heim")
                print("q. Hætta")
                choice = self._prompt_choice(["b", "h", "q"])
                if choice == "b":
                    return "BACK"
                if choice == "h":
                    return "HOME"
                return "QUIT"

    def _prompt_menu_field(self, label: str) -> str:
        """
        Prompt for a menu field, supporting commands:
        'b' -> BACK, 'h' -> HOME, 'q' -> QUIT.
        Returns either the text, or one of the strings BACK/HOME/QUIT.
        """
        while True:
            value: str = input(f"{label}: ").strip()
            lower: str = value.lower()
            if lower in ("b", "h", "q"):
                if lower == "b":
                    return "BACK"
                if lower == "h":
                    return "HOME"
                return "QUIT"

            if not value:
                print("Þetta má ekki vera tómt, reyndu aftur (eða b/h/q).")
                continue

            return value
