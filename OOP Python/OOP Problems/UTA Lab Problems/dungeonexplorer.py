class Item:
    def __init__(self, name, description, durability):
        self.name = name
        self.description = description
        self.durability = durability
    
    def use(self):
        self.durability -= 1
        print(f"{self.name} has been used. Durability reduced to {self.durability}.")
    
    def create_copy(self):
        return Item(self.name, self.description, self.durability)

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.connected_rooms = {}
        self.enemies = []
        self.likes = 0
    
    def add_item(self, item):
        self.items.append(item)
    
    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
    
    def connect_room(self, direction, room):
        self.connected_rooms[direction] = room
    
    def add_enemy(self, enemy):
        self.enemies.append(enemy)
    
    def remove_enemy(self, enemy):
        if enemy in self.enemies:
            self.enemies.remove(enemy)
    
    def like(self):
        self.likes += 1
    
    def get_copy(self):
        room_copy = Room(self.name, self.description)
        room_copy.items = [item.create_copy() for item in self.items]
        room_copy.connected_rooms = self.connected_rooms.copy()
        room_copy.enemies = self.enemies[:]
        room_copy.likes = self.likes
        return room_copy

class Player:
    def __init__(self, name, starting_room, health=100, max_health=100):
        self.name = name
        self.inventory = []
        self.current_room = starting_room
        self.health = health
        self.max_health = max_health
    
    def pick_up_item(self, item):
        self.inventory.append(item)
        self.current_room.remove_item(item)
    
    def drop_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            self.current_room.add_item(item)
    
    def move(self, direction):
        if direction in self.current_room.connected_rooms:
            self.current_room = self.current_room.connected_rooms[direction]
            print(f"You have moved to {self.current_room.name}.")
        else:
            print("You cannot move in that direction.")
    
    def use_item(self, item_name):
        for item in self.inventory:
            if item.name == item_name:
                item.use()
                return
        print(f"You do not have {item_name} in your inventory.")
    
    def attack(self, enemy_name):
        for enemy in self.current_room.enemies:
            if enemy.name == enemy_name:
                damage = enemy.attack()
                enemy.take_damage(damage)
                return
        print(f"No enemy named {enemy_name} found in this room.")
    
    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            print("You have been defeated!")
        else:
            print(f"You have taken {amount} damage. Current health: {self.health}/{self.max_health}.")
    
    def heal(self, amount):
        self.health = min(self.health + amount, self.max_health)
        print(f"You have healed for {amount} points. Current health: {self.health}/{self.max_health}.")

class Enemy:
    def __init__(self, name, health, weapon):
        self.name = name
        self.health = health
        self.max_health = health
        self.weapon = weapon
    
    def attack(self):
        return self.weapon.use()
    
    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            print(f"{self.name} has been defeated!")
        else:
            print(f"{self.name} has taken {amount} damage. Current health: {self.health}/{self.max_health}.")

class Weapon:
    def __init__(self, name, description, durability, damage):
        self.name = name
        self.description = description
        self.durability = durability
        self.damage = damage
    
    def use(self):
        self.durability -= 1
        print(f"{self.name} has been used. Durability reduced to {self.durability}.")
        return self.damage
    
    def create_copy(self):
        return Weapon(self.name, self.description, self.durability, self.damage)

# Example usage:

# Create items
sword = Weapon("Sword", "A sharp sword", 10, 5)
potion = Item("Potion", "A healing potion", 1)

# Create rooms
start_room = Room("Start Room", "The beginning of your journey")
treasure_room = Room("Treasure Room", "A room full of treasures")
start_room.add_item(sword)
treasure_room.add_item(potion)
start_room.connect_room("east", treasure_room)

# Create player
player = Player("Hero", start_room)

# Create enemy
enemy_skeleton = Enemy("Skeleton", 20, sword)

# Player actions
player.move("east")  # Moves to treasure room
player.pick_up_item(potion)  # Picks up potion
player.attack("Skeleton")  # Attacks skeleton
enemy_skeleton.attack()  # Skeleton attacks player
player.take_damage(3)  # Player takes damage
player.heal(10)  # Player heals
player.use_item("Potion")  # Player uses potion