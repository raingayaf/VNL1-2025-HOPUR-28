import os
from ui import messages

class InputHandler:
    """Manages user input and validation for UI menus."""
    
    WIDTH = 60

    @staticmethod
    def clear_screen():
        """Clear the terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def get_user_input(self, prompt: str, valid_input: set[str]) -> str:
        """Prompts the user until a valid input is enterd."""
        while True:
            user_input = input(prompt).strip().lower()
            if user_input in valid_input:
                return user_input
            print('\n' + messages.INVALID_INPUT.center(self.WIDTH) + '\n') 
    
    def get_non_empty_string(self, prompt: str) -> str:
        """Prompts the user until a non-empty string is entered."""
        while True:
            user_input = input(prompt).strip()
            if user_input != '':
                return user_input

    def get_int(self, prompt: str, min_value: int | None = None, max_value: int | None = None) -> int:
        """Prompts the user until a valid integer within allowed range is entered."""
        while True:
            user_input = input(prompt).strip()
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