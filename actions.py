from enemy import Enemy
from user_commands import UserCommands as UC

import constants


class UserActions:
    def __init__(self, player):
        self.player = player
        self.valid_input = UC.options()
        self.ACTIONS_MAP = {
            UC.fight.value: self._fight,
            UC.run.value: self._run,
            UC.quit.value: self._quit,
            UC.character.value: self._character
        }

    def _validate_user_action(self, action):
        is_valid = False

        if action == '':
            print("Not a valid input")
            return is_valid

        user_input = action.strip().lower()[0]
        if user_input in self.valid_input:
            is_valid = True
            return is_valid
        print("Not a valid input")

    def _character(self):
        return "character"

    def _fight(self):
        print(constants.START_BATTLE)
        return "fight"

    def _run(self):
        print(constants.RUN_AWAY)
        print(constants.GAME_OVER_LOSE)
        return "exit"

    def _quit(self):
        print(constants.QUIT)
        return "exit"

    def get_user_action(self):
        ''' Gets input from user and validates '''
        while True:
            user_input = input(constants.ACTIONS_PROMPT)
            if self._validate_user_action(user_input):
                return user_input            

    def execute_action(self, action):
        response = self.ACTIONS_MAP[action]()
        return response