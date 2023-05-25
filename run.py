import random 
import sys

# Define the Player class

class Player:
    def __init__(self):
        self.health = 100
        self.defence = 10
        self.attack = 10
        self.level = 1
        
    def increase_attack(self):
        self.attack += 5
        
    def increase_defence(self):
        self.defence += 5
    
    def take_damage(self, damage):
        damage -= self.defence
        if damage > 0:
            self.health -= damage
            
    def is_alive():
        return self.health > 0
    
    def display_stats():
        print("Player Stats:")
        print(f"Player Level: {self.level}")
        print(f"Player Health: {self.health}")
        print(f"Player Attack: {self.attack}")
        print(f"Player Defence: {self.defence}")


# Define the Planet Class 

class Planet: 
    def __init__(self, name, resources, level):
        self.name = name
        self.resources = resources
        self.assimilated = False
        self.level = random.randint(1, 20)
        self.attack_points = random.randomint(1, 5) + level
        self.defence_points = random.randint(1, 5) + level
    
    def attack_player(self, player):
        damage_dealt = self.attack_points
        player.take_damage(damage_dealt)
        print(self.name, "attacks! Player takes", damage_dealt, "damage.")
        
    def assimilated(self):
        self.assimilated = True
        
    def is_assimilated(self):
        return self.assimilated
    
# Define System Class 

class System:
    def __init__ (self, enemy_resistance, planets):
        self.name = name
        self.enemy_resistance = enemy_resistance
        self.planets = planets
        
    def assimilate_planet(self, planet_index):
        if planet_index in range(len(self.planets)):
            planet = self.planets[planet_index]
            if not planet.is_assimilated():
                planet.assimilate()
                self.resources_gained = planet.resources
                planet.resources = {"processing": 0}
                return True
            else:
                print(planet.name, "is already assimilated!")
        else:
            print("Invalid selection")
        return False
    
    def attack(self, attack_power):
        success_chance = attack_power / self.enemy_resistance
        return random.random() <= success_chance
    
    def display_planets(self):
        for i, planet in enumerate(self.planets):
            print(f"{i+1}. {planet.name}")
    
    # def add_planet(self, planet):
    #     self.planets.append(planet)
        
# Load systems data
def load_systems_data():
    systems_data = [
        {
            "name": "Alpha System",
            "enemy_resistance": random.randint(40, 70),
            "planets": [
                Planet("Earth", {"processing": random.randint(20, 50)}),
                Planet("Vulcan", {"processing": random.randint(20, 50)}),
                Planet("Klingon", {"processing": random.randint(20, 50)}),
                Planet("Romulus", {"processing": random.randint(20, 50)}),
                Planet("Andoria", {"processing": random.randint(20, 50)})
            ]
        },
        {
            "name": "Beta System",
            "enemy_resistance": random.randint(40, 70),
            "planets": [
                Planet("Cardassia Prime", {"processing": random.randint(20, 50)}),
                Planet("Bajor", {"processing": random.randint(20, 50)}),
                Planet("Ferenginar", {"processing": random.randint(20, 50)}),
                Planet("Qo'noS", {"processing": random.randint(20, 50)}),
                Planet("Trill", {"processing": random.randint(20, 50)})
            ]
        },
        {
            "name": "Gamma System",
            "enemy_resistance": random.randint(40, 70),
            "planets": [
                Planet("Betazed", {"processing": random.randint(20, 50)}),
                Planet("Risa", {"processing": random.randint(20, 50)}),
                Planet("Tellar Prime", {"processing": random.randint(20, 50)}),
                Planet("Q'uorath", {"processing": random.randint(20, 50)}),
                Planet("Federation Outpost 112", {"processing": random.randint(20, 50)})
            ]
        },
        {
            "name": "Delta System",
            "enemy_resistance": random.randint(40, 70),
            "planets": [
                Planet("Vorta", {"processing": random.randint(20, 50)}),
                Planet("Founders' Homeworld", {"processing": random.randint(20, 50)}),
                Planet("Breen Homeworld", {"processing": random.randint(20, 50)}),
                Planet("Talax", {"processing": random.randint(20, 50)}),
                Planet("Ocampa", {"processing": random.randint(20, 50)})
            ]
        },
        {
            "name": "Epsilon System",
            "enemy_resistance": random.randint(40, 70),
            "planets": [
                Planet("Nimbus III", {"processing": random.randint(20, 50)}),
                Planet("Rigel VII", {"processing": random.randint(20, 50)}),
                Planet("Sheliak", {"processing": random.randint(20, 50)}),
                Planet("Tribble Homeworld", {"processing": random.randint(20, 50)}),
                Planet("Deneb IV", {"processing": random.randint(20, 50)})
            ]
        }
    ]
    return systems_data  

# Assimilate a planet within a system 

def assimilate_planet(system, player):
    print("\nAvailable Systems for attack: ")
    for i, system in enumerate(systems):
        print(f"{i+1}. {system.name}")
        
    system_index = int(input("Select a system to attack: ")) - 1
    selected_system = systems[system_index]
    print(f"\nAvailable planets for attack in {selected_system.name}:")
    selected_system.display_planets()
    
    planet_index = int(input("Select a planet to attack: ")) - 1
    assimilated = selected_system.assimilate_planet(planet_index)
    if assimilated:
        player.level += 1
        player.increase_attack()
        player.increase_defence()
        print("You have assimilated", assimilated.name)
    else:
        print("Assimilation failed!")
        
# Attack a player


        
# Main game loop

def main_game_loop(player, systems):
    
    while True:
        print("\nPlayers: Turn")
        player.display_stats()
        break
        
    

# Display opening screen 

def opening_page():
    
    print("=== BorgLite ===\n")
    print("Welcome to BorgLite!")
    choice = input("Do you wish to become part of the collective? (Y/N) ")
    if choice.upper() == "Y":
        print("Welcome! Prepare to assimilate the digital realm.")
        main_game_loop()
    else:
        print("Your resistance is futile. Goodbye!")

# Run the game
if __name__ == "__main__":
    
    opening_page()