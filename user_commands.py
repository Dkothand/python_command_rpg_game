from enum import Enum


class UserCommands(Enum):
    fight = 'f'
    quit = 'q'
    character = 'c'

    @classmethod
    def options(cls):
        return tuple(key.value for key in UserCommands)


class BattleCommands(Enum):
    attack = 'a'
    run = 'r'

    @classmethod
    def options(cls):
        return tuple(key.value for key in BattleCommands)