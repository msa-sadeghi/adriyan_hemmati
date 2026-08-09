class Enemy:
    def __init__(self, type, image, damage):
        self.type = type
        self.image = image
        self.damage = damage

    def move(self):
        print(f"{self.type} is moving")
    
    def damage_player(self):
        print(f"{self.type} is damaging player")

class Zombie(Enemy):
    def __init__(self, type, image, damage, power):
        super().__init__(type, image, damage)
        self.power = power
    def eat_player(self):
        print(f"{self.type} is eating player")
    
z1 = Zombie("male zombie", 'mz', 2, 3)
z1.move()
z1.damage_player()   
z1.eat_player()   
   

