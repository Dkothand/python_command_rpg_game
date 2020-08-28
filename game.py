from hero import Hero
from enemy import Enemy
from user_input import UserInput
from actions import UserActions

import constants


class Game:
    def __init__(self):
        self._start_message()
        self.user_input = UserInput()
        self.user_actions = None
        self.player = None
        self.enemy = None

    def _start_message(self):
        print(constants.GAME_START)

    def _create_characters(self, user_name):
        self.player = Hero(user_name)
        self.enemy = Enemy("Orc")

    def _load_user_actions(self):
        """ Instantiates UserActions, requires created player and enemy objects """
        self.user_actions = UserActions(self.player, self.enemy)

    def _initalize_game(self):
        player_name = self.user_input.get_player_name()
        self._create_characters(player_name)
        self._load_user_actions()

    def execute(self, action):
        self.user_actions.execute_action(action)

    def run(self):
        self._initalize_game()
        command = self.user_input.get_user_action()
        self.execute(command)
