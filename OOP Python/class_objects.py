class Monster:
    def __init__(self, health, energy, **kwargs) -> None:
        self.health = health
        self.energy = energy
        super().__init__(**kwargs)
        
    def attack(self, amount):
        print('The monster has attacked')
        print(f"{amount} damage dealt")
        self.health -= amount
        
    def move(self, speed):
        print('The monster has moved')
        print(f"It has speed {speed}")

class Fish:
    def __init__(self, speed, has_scales, **kwargs) -> None:
        self.speed = speed
        self.has_scales = has_scales
        super().__init__(**kwargs)
        
    def swim(self):
        print(f'The fish is swimming at the speed of {self.speed}')

class Shark(Monster, Fish):
    def __init__(self, bite_strength, health, energy, speed, has_scales) -> None:
        self.bite_strength = bite_strength
        super().__init__(health=health, energy=energy, speed=speed, has_scales=has_scales)

# Instantiate Shark
shark = Shark(bite_strength=80, health=100, energy=200, speed=30, has_scales=True)

