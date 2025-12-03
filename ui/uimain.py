from ui.menu_ui import MenuUI
from logic.logic_api import LogicAPI


class UIMain:
    """Top-level UI state machine."""

    current_screen: str

    def __init__(self) -> None:
        logic_api = LogicAPI()
        self._menu_ui = MenuUI(logic_api)
        self.current_screen = "MAIN_MENU"

    def run(self) -> None:
        """Main loop handling navigation."""
        while True:
            if self.current_screen == "MAIN_MENU":
                action: str = self._menu_ui.show_main_menu()
                if action == "LIST":
                    self.current_screen = "MENU_LIST"
                elif action == "CREATE":
                    self.current_screen = "MENU_CREATE"
                elif action == "QUIT":
                    print("Bless!")
                    break

            elif self.current_screen == "MENU_LIST":
                action = self._menu_ui.show_menu_list_flow()
                if action in ("BACK", "HOME"):
                    self.current_screen = "MAIN_MENU"
                elif action == "QUIT":
                    print("Bless!")
                    break

            elif self.current_screen == "MENU_CREATE":
                action = self._menu_ui.create_menu_flow()
                if action in ("DONE", "BACK", "HOME"):
                    self.current_screen = "MAIN_MENU"
                elif action == "QUIT":
                    print("Bless!")
                    break

            else:
                print(f"Óþekkt skjár: {self.current_screen}, fer heim.")
                self.current_screen = "MAIN_MENU"
