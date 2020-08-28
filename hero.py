from character import Character

import constants


class Hero(Character):
    def __init__(self, name):
        super().__init__(name)
        self.hp = 20
        self.atk = 5
        self.is_victor = None
        print(f'A new hero {self.name} is born!')

    def __repr__(self):
        character = f"""
        {'-' * 25}
        Character: {self.name}
        Health: {self.hp}
        Attack: {self.atk}
        {'-' * 25}
        """
        return character
        
    def check_victory(self):
        if self.hp > 0:
            print(f'{self.name} is victorius!')
            print(constants.GAME_OVER_WIN)
            self.is_victor = True
            return self.is_victor
        else:
            print(f'{self.name} has fallen!')
            print(constants.GAME_OVER_LOSE)
            self.is_victor = False
            return self.is_victor
