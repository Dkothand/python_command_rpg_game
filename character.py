class Character:
    def __init__(self, name=''):
        self.name = name
        self.hp = 10
        self.atk = 2

    def _set_lower_health_bound(self):
        if self.hp < 0:
            self.hp = 0

    def check_health(self):
        if self.hp == 0:
            print(f'{self.name} is defeated!')

    def attack(self, opponent):
        if self.hp == 0:
            return

        print(f'{self.name} attacks!')
        opponent.hp -= self.atk
        opponent._set_lower_health_bound()
        print(f'{opponent.name} takes {self.atk} damage! Their health is now {opponent.hp}')
        opponent.check_health()
