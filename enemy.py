from character import Character
from random import randint


class Enemy(Character):
    def __init__(self, name):
        super().__init__(name)
        self.hp = self.get_hp()
        self.atk = self.get_atk()
        print(f'A new enemy {self.name} approaches!')

    def get_hp(self):
        return randint(5,15) 

    def get_atk(self):
        return randint(3,5)
