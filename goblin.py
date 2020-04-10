from character import Character

class Goblin(Character):
    pass
    def __init__(self, goblin_name, goblin_health, goblin_power):
        self.name = goblin_name
        self.health = goblin_health
        self.power = goblin_power
        # self.goblin_attack = goblin_attack

    def attack(self, target):
        print(f'{self.name} is attacking {target.name}')

    def alive(self):
        if self.health > 0:
            return True
        else:
            return False