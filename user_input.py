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
        
    def _validate_user_action(self, action):
        valid_input = UserCommands.options()
        is_valid = False

        if action == '':
            print("Not a valid input")
            return is_valid

        user_input = action.strip().lower()[0]
        if user_input in valid_input:
            is_valid = True
            return is_valid
        print("Not a valid input")

    def get_player_name(self):
        ''' Gets player name from user and validates '''
        while True:
            name = input("What is your hero's name? ")
            if self._validate_name(name):
                return name

    def get_user_action(self):
        ''' Gets input from user and validates '''
        while True:
            user_input = input(constants.ACTIONS_PROMPT)
            if self._validate_user_action(user_input):
                return user_input            
