from enemy import Enemy
from user_commands import UserCommands as UC

import constants


class UserActions:
    def __init__(self, player):
        self.toggle_game_state = True
        self.player = player
        self.enemy = None
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
        self.enemy = Enemy()
        while not (self.player.hp == 0 or self.enemy.hp == 0):
            self.player.attack(self.enemy)
            self.enemy.attack(self.player)
        player_win = self.player.check_victory()
        if not player_win:
            self.toggle_game_state = False

    def run(self):
        print(constants.RUN_AWAY)
        print(constants.GAME_OVER_LOSE)
        self.toggle_game_state = False

    def quit(self):
        print(constants.QUIT)
        self.toggle_game_state = False

    def execute_action(self, action):
        self.ACTIONS_MAP[action]()