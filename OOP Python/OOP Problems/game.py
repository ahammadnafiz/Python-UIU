import random

class Character:
    def __init__(self, name, attack_damage, total_health):
        self.name = name
        self.attack_damage = attack_damage
        self.total_health = total_health
        self.current_health = total_health

    def is_alive(self):
        return self.current_health > 0

    def take_damage(self, damage):
        self.current_health -= damage
        if self.current_health < 0:
            self.current_health = 0

    def display_status(self):
        print(f"{self.name} - Health: {self.current_health}/{self.total_health}")

class Hero(Character):
    def __init__(self, name, special_power, attack_damage=15, total_health=100):
        super().__init__(name, attack_damage, total_health)
        self.special_power = special_power
        self.level = 1
        self.experience = 0
        self.max_experience = 100

    def heal(self):
        if self.current_health < self.total_health:
            self.current_health += 25
            if self.current_health > self.total_health:
                self.current_health = self.total_health
            print(f"{self.name} healed for 25 health.")
        else:
            print(f"{self.name} is already at full health.")

    def level_up(self):
        self.level += 1
        self.max_experience *= 1.5
        self.attack_damage += 5
        self.total_health += 20
        self.current_health = self.total_health
        print(f"{self.name} leveled up to Level {self.level}!")

    def special_attack(self, enemies):
        if self.special_power == "Fireball" and self.experience >= 50:
            print(f"{self.name} used Fireball!")
            for enemy in enemies:
                damage = self.attack_damage + random.randint(10, 20)
                enemy.take_damage(damage)
                print(f"{enemy.name} took {damage} damage.")
            self.experience -= 50
        else:
            print("Not enough experience or invalid special power.")

class Enemy(Character):
    def __init__(self, name, color, attack_damage=5, total_health=50):
        super().__init__(name, attack_damage, total_health)
        self.color = color

# Game Setup
hero = Hero(name="Hero1", special_power="Fireball")
enemies = [
    Enemy(name="Enemy1", color="Red"),
    Enemy(name="Enemy2", color="Blue"),
    Enemy(name="Enemy3", color="Green")
]

# Game Execution
while hero.is_alive() and any(enemy.is_alive() for enemy in enemies):
    hero.display_status()
    for enemy in enemies:
        enemy.display_status()

    hero.special_attack(enemies)

    for enemy in enemies:
        if enemy.is_alive():
            enemy.attack(hero)

    hero.experience += 20  # Gain experience each round for added complexity
    if hero.experience >= hero.max_experience:
        hero.level_up()

print("Game Over!")
if hero.is_alive():
    print(f"{hero.name} wins!")
else:
    print("Enemies have defeated the hero.")
