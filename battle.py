class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def fight(self):
        while not (self.player.hp == 0 or self.enemy.hp == 0):
            self.player.attack(self.enemy)
            self.enemy.attack(self.player)
        player_survive = self.player.battle_report()
        if not player_survive:
            return "lose"
        return "win"