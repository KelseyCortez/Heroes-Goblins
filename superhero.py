from character import Character

class Hero(Character):
    pass
    def __init__(self, hero_name, hero_health, hero_power):
        self.name = hero_name
        self.health = hero_health
        self.power = hero_power
        # self.attack_name = hero_attack
        
    def attack(self, target):
        print(f'{self.name} is attacking {target.name}')

    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

