import os

class InputHandler:
    """Get and validate user input for UI menus."""
    
    WIDTH = 60

    @staticmethod
    def clear_screen():
        """Clear the terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def get_menu_input(self, instruction: str, valid_input: set[str]) -> str:
        """ """
        user_input = input(instruction).strip().lower()
        if user_input in valid_input:
            return user_input
        print('\n' + 'ÓGILT VAL!'.center(self.WIDTH) + '\n') 
        return None 
    
    def get_non_empty_string(self, instruction: str) -> str:
        """ """
        while True:
            user_input = input(instruction).strip()
            if user_input != '':
                return user_input

    def get_int(self, instruction: str, min_value: int | None = None, max_value: int | None = None) -> int:
        """ """
        while True:
            user_input = input(instruction).strip()
            try:
                value = int(user_input)
            except ValueError:
                print('\nSláðu inn tölu.')
                continue
            if min_value is not None and value < min_value:
                print(f'\nFjöldinn má ekki vera minni en {min_value}!')
                continue
            if max_value is not None and value > max_value:
                print(f'\nFjöldinn má ekki vera meiri en {max_value}!')
                continue
            return value