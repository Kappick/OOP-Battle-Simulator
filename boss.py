import random
from enemy import Enemy
class Boss(Enemy):
    def __init__(self, name):
        super().__init__(name)
        self.health = 650
        self.attack_power = random.randint(50, 400)
    
    def attack(self):
        if self.health < 250:
            self.attack_power <= random.randint(100, 500)
            
        

