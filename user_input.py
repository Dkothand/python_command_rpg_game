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
            if self._validate_name(name):
                return name

