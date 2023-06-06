import random
import sys
import time
from leaderboard import update_leaderboard, display_leaderboard

# Define the Player class
class Player:
    def __init__(self):
        self.name = "Rhys"
        self.health = 100
        self.defence = 10
        self.attack = 100
        self.level = 1
        self.processing = 1000
        self.score = 0
        self.rank = ""
        self.assimilate_planets = [] # List to store assimilated planets
        self.upgrades = [] # List to store upgrades
        
    def leaderboard_player(self, level, score): # Player's leaderboard function calling the module leaderboard.py
        
        player_row = {self.rank, self.name, self.level, self.score} # Create player_row object to pass to the update_leaderboard function
        update_leaderboard(player)
        
    def apply_upgrade(self, index, processing):
        if index >= 0 and index < len(self.upgrades):
            upgrade = self.upgrades[index]
            if self.processing >= 100:
                self.health += upgrade.add_health
                self.defence += upgrade.add_defence
                self.attack += upgrade.add_attack
                self.processing -= 100
                print("\n   >> Upgrade applied successfully!")
            else:
                 print(f"\n   >> Insufficient processing power. You have {player.processing} in storage.")

        else:
            print("  >> Invalid.")
        
    def increase_attack(self): # Increase attack each level
        self.attack += 2

    def increase_defence(self): # Increase defence each level
        self.defence += 2

    def take_damage(self, damage): # Take damage from system by individual planets
        if self.defence > 0:
            if damage <= self.defence:
                self.defence -= damage
            else:
                remainder = damage - self.defence
                self.defence = 0
                self.health -= remainder
        else: 
            self.health -= damage
        self.health = max(self.health, 0)  # Ensure health doesn't go below 0
        return self.defence and self.health
    
    def hacking_damage(self, damage, has_defences): # Take damage from failure to hack defences
        damage_taken = damage
        if self.defence > 0:
            damage_taken = min(damage, self.health)  # Calculate the actual damage taken
            if damage_taken <= self.defence:
                self.defence -= damage_taken
            else:
                remainder = damage_taken - self.defence
                self.defence = 0
                self.health -= remainder
        else:
            self.health -= damage_taken
        self.health = max(self.health, 0)  # Ensure health doesn't go below 0   
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
        
        num_planets = len(self.assimilate_planets)
        self.score = self.processing * num_planets * self.level * self.attack
        
        sw = "\033[37m" # white
        ew = "\033[0m"
        
        s = "\033[32m" # green
        e = "\033[0m"
        
        sr = "\033[31m" # red
        er = "\033[0m"
        
        
        art = f"""  {s}                          
 ________.--------------._______________________________________________________________
 |  ||__| [_]|                    |                                                     |
 |  |     [_]|    {sw}Player Stats:  {ew}{s} | {e}    {sw} Power  {power_icon} : {self.processing} {ew}   {s}    |  {e}   {sw}score: {self.score}  {ew} {s}       
 |__|_____[_]|____________________|_____________________________________________________|                                                     
 | | {sw}PWR{ew}{s} |  |{sw} ::{ew}{s} |{sw}-++++-{ew}{s} |   ||   |                                                     |
 | | {sw}OFF{ew}{s} |  |_{sw}::{ew}{s}_|{sw} /-/-/-{ew}{s}|___||___|  {sw} Health {heart_icon}  : { self.health }   Attack {sword_icon}  : { self.attack }   Defence{shield_icon}  : { self.defence}    {ew} {s}                                            
 |_|{sw}['q']{s}|________________________|_____________________________________________________|                                                      
 |                 _______________|            ________           ________              |                             
 |  {sw}  1. [ALPHA] {ew}{s} |                                                                     |       
 |   {sw} 2. [BETA ] {ew}{s} |   __.------------.                                                  |
 | __   ____,-----------------,  -| |\`-.                                               |
 | __|  ____|] =========--  [<    |_|____`-.                                            |
 | `-._______`-----------------`____________-`                                          |    
 |      `-`-----'---'---------`------------'                                            |        
 |   {sw} 3. [GAMMA] {ew}{s} |                                                                     |
 |  {sw}  4. [DELTA] {ew}{s} |                                                                     |
 |  {sw}  5. [EPSIL] {ew}{s} |                                                                     |
 |  _____   |   _ |                                                                     |
 | |{sw}+ B +{ew}{s}|  |__|_________________ ______________________________________________________|
 | ||{sw} O {ew}{s}||  .   {sw} -Lvl: {self.level} {ew}{s} --.  _                                                       
 | ||{sw} R {ew}{s}||  |               | [_] |   {sw} Attack a system  'a'   {ew}{s}                          |
 | ||{sw} G {ew}{s}||                    [_] |  {sw}  Upgrades         'u'       <<   choices     {ew}{s}     |
 | |{sw}L{ew}{s}_{sw}T{ew}{s}_{sw}E{ew}{s}|  [___] [___] [___] [_] |  {sw}  Leaderboards     'l'     {ew}{s}        ______          |
 |________________________________|  {sw}  Help             'h'      {ew}{s}                       |
 |__[][][][]____________[][][][]__|____________________________________________________ |
 {e} """
 
        print(art)
        
        
    def display_game_finished(self): # Display end game score 
        num_planets = len(self.assimilate_planets)
        score = self.processing * num_planets * self.level * self.attack
        type_text(f"   >> Final Score: {score}\n")
        print(f"\n   >> Assimilated Planets {planet_icon} : {num_planets}")
        if self.assimilate_planets:
            for planet in self.assimilate_planets:
                print(f"   - {planet.name}")
        else:
            type_text("   >> No planets assimilated.\n")
                    
# Define the upgrades class
class Upgrades:
    def __init__(self, name, add_health=0, add_defence=0, add_attack=0):
        self.name = name
        self.add_health = add_health
        self.add_defence = add_defence
        self.add_attack = add_attack

    @staticmethod
    def load_upgrades_data(heart_icon, sword_icon, shield_icon):
        upgrades_data = [
            {
                "name": f"Health Regeneration {heart_icon}  +50  {shield_icon}  -2 {sword_icon}  -2",
                "add_health": 50,
                "add_defence": -2,
                "add_attack": -2,
            },
            {
                "name": f"Adaptive Shielding {shield_icon}  +50 {sword_icon}  -2",
                "add_defence": 50,
                "add_attack": -2
            },
            {
                "name": f"Cybernetic Implant {sword_icon}  +5",
                "add_attack": 5
            }
        ]
        
        upgrades = []
        for upgrade_info in upgrades_data:
            upgrade = Upgrades(**upgrade_info)
            upgrades.append(upgrade)
        
        return upgrades


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
        print( f"\n   -+++- {self.name} attacks! Player takes {damage_dealt} damage")
        print("   -+++- Player health remaining:", player.health)
        if not player.is_alive():
            print("\n   >> Player has lost control of the collective.\n")
            player.display_game_finished()
            level = ""
            score = ""
            player.leaderboard_player(level, score)
            print("\n  >> GAME OVER")
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
                    type_text(f"\n   >> {planet.name}'s defences initiated ...\n")
                    type_text("   >> Hacking sequence ... \n")
                    type_text("   >> START \n")
                    print("\n")
                    # ASCII art for code rain characters
                    s = "\033[32m" # green
                    e = "\033[0m"
                    code_rain_chars = ['|', '/', '-', '\\']
                    
                    # Function to generate random code rain line with numbers
                    def generate_code_rain_line(width, access_code, fake_code):
                        line = ""
                        for i in range(width):
                            if len(access_code) > 0 and random.random() < 0.1:  # 10% chance of adding a number clue
                                digit = access_code.pop(0)
                                if i < 2:  # Check for the first two characters
                                    line += "00"  # Set the first two characters as "00"
                                else:
                                    line += str(digit)
                            elif len(fake_code) > 0 and random.random() < 0.1:
                                fake_digit = fake_code.pop(0)
                                line += str(fake_digit)
                            else:
                                line += random.choice(code_rain_chars)
                        return line
                    
                    # Function to generate random access code
                    def generate_access_code():
                        code = []
                        code.append(0)
                        code.append(0)
                        for _ in range(4):
                            digit = random.randint(3, 9)  # Random number from 1 to 9 (excluding 0)
                            code.append(digit)
                        return code
                    
                    # Function to generate random fake code
                    def generate_fake_code():
                        code = []
                        for _ in range(1):
                            fake_digit = random.randint(1, 2) # Random number
                            code.append(fake_digit)
                        return code

                    # Function to check if the input code is correct
                    def check_code(input_code, access_code):
                        if input_code.lower() == "b" and player.processing >= 100:
                            print("   >> Automated cracking in progress...")
                            automated_code = automate_crack(access_code)
                            print("   >> Access code: {}".format(automated_code))
                            player.reduce_processing(100, input_code)
                            return True
                        else:
                            print("")    
                        for i in range(len(input_code)):
                            if input_code[i] != str(access_code[i]):
                                return False
                        return len(input_code) == len(access_code)

                    # Function to automate the cracking of the access code
                    def automate_crack(access_code):
                        return "".join(str(digit) for digit in access_code)

                    # Generate access code
                    access_code = generate_access_code()
                    fake_code = generate_fake_code()

                    # Print the code rain animation
                    def print_code_rain(access_code, fake_code):
                        for _ in range(10):
                            code_rain_line = generate_code_rain_line(85, access_code.copy(), fake_code.copy())
                            print(f"{s}   {code_rain_line}{e}")

                    # Start the code rain static animation
                    print_code_rain(access_code, fake_code)

                    # Game loop
                    attempts_left = 3
                    while attempts_left > 0:
                        # Read user input
                        if player.processing >= 100:
                            print("\n   >> Bypass enemy systems. Costs 100 processing power.\n")
                            print(f"   >> You have [{player.processing} processing power] in storage. Please type 'b'\n")
                        else:
                            type_text(f"\n   >> Insufficient processing power. You have {player.processing} in storage.")
                            type_text("\n   >> The collective cannot bypass enemy systems right now.")
                            # print(access_code)
                            
                        type_text("\n   >> Enter the access code (6 digits): ")
                        input_code = input()
                        # Check if the input code is correct
                        if check_code(input_code, access_code):
                            print("   >> Access granted...")
                            planet.assimilate(player)
                            return True
                        else:
                            attempts_left -= 1
                            if attempts_left < 2 and attempts_left > 0:
                                print("   >> Access denied. {} attempt left.".format(attempts_left))
                            elif attempts_left > 1: 
                                print("   >> Access denied. {} attempts left.".format(attempts_left))
                            else:
                                print("   >> Access denied. Hacking failed.")
                                player_damage = player.hacking_damage(random.randint(1, 50), planet.has_defences)
                                print(f"\n   >> You took damage {player_damage}. Health remaining {player.health}.")
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
            system.enemy_resistance = random.randint(3, 17)  # Update the resistance level within the desired range
        elif player.level >= 5 and player.level <= 10:
            system.enemy_resistance = random.randint(10, 35)  # Update the resistance level within the desired range
        else:
            system.enemy_resistance = random.randint(20, 65)  # Update the resistance level within the desired range
            
        success_chance = attack_power / system.enemy_resistance    
        print("\n   -+++- Attacking", system.name, "with resistance level:", system.enemy_resistance)
        print(f"   -+++- Engagement Probability: {round(success_chance, 2)}\n")
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
    

# Assimilate a planet within a system
def attack_system(system, player):
    
    success = system.attack(player.attack)
    if success:
        while True:
            main_loop= False # Stop main loop
             
            type_text("   >> We are Borg. Existence as you know it is over. Resistance is futile.\n")
            # Display the available planets for assimilation
            print("\n   >> Available planets for assimilation:")
            for i, planet in enumerate(system.planets):
                if planet.is_assimilated():
                    print(f"   {str(i + 1)}. {''.join(chr(822) + c for c in planet.name)} (Assimilated)") # Put a line through planet names that have been assimilated
                else:
                    print(f"   {i + 1}. {planet.name}")
                        
            type_text("\n   >> Select a planet to assimilate: ")
            try:
                choice = int(input())  # Convert choice to an integer

                if choice not in range(1, 6):
                    print("   >> Invalid system index. Please try again.")
                else:
                    choice -= 1  # Adjust the choice to match the index
                    assimilated = system.assimilate_planet(choice, player)
                    if assimilated:
                        player.level += 1
                        player.increase_attack()
                        player.increase_defence()
                        type_text(f'\n   >> You have assimilated {system.planets[choice].name.upper()}\n')
                        
                        # if planets all assimilated what happens??? add here
                        
                        break # Break back to main loop
                    else:
                        print("   >> Assimilation failed!\n")
                        return player.health # Return player's health before loop broken
                        break # Break the loop
            except ValueError:
                print("   >> Invalid index. Please choose either 1, 2, 3, 4, 5.\n")

    else:
        type_text("   >> Our attack was unsuccessful. Prepare for a counterattack!\n")
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
            type_text("\n   >> State your directives for our next course of action.\n")


# Decrease player life
def decrease_player_life(player, damage_dealt):
    player.take_damage(damage_dealt)
    print(f"Your collective has been damaged! Player health remaining: {player.health}\n")
    if not player.is_alive():
        print("Your collective has been destroyed.")
        player.display_game_finished()
        game_over(delay=0.08)


# Game over
def game_over():
    player.display_game_finished()
    type_text("\n   >> GAME OVER\n")
    sys.exit()

# When run.py is loaded programme runs
if __name__ == "__main__":
    # Load upgrades data
    upgrades = Upgrades.load_upgrades_data("❤️", "⚔️", "🛡️")
    systems_data = load_systems_data()
    # Game initialization
    player = Player()
    systems_data = load_systems_data()
    systems = []

    # Create system objects
    for system_data in systems_data:
        system = System(system_data["name"], system_data["enemy_resistance"], system_data["planets"])
        systems.append(system)

    # Game loop
    s = "\033[32m" # green
    e = "\033[0m"
    game_name = f""" {s}



                ██████╗░░█████╗░██████╗░░██████╗░██╗░░░░░██╗████████╗███████╗
                ██╔══██╗██╔══██╗██╔══██╗██╔════╝░██║░░░░░██║╚══██╔══╝██╔════╝
                ██████╦╝██║░░██║██████╔╝██║░░██╗░██║░░░░░██║░░░██║░░░█████╗░░
                ██╔══██╗██║░░██║██╔══██╗██║░░╚██╗██║░░░░░██║░░░██║░░░██╔══╝░░
                ██████╦╝╚█████╔╝██║░░██║╚██████╔╝███████╗██║░░░██║░░░███████╗
                ╚═════╝░░╚════╝░╚═╝░░╚═╝░╚═════╝░╚══════╝╚═╝░░░╚═╝░░░╚══════╝

    {e}"""
    print(game_name)
    
    # Time delay function
    def type_text(text, delay=0.02):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)

    # Game Icons
    heart_icon = "❤️"
    sword_icon = "⚔️"
    shield_icon = "🛡️"
    power_icon = "⚡️"
    planet_icon = "🌍"
    # cube = "▣"

    
    main_loop = True
    while main_loop == True:
        player.display_stats()
        choice = ""
        type_text("   >> Enter your choice: ")
        while not choice:
            choice = input().lower()
        if choice == "a":
            for i, system in enumerate(systems):
                i + 1 == system.name
        
            while True: 
                try:
                    type_text("\n   >> Select a system to attack: ")
                    system_index = input().lower()
                 
               
                    if system_index == "q": # Breaking the game loop and exiting the system, for expanded player choice
                        game_over()
                    else:
                        system_index = int(system_index) - 1 # Indexing the stystems for player input
                        if system_index in range(len(systems)):
                            selected_system = systems[system_index]
                            if all(planet.is_assimilated() for planet in selected_system.planets):
                                type_text(f"   >> {selected_system.name} is under our control. Please select another destination.\n")
                                continue # Go back to the beginning of the loop.
                                
                            attack_system(selected_system, player)
                            break
                        else:
                            type_text("   >> Invalid system index. Please try again.")
                except ValueError:
                    type_text("   >> Invalid input. Please enter a valid system index 1, 2, 3, 4, 5.")
             
            if not player.is_alive():
                game_over()
        elif choice == "u":
            type_text("\n   >> Available Upgrades:\n") # Display available upgrades
            print(f"   >> Costs power {power_icon} : - 100\n")
            player.upgrades = upgrades  

            for i, upgrade in enumerate(player.upgrades):
                print(f"   {i + 1}. {upgrade.name}")

            choice = int(input("\n   >> Select an upgrade to apply: ")) - 1
            player.apply_upgrade(choice, player.processing)

        elif choice == "l":
            display_leaderboard(player)
            type_text("\n  >> would you like to contine? (y/n) \n")
            type_text("  >> ")
            choice = input().lower()
            if choice == "y":
                continue
            else:
                type_text("\n  >> System exiting ...")
                sys.exit()
        elif choice == "q":
            level = ""
            score = ""
            player.leaderboard_player(level, score)
            game_over()
        else:
            type_text("   >> Invalid key. Please try 'a', 'u', 'l' and 'q'.")
