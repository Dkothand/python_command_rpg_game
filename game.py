from battle import Battle
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
        self.is_game_running = True

    def _start_message(self):
        print(constants.GAME_START)

    def _handle_menu_action_response(self, res):
        if res == 'fight':
            self._create_enemy()
            battle = Battle(self.player, self.enemy)
            result = battle.fight()
            self._check_victory(result)
        elif res == 'character':
            print(self.player.__repr__())
        elif res == 'exit':
            self._end_game()

    def _create_characters(self, user_name):
        self.player = Hero(user_name)

    def _create_enemy(self):
        self.enemy = Enemy()

    def _check_victory(self, outcome):
        if outcome == "lose":
            print(constants.GAME_OVER_LOSE)
            self._end_game()

    def _load_user_actions(self):
        self.user_actions = UserActions(self.player)

    def _initalize_game(self):
        player_name = self.user_input.get_player_name()
        self._create_characters(player_name)
        self._load_user_actions()

    def _end_game(self):
        self.is_game_running = False

    def execute(self, action):
        res = self.user_actions.execute_action(action)
        self._handle_menu_action_response(res)

    def run(self):
        self._initalize_game()
        while self.is_game_running:
            command = self.user_actions.get_user_action()
            self.execute(command)
        if self.player.hp == 0:
            print(constants.GAME_OVER_LOSE)
