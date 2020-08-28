from user_commands import UserCommands as UC

import constants


class UserActions:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.ACTIONS_MAP = {
            UC.fight.value: self.fight,
            UC.run.value: self.run,
            UC.quit.value: self.quit,
            UC.character.value: self.character
        }

    def character(self):
        print(self.player.__repr__())

    def fight(self):
        print(constants.START_BATTLE)
        while not (self.player.hp == 0 or self.enemy.hp == 0):
            self.player.attack(self.enemy)
            self.enemy.attack(self.player)
        self.player.check_victory()

    @staticmethod
    def run():
        print(constants.RUN_AWAY)
        print(constants.GAME_OVER_LOSE)

    @staticmethod
    def quit():
        print(constants.QUIT)

    def execute_action(self, action):
        self.ACTIONS_MAP[action]()