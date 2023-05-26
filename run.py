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
        self.assimilate_planets = []
    
    def increase_attack(self):
        self.attack += 2

    def increase_defence(self):
        self.defence += 2

    def take_damage(self, damage):
        damage_taken = min(damage, self.health)  # Calculate the actual damage taken
        self.health -= damage_taken

        if damage > self.defence:
            damage -= self.defence
            self.health -= damage
        else:
            self.defence -= damage
            if self.defence < 0:
                self.defence = 0

        if self.health < 0:
            self.health = 0

        return damage_taken
            
    def reduce_processing(self, processing, input_code):
        if input_code.lower() == "b" and self.processing >= 100:
            self.processing -= 100
            if self.processing < 0:
                self.processing = 0
        else: 
            self.processing -= processing  # Reduce processing even if input code is incorrect
            if self.processing < 0:
                self.processing = 0

    def is_alive(self):
        return self.health > 0

    def display_stats(self):
        print("\nPlayer Stats:")
        print(f"Player Level: {self.level}")
        print(f"Player Health: {self.health}")
        print(f"Player Attack: {self.attack}")
        print(f"Player Defence: {self.defence}")
        print(f"Processing Power: {self.processing}")
        
    def display_game_finished(self): # Display end game score
        # print("\nPlayer Score:")
        # print(f"Player Level: {self.level}")
        # print(f"Processing Power: {self.processing}\n")
        num_planets = len(self.assimilate_planets)
        print(f"\nAssimilated Planets: {num_planets}")
        if self.assimilate_planets:
            for planet in self.assimilate_planets:
                print(f" - {planet.name}")
        else:
            print("No planets assimilated.")

# Define the Planet Class
class Planet:
    def __init__(self, name, resources, level):
        self.name = name
        self.resources = resources
        self.assimilated = False
        self.level = level + 1
        self.attack_points = random.randint(5, 25) + level
        self.defence_points = random.randint(5, 25) + level
        self.has_defences = random.choice([True, False]) # Randomise defences for planets

    def attack_player(self, player):
        damage_dealt = self.attack_points
        player.take_damage(damage_dealt)
        print(self.name, "attacks! Player takes", damage_dealt, "damage.")
        print("Player health remaining:", player.health)
        if not player.is_alive():
            print("\nPlayer has lost control of the collective.\n")
            player.display_game_finished()
            print("\nGAME OVER")
            sys.exit()
            
    def assimilate(self, player):
        self.assimilated = True
        player.processing += self.resources.get("processing", 0)
        player.assimilate_planets.append(self) # Add the assimilated planet to the player's list

    def is_assimilated(self):
        return self.assimilated

# Define System Class
class System:
    def __init__(self, name, enemy_resistance, planets):
        self.name = name
        self.enemy_resistance = enemy_resistance
        self.planets = planets

    def assimilate_planet(self, planet_index, player):
        if planet_index in range(len(self.planets)):
            planet = self.planets[planet_index]
            if not planet.is_assimilated():
                if planet.has_defences: # Hacking mini game initiated randomly if boolean value is True1
                    print(f"\n{planet.name}'s defences initiated ... \n")
                    print("---------------{ Hacking }---------------\n")
                    # ASCII art for code rain characters
                    code_rain_chars = ['|', '/', '-', '\\']

                    # Function to generate random code rain line with numbers
                    def generate_code_rain_line(width, access_code):
                        line = ""
                        for i in range(width):
                            if len(access_code) > 0 and random.random() < 0.2:  # 20% chance of adding a number clue
                                digit = access_code.pop(0)
                                if i < 2:  # Check for the first two characters
                                    line += "00"  # Set the first two characters as "00"
                                else:
                                    line += str(digit)
                            else:
                                line += random.choice(code_rain_chars)
                        return line

                    # Function to generate random access code
                    def generate_access_code():
                        code = []
                        code.append(0)
                        code.append(0)
                        for _ in range(4):
                            digit = random.randint(1, 9)  # Random number from 1 to 9 (excluding 0)
                            code.append(digit)
                        return code

                    # Function to check if the input code is correct
                    def check_code(input_code, access_code):
                        if input_code.lower() == "b" and player.processing >= 100:
                            print("Automated cracking in progress...")
                            automated_code = automate_crack(access_code)
                            print("Access code: {}".format(automated_code))
                            player.reduce_processing(100, input_code)
                            return True
                        else:
                            print("Processing power insufficient.")    
                        for i in range(len(input_code)):
                            if input_code[i] != str(access_code[i]):
                                return False
                        return len(input_code) == len(access_code)

                    # Function to automate the cracking of the access code
                    def automate_crack(access_code):
                        return "".join(str(digit) for digit in access_code)

                    # Generate access code
                    access_code = generate_access_code()

                    # Print the code rain animation
                    def print_code_rain(access_code):
                        for _ in range(10):
                            code_rain_line = generate_code_rain_line(40, access_code.copy())
                            print(code_rain_line)

                    # Start the code rain static animation
                    print_code_rain(access_code)

                    # Game loop
                    attempts_left = 3
                    while attempts_left > 0:
                        # Read user input
                        if player.processing >= 100:
                            print("\nBypass enemy systems. Costs 100 processing power.\n")
                            print(f"You have {player.processing} processing power in storage. Please type 'b'\n")
                        else:
                            print(f"\nInsufficient processing power. You have {player.processing} in storage.")
                            print("The collective cannot bypass enemy systems right now.")
                            
                        input_code = input("\nEnter the access code (6 digits): ")
                    
                        # Check if the input code is correct
                        if check_code(input_code, access_code):
                            print("Access granted...")
                            planet.assimilate(player)
                            return True
                        else:
                            attempts_left -= 1
                            if attempts_left < 2 and attempts_left > 0:
                                print("Access denied. {} attempt left.".format(attempts_left))
                            elif attempts_left > 1: 
                                print("Access denied. {} attempts left.".format(attempts_left))
                            else:
                                print("Access denied. Hacking failed.")
                                player_damage = player.take_damage(random.randint(1, 50))
                                print(f"\nYou took damage {player_damage}. Health remaining {player.health}.")
                else:
                    planet.assimilate(player)
                    return True
            else:
                print(planet.name, "is already assimilated!")
        else:
            print("Invalid selection")
        return False
    
    def attack(system, attack_power):
        if player.level < 5:
            system.enemy_resistance = random.randint(1, 25)  # Update the resistance level within the desired range
        success_chance = attack_power / system.enemy_resistance
        print("\nAttacking", system.name, "with resistance level:", system.enemy_resistance)
        print(attack_power)
        print(success_chance)
        return success_chance >= 1


# Load systems data
def load_systems_data():
    systems_data = [
        {
            "name": "Alpha System",
            "enemy_resistance": random.randint(25, 60),
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
            "enemy_resistance": random.randint(9, 60),
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
            "enemy_resistance": random.randint(9, 60),
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
            "enemy_resistance": random.randint(1, 30),
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
            "enemy_resistance": random.randint(9, 50),
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
    
systems_data = load_systems_data()

# Assimilate a planet within a system
def attack_system(system, player):
    
    success = system.attack(player.attack)
    if success:
        print("We are Borg. Existence as you know it is over. Resistance is futile.\n")
        # Display the available planets for assimilation
        print("\nAvailable planets for assimilation:")
        for i, planet in enumerate(system.planets):
            if planet.is_assimilated():
                print(f"{str(i + 1)}. {''.join(chr(822) + c for c in planet.name)} (Assimilated)")
            else:
                print(f"{i + 1}. {planet.name}")

        choice = int(input("Select a planet to assimilate: ")) - 1
        assimilated = system.assimilate_planet(choice, player)
        if assimilated:
            player.level += 1
            player.increase_attack()
            player.increase_defence()
            print("\n=================================================================")
            print(f"{f'You have assimilated {system.planets[choice].name}'.center(67)}")
            print("=================================================================")
        else:
            print("Assimilation failed!\n")
    else:
        print("Our attack was unsuccessful. Prepare for a counterattack!\n")
        # Randomly select a planet from the system to attack the player
        enemy_planet = random.choice(system.planets)
        enemy_planet.attack_player(player)
        if not player.is_alive():
            game_over()

        # Determine the outcome based on player's attack power and enemy resistance
        if player.attack > system.enemy_resistance:
            print("We have successfully counterattacked the enemy planet!")
            system.planets.remove(enemy_planet)
        else:
            print("Our counterattack was unsuccessful.\n")


# Decrease player life
def decrease_player_life(player, damage_dealt):
    player.take_damage(damage_dealt)
    print(f"Your collective has been damaged! Player health remaining: {player.health}\n")
    if not player.is_alive():
        print("Your collective has been destroyed.")
        player.display_game_finished()
        print("GAME OVER")
        sys.exit()


# Game over
def game_over():
    player.display_game_finished()
    print("\nGAME OVER\n")
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
print("\n============================================")
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

        system_index = int(input("\nSelect a system to attack: ")) - 1
        selected_system = systems[system_index]
        attack_system(selected_system, player)

        if not player.is_alive():
            game_over()

    elif choice == "2":
        game_over()

    else:
        print("Invalid choice. Please try again.")
