import random
import sys

# Define the Player class
class Player:
    def __init__(self):
        self.health = 100
        self.defence = 10
        self.attack = 10
        self.level = 1
        self.processing = 0

    def increase_attack(self):
        self.attack += 2

    def increase_defence(self):
        self.defence += 2

    def take_damage(self, damage):
        if damage > self.defence:
            damage -= self.defence
            self.health -= damage
        else:
            self.defence -= damage
            if self.defence < 0:
                self.defence = 0
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        return self.health > 0

    def display_stats(self):
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
        self.level = level + 1
        self.attack_points = random.randint(5, 15) + level
        self.defence_points = random.randint(5, 15) + level

    def attack_player(self, player):
        damage_dealt = self.attack_points
        player.take_damage(damage_dealt)
        print(self.name, "attacks! Player takes", damage_dealt, "damage.")
        print("Player health remaining:", player.health)
        if not player.is_alive():
            print("Player has been assimilated. Game Over.")
            sys.exit()

    def assimilate(self):
        self.assimilated = True

    def is_assimilated(self):
        return self.assimilated

# Define System Class
class System:
    def __init__(self, name, enemy_resistance, planets):
        self.name = name
        self.enemy_resistance = enemy_resistance
        self.planets = planets

    def assimilate_planet(self, planet_index):
        if planet_index in range(len(self.planets)):
            planet = self.planets[planet_index]
            if not planet.is_assimilated():
                planet.assimilate()
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


# Load systems data
def load_systems_data():
    systems_data = [
        {
            "name": "Alpha System",
            "enemy_resistance": random.randint(1, 20),
            "planets": [
                Planet("Earth", {"processing": random.randint(20, 50)}, 1),
                Planet("Vulcan", {"processing": random.randint(20, 50)}, 1),
                Planet("Klingon", {"processing": random.randint(20, 50)}, 1),
                Planet("Romulus", {"processing": random.randint(20, 50)}, 1),
                Planet("Andoria", {"processing": random.randint(20, 50)}, 1)
            ]
        },
        {
            "name": "Beta System",
            "enemy_resistance": random.randint(1, 20),
            "planets": [
                Planet("Cardassia Prime", {"processing": random.randint(20, 50)}, 1),
                Planet("Bajor", {"processing": random.randint(20, 50)}, 1),
                Planet("Ferenginar", {"processing": random.randint(20, 50)}, 1),
                Planet("Qo'noS", {"processing": random.randint(20, 50)}, 1),
                Planet("Trill", {"processing": random.randint(20, 50)}, 1)
            ]
        },
        {
            "name": "Gamma System",
            "enemy_resistance": random.randint(1, 20),
            "planets": [
                Planet("Betazed", {"processing": random.randint(20, 50)}, 1),
                Planet("Risa", {"processing": random.randint(20, 50)}, 1),
                Planet("Tellar Prime", {"processing": random.randint(20, 50)}, 1),
                Planet("Q'uorath", {"processing": random.randint(20, 50)}, 1),
                Planet("Federation Outpost 112", {"processing": random.randint(20, 50)}, 1)
            ]
        },
        {
            "name": "Delta System",
            "enemy_resistance": random.randint(1, 100),
            "planets": [
                Planet("Vorta", {"processing": random.randint(20, 50)}, 1),
                Planet("Founders' Homeworld", {"processing": random.randint(20, 50)}, 1),
                Planet("Breen Homeworld", {"processing": random.randint(20, 50)}, 1),
                Planet("Talax", {"processing": random.randint(20, 50)}, 1),
                Planet("Ocampa", {"processing": random.randint(20, 50)}, 1)
            ]
        },
        {
            "name": "Epsilon System",
            "enemy_resistance": random.randint(1, 20),
            "planets": [
                Planet("Nimbus III", {"processing": random.randint(20, 50)}, 1),
                Planet("Rigel VII", {"processing": random.randint(20, 50)}, 1),
                Planet("Sheliak", {"processing": random.randint(20, 50)}, 1),
                Planet("Tribble Homeworld", {"processing": random.randint(20, 50)}, 1),
                Planet("Deneb IV", {"processing": random.randint(20, 50)}, 1)
            ]
        }
    ]
    return systems_data

# Assimilate a planet within a system
def attack_system(system, player):
    print("\nAttacking", system.name, "with resistance level:", system.enemy_resistance)
    success = system.attack(player.attack)
    if success:
        print("We are Borg. Existence as you know it is over. We will add your biological and technological distinctiveness to our own. Resistance is futile.\n")
        # Display the available planets for assimilation
        print("\nAvailable planets for assimilation:")
        for i, planet in enumerate(system.planets):
            print(f"{i + 1}. {planet.name}")

        choice = int(input("Select a planet to assimilate: ")) - 1
        assimilated = system.assimilate_planet(choice)
        if assimilated:
            player.level += 1
            player.increase_attack()
            player.increase_defence()
            print("\n=================================================================")
            print(f"{f'You have assimilated {system.planets[choice].name}'.center(67)}")
            print("=================================================================\n")
        else:
            print("Assimilation failed!")
    else:
        print("Our attack was unsuccessful. Prepare for counterattack!\n")
        system.planets[random.randint(0, len(system.planets) - 1)].attack_player(player)
        decrease_player_life(player, system.planets[random.randint(0, len(system.planets) - 1)].attack_points)


# Decrease player life
def decrease_player_life(player, damage_dealt):
    player.take_damage(damage_dealt)
    print("Your collective has been damaged! Player health remaining:", player.health)
    if not player.is_alive():
        print("Your collective has been destroyed. Game over.")
        sys.exit()


# Game over
def game_over():
    print("\nGAME OVER")
    sys.exit()


# Game initialization
player = Player()
systems_data = load_systems_data()
systems = []

# Create system objects
for system_data in systems_data:
    system = System(system_data["name"], system_data["enemy_resistance"], system_data["planets"])
    systems.append(system)

# Game loop
print("============================================")
print("            Welcome to BorgLite             ")
print("============================================")

while True:
    player.display_stats()
    print("\nWhat would you like to do?")
    print("1. Attack a system")
    print("2. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nAvailable Systems for attack: ")
        for i, system in enumerate(systems):
            print(f"{i + 1}. {system.name}")

        system_index = int(input("Select a system to attack: ")) - 1
        selected_system = systems[system_index]
        attack_system(selected_system, player)

        if not player.is_alive():
            game_over()

    elif choice == "2":
        game_over()

    else:
        print("Invalid choice. Please try again.")
