class Hero:
    def __init__(self, name, special_power, attack_damage, total_health) -> None:
        self.name = name
        self.special_power = special_power
        self.attack_damage = attack_damage
        self.total_health = total_health
    
    def heal(self):
        self.total_health += 25
        self.total_health = min(self.total_health, 100)
        
    def attack(self, enemy):
        enemy.total_health -= self.attack_damage


class Enemy:
    def __init__(self, color, attack_damage, total_health) -> None:
        self.color = color
        self.attack_damage = attack_damage
        self.total_health = total_health
        
    def attack(self, hero):
        hero.total_health -= self.attack_damage


hero = Hero('Cyrus', 'Ice', 15, 100)
enemy = Enemy('Red', 5, 50)

hero.attack(enemy)
hero.heal()

print(f"{hero.name}'s health: {hero.total_health}")
print(f"{enemy.color} enemy's health: {enemy.total_health}")

