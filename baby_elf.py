from enemy import Enemy
import random

class Baby_Elf(Enemy):
    def cry():
        print("WAAAAA WAAAA")

    def take_damage(self, damage):
        print("YOU HIT A BABY! YOU MONSTER")
        return super().take_damage(damage)
       
    def __init__(self, name):
        super().__init__(name)   
        self.health = 50
        self.attack_power = 700