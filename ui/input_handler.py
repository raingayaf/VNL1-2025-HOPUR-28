import os
from ui import messages

class InputHandler:
    """Manages user input and validation for UI menus."""
    
    WIDTH: int = 60

    @staticmethod
    def clear_screen() -> None:
        """Clears the terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def get_user_input(self, prompt: str, valid_input: set[str]) -> str:
        """Prompts the user until a valid input is entered."""
        while True:
            try:
                user_input = input(prompt).strip().lower()
            except (KeyboardInterrupt, EOFError):
                print('\n' + messages.INVALID_INPUT.center(self.WIDTH) + '\n')
                continue

            if user_input in valid_input:
                return user_input
            print('\n' + messages.INVALID_INPUT.center(self.WIDTH) + '\n')

    def get_input_with_nav(self, prompt: str, allow_empty: bool = False):
        """ """
        while True:
            try:
                user_input = input(prompt).strip()
            except (KeyboardInterrupt, EOFError):
                print('\n' + messages.INVALID_INPUT.center(self.WIDTH) + '\n')
                continue
            if user_input.lower() == '/b':
                return 'BACK'
            if user_input.lower() == '/q':
                return 'QUIT'
            if not allow_empty and user_input == '':
                print('\n' + 'Þú verður að skrá þessar upplýsingar'.center(self.WIDTH))
                print('til að geta haldið áfram.'.center(self.WIDTH) + '\n')
                continue
            return user_input
    
    def get_non_empty_string(self, prompt: str) -> str:
        """Prompts the user until a non-empty string is entered."""
        while True:
            user_input = input(prompt).strip()
            if user_input:
                return user_input

    def get_int(self, prompt: str, min_value: int | None = None, max_value: int | None = None) -> int:
        """Prompts the user until a valid integer within allowed range is entered."""
        # held að þetta er ekki búið að vera testað fyrir CTRL+C en
        while True:
            try:
                user_input = input(prompt).strip()
            except (KeyboardInterrupt, EOFError):
                print('\n' + messages.INVALID_INPUT.center(self.WIDTH) + '\n')
                continue
            try:
                value = int(user_input)
            except ValueError:
                print('\n' + messages.INT_MUST_BE_NUMBER.center(self.WIDTH) + '\n')
                continue
            if min_value is not None and value < min_value:
                print('\n' + messages.INT_BELOW_MIN.format(min_value=min_value).center(self.WIDTH) + '\n')
                continue
            if max_value is not None and value > max_value:
                print('\n' + messages.INT_ABOVE_MAX.format(max_value=max_value).center(self.WIDTH) + '\n')
                continue
            return value
        
    def wait_for_enter(self, prompt: str = 'Ýttu á ENTER til að halda áfram.') -> None:
        """Pauses program until user presses ENTER."""
        input(prompt)

    def try_again_enter(self) -> None:
        """Tells user to press enter and try again."""
        input(messages.TRY_AGAIN.center(self.WIDTH))

    def back_home_enter(self) -> None:
        """Tells user to go back to home screen."""
        input(messages.BACK_HOME.center(self.WIDTH))

    def get_score(self) -> tuple[int, int]:
        """Validates score format and prevents input errors"""
        while True:
            score_input = input('Skráðu stig leiks á forminu, 1-4: ')
            if "-" not in score_input:
                print("Villa! Skrifaðu á forminu: 1-4.")
                continue

            left, right = score_input.split("-", 1)

            if not left.strip().isdigit() or not right.strip().isdigit():
                print("Villa! Báðir hlutir þurfa að vera tölur, t.d. 1-4.")
                continue

            a = int(left.strip())
            b = int(right.strip())

            if a == b:
                print('Jafntefli er ekki í boði')
                continue

            return a, b

