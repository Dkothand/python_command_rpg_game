from character import Character
from constants import ENEMY_NAME
from random import choice, randint

class Enemy(Character):
    def __init__(self):
        super().__init__()
        self.name = self.get_name()
        self.hp = self.get_hp()
        self.atk = self.get_atk()
        print(f'A new enemy {self.name} approaches!')

    def get_name(self):
        return choice(ENEMY_NAME)

    def get_hp(self):
        return randint(5,15) 

    def get_atk(self):
        return randint(3,5)
