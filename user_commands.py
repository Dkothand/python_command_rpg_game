from enum import Enum


class UserCommands(Enum):
    fight = 'f'
    run = 'r'
    quit = 'q'
    character = 'c'

    @classmethod
    def options(cls):
        return tuple(key.value for key in UserCommands)
