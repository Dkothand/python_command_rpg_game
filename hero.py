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
        
    def battle_report(self):
        is_winner = True
        if self.hp > 0:
            print(f'{self.name} is victorius!')
        else:
            print(f'{self.name} has fallen!')
            is_winner = False
        return is_winner