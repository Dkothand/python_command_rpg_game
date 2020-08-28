from user_commands import UserCommands

import constants


class UserInput:
    def _validate_name(self, name):
        # TODO: Add check for numbers and non-apostrophe punctuation
        is_valid = False
        if name == '':
            print("Name can't be empty!")
            return is_valid

        if len(name) > 10:
            print("Name must be 10 characters or less")
            return is_valid
        
        is_valid = True
        return is_valid 
        
    def get_player_name(self):
        ''' Gets player name from user and validates '''
        while True:
            name = input("What is your hero's name? ")
            is_valid = self._validate_name(name)

            if is_valid:
                return name

    @staticmethod
    def get_user_action():
        ''' Gets input from user and validates '''
        valid_input = UserCommands.options()
        while True:
            user_input = input(constants.ACTIONS_PROMPT)
            user_input = user_input.strip().lower()[0]

            if user_input in valid_input:
                return user_input
            print("Not a valid input")
            
