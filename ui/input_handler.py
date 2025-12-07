class InputHandler:
    """Deal with and validate user input for UI menus."""
    
    WIDTH = 60

    @staticmethod
    def clear_screen():
        import os
        """Clear the terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def get_menu_input(self, instruction, valid_input):
        user_input = input(instruction).strip()

        if user_input in valid_input:
            return user_input
        
        print('\n' + 'ÓGILT VAL!'.center(self.WIDTH) + '\n') 
        return None 
    