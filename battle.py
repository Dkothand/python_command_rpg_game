from user_commands import BattleCommands as BC

import constants

class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.valid_input = BC.options()
        self.ACTIONS_MAP = {
           BC.attack.value: self._attack,
           BC.run.value: self._run 
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

    def _attack(self):
        self.player.attack(self.enemy)
        return "attack"

    def _run(self):
        print(constants.RUN_AWAY)
        return "exit"

    def execute_action(self, action):
        response = self.ACTIONS_MAP[action]()
        return response

    def get_user_action(self):
        ''' Gets input from user and validates '''
        while True:
            user_input = input(constants.BATTLE_PROMPT)
            if self._validate_user_action(user_input):
                return user_input            

    def fight(self):
        while not (self.player.hp == 0 or self.enemy.hp == 0):
            command = self.get_user_action()
            res = self.execute_action(command)
            if res == "exit":
                return "lose"
            self.enemy.attack(self.player)
        player_survive = self.player.battle_report()
        if not player_survive:
            return "lose"
        return "win"