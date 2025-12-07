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
    