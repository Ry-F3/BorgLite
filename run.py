import random
import sys
import time
from leaderboard import update_leaderboard, display_leaderboard

# Define the Player class
class Player:
    
    def __init__(self):
        self.name = ""
        self.health = 100
        self.defence = 10
        self.attack = 10
        self.level = 1
        self.processing = 50
        self.score = 0
        self.rank = ""
        self.assimilate_planets = []  # List to store assimilated planets
        self.upgrades = []  # List to store upgrades
        
    def leaderboard_player(self, level, score):  # Player's leaderboard function calling the module leaderboard.py
        """
        This function connects player objects to the leaderboard.py module. 
        It extracts player information and passes it to the update_leaderboard() function, ensuring proper leaderboard updates.
        """    
        player_row = {self.rank, self.name, self.level, self.score}  # Create player_row object to pass to the update_leaderboard function
        update_leaderboard(player)
        
    def apply_upgrade(self, upgrade, processing):
        """
        Apply upgrades to the player's class.
        """
        self.health += upgrade.add_health
        self.defence += upgrade.add_defence
        self.attack += upgrade.add_attack
        
        # Check if it's the initial upgrade application
        if processing >= 100:
            self.processing -= 100
            print("\n   >> Upgrade applied successfully!")
        else:
            print(f"\n   >> Upgrade applied successfully! No processing power consumed.")
        
    def increase_attack(self):  # Increase attack each level
        self.attack += 2
        
    def decrease_attack(self, val):  # Decrease attack each level
        self.attack -= val

    def increase_defence(self, increase):  # Increase defence each level
        increase = increase
        self.defence += increase
        
    def increase_processing(self):  # Increase processing power
        power = random.randint(25,50)
        self.processing += power
        print(f"   >> You recieved a power{power_icon} bonus: {power}")
        
    def decrease_processing(self, amount):  # Decrease processing power
        power = random.randint(10, amount)
        self.processing -= power
        print(f"   >> You loose power : {power} {power_icon}")

    def take_damage(self, damage):  # Take damage from system by individual planets
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
    
    def hacking_damage(self, damage, has_defences):  # Take damage from failure to hack defences
        """
        Player takes damage from the hacking mini game, if the player fails three times to figure out the code.
        """
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
        """
        Reduce power when player chooses to bypass hacking mini game.
        """
        if input_code.lower() == "b" and self.processing >= 100:
            self.processing -= 100
            if self.processing < 0:
                self.processing = 0
        else: 
            self.processing -= processing   # Reduce processing even if input code is incorrect
            if self.processing < 0:
                self.processing = 0

    def is_alive(self):
        return self.health > 0 and self.processing > 0

    def display_stats(self):
        """
        Display game interface featuring ASCII art.
        """
        num_planets = len(self.assimilate_planets)
        self.score = self.processing * num_planets * self.level * self.attack
        
        sw = "\033[37m"  # White
        ew = "\033[0m"
        
        s = "\033[32m"  # Green
        e = "\033[0m"
        
        sr = "\033[31m"  # Red
        er = "\033[0m"
        
        art = f"""  {s}                          
 ________.--------------._______________________________________________________________
 |  ||__| [_]|                    |                                                     |
 |  |     [_]|    {sw}Player Stats:  {ew}{s} | {e}    {sw} Power {power_icon} : {self.processing} {ew}   {s}    |  {e}   {sw}score: {self.score}  {ew} {s}       
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
           
    def display_game_finished(self):  # Display end game score 
        num_planets = len(self.assimilate_planets)
        score = self.processing * num_planets * self.level * self.attack
        type_text(f"\n   >> Final Score: {score}\n")
        print(f"\n   >> Assimilated Planets {planet_icon} : {num_planets}")
        if self.assimilate_planets:
            for planet, destroyed in self.assimilate_planets:
                if destroyed:
                    print(f"   - {planet}")
                else:
                    print(f"   - {planet}")
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
        """
        By using @staticmethod, we indicate that the method is independent of the instance and doesn't require access to instance-specific data. 
        It allows the method to be called directly on the class itself, without the need to create an instance of the class.
        """
        upgrades_data = [
            {
                "name": f"Health Regeneration {heart_icon}  +10  {shield_icon}  +2  {sword_icon}  -2",
                "add_health": 10,
                "add_defence": 2,
                "add_attack": -2,
            },
            {
                "name": f"Adaptive Shielding  {shield_icon}  +10  {heart_icon}  -5 {sword_icon}   +1",
                "add_defence": 10,
                "add_health": -5,
                "add_attack": 1,
            },
            {
                "name": f"Cybernetic Implant  {sword_icon}  +2   {heart_icon}  -10" ,
                "add_attack": 2,
                "add_health": -10,
            }
        ]
        
        upgrades = []
        for upgrade_info in upgrades_data:
            upgrade = Upgrades(**upgrade_info)
            upgrades.append(upgrade)
        
        return upgrades

# Define the Planet Class
class Planet:
    def __init__(self, name, resources, level, population):
        self.name = name
        self.resources = resources
        self.assimilated = False
        self.level = level + 1
        self.attack_points = random.randint(5, 25) + level
        self.defence_points = random.randint(5, 25) + level
        self.has_defences = random.choice([True, False])  # Randomise defences for planets
        self.population = population
    
    def __str__(self):  # planet names contained memory addresses and the __str__ method overrides the default string representation
        return self.name

    def pop(self):
        game = True
        player_wins = False
        while game:
            if not player.is_alive():
                game = False
                break
            player_dice = self.get_dice_roll(self.population)
            ai_dice = self.get_dice_roll(self.population)
            player_rolls = self.roll_dice(player_dice)
            ai_rolls = self.roll_dice(ai_dice)
            print(f"\n   ++ {player.name} rolls {player_dice} dice: {', '.join(map(str, player_rolls))}")
            print(f"   ++ AI rolls {ai_dice} dice: {', '.join(map(str, ai_rolls))}")

            player_total = sum(player_rolls)
            ai_total = sum(ai_rolls)

            if player_total > ai_total:
                print(f"\n   ++ You win the battle!")
                player_wins = True
                break
            elif player_total < ai_total:
                print("\n   >> AI wins! The planet is not assimilated.")
                self.reduce_population(self.population // 2)
                choice = input("\n   >> Do you want to roll again? (y/n): ")
                if choice == 'y':
                    player.decrease_processing(10)
                    print(f"   >> Power left in storage : {player.processing} {power_icon}")
                    continue
                elif choice == 'n':
                    game = False
                    player_wins = False
                    break
            else:
                print("   >> It's a draw! The assimilation attempt failed. Reducing population...\n")
                self.reduce_population(self.population // 4)
                
        return player_wins

    def reduce_population(self, reduction_amount):
        s = "\033[32m"  # Green
        e = "\033[0m"
        self.population -= reduction_amount
        print(f"   >> {self.name}'s population reduced to {s}{self.population}{e} ...")

    @staticmethod
    def get_dice_roll(population):
        if population <= 10000000:
            return 1
        elif population <= 100000000:
            return 2
        else:
            return 3

    @staticmethod
    def roll_dice(num_dice):
        return [random.randint(1, 6) for _ in range(num_dice)]

    def play_dice_game(self):
        s = "\033[32m"  # Green
        e = "\033[0m"

        type_text(f"   >> {self.name}'s population: {s}{self.population}{e}\n")
        continue_playing = True

        while continue_playing:
            assimilated = False
            destroy_planet = False
            while not assimilated:
                if not player.is_alive():
                    type_text("\n   >> You have lost all power...\n")
                    type_text("   >> System failure...\n")
                    game_over()
                    sys.exit()
                type_text("\n   >> The collective must make a choice:")
                type_text(f"\n   - 'roll' the dice to try and assimilate {self.name} and gain power. Costs 10 {power_icon}")
                type_text(f"\n   - 'destroy' all life on {self.name}, but gain 0 power{power_icon}")
                type_text("\n   - 'flee' to fight another day...\n")
                choice = input(f"\n   >> Enter one of the keywords to make your choice: ")

                if choice == "roll":
                    if player.processing >= 10:
                        player.decrease_processing(10)
                        print(f"   >> Power left in storage : {player.processing} {power_icon}")
                        player_wins = self.pop()
                        if player_wins:
                            continue_playing = False
                            assimilated = True
                            break
                        else:
                            continue
                    else:
                        ("   >> Insufficient power")
                elif choice == "destroy":
                    if self.assimilate(player, destroy_planet=True):
                        continue_playing = False
                        assimilated = False
                        break
                    else:
                        continue_playing = False
                        assimilated = True
                        break
                elif choice == "flee":
                    type_text("   >> Are you sure you want to flee? (y/n): ")
                    choice = input()
                    if choice == "y":
                        is_alive = False
                        type_text("   >> We, the Borg, do not flee. Drone terminated ...\n")
                        game_over()
                        sys.exit()
                    elif choice == "n":
                        continue
                    else:
                        type_text("   >> Invalid input.\n")
                else:
                    print("   >> Invalid choice. Please enter 'roll', 'destroy' or 'flee'.\n")
                    
            if assimilated and not destroy_planet:
                self.assimilate(player)
                break
            elif destroy_planet:
                self.assimilate(player, destroy_planet=True)
                break    
                
    def attack_player(self, player):
        # Color Yellow
        ys = "\033[33m"
        ye = "\033[0m"
        damage_dealt = self.attack_points
        player.take_damage(damage_dealt)
        print( f"\n  {ys} -+++-{ye} {self.name} attacks! Player takes {damage_dealt} damage")
        print(f" {ys}  -+++-{ye} Player health remaining:", player.health)
        if not player.is_alive():
            print("\n   >> Player has lost control of the collective.\n")
            player.display_game_finished()
            level = ""
            score = ""
            player.leaderboard_player(level, score)
            print("\n  >> GAME OVER")
            sys.exit()
            
    def assimilate(self, player, destroy_planet=False):
        self.assimilated = True
        if destroy_planet:
            destroyed_planet_name = self.name
            print("   >> The planet is dust and rubble, 0 power {} is harvested.".format(power_icon))
            player.assimilate_planets.append((destroyed_planet_name, True))
            destroy_planet = True
            return True
        else:
            player.processing += self.resources.get("processing", 0)
            player.assimilate_planets.append((self, True))  # Add the assimilated planet to the player's list
            type_text("   ++ You harvested precious resources and gained power {} {}\n".format(self.resources.get("processing", 0), power_icon))
            return False
        
    def is_assimilated(self):
        return self.assimilated

# Define System Class
class System:
    def __init__(self, name, enemy_resistance, planets):
        self.name = name
        self.enemy_resistance = enemy_resistance
        self.planets = planets

    def assimilate_planet(self, planet_index, player, destroy_planet=False):
        """
        The function responsible for assimilating planets and incorporates an embedded hacking mini-game,
        that becomes active, when the planet's defenses are activated.
        """
        if planet_index in range(len(self.planets)):
            planet = self.planets[planet_index]
            if not planet.is_assimilated():
                if not planet.has_defences:
                    planet.play_dice_game()
                if planet.has_defences:  # Hacking mini game initiated randomly if boolean value is True
                    type_text(f"\n   >> {planet.name}'s defences initiated ...\n")
                    type_text("   >> Hacking sequence ... \n")
                    type_text("   >> START \n")
                    print("\n")
                    # ASCII art for code rain characters
                    s = "\033[32m"  # Green
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
                    
                    # Function to generate random fake code to throw the player off
                    def generate_fake_code():
                        code = []
                        for _ in range(1):
                            fake_digit = random.randint(1, 2)  # Random number
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
                            
                        type_text("\n   >> Enter the access code (6 digits): ")
                        input_code = input()
                        # Check if the input code is correct
                        if check_code(input_code, access_code):
                            print("   >> Access granted...")
                            planet.assimilate(player)
                            self.check_assimilation_events(system, player, self.backstories)
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
                    # planet.assimilate(player)
                    self.check_assimilation_events(system, player, self.backstories)
                    return True
            else:
                print("   >>", planet.name, "is already assimilated!")
        else:
            print("Invalid selection")
        return False
    
    # Define a list of backstories
    # Color Green
    s = "\033[32m" 
    e = "\033[0m"
    backstories = [
        {
            "backstory": "   >> While exploring the sector... \n    - Just before completing the assimilation process on the final planet in the system. \n    - Your Borg probes come across an abandoned mining vessel drifting in space.\n    - The vessel appears to have been derelict for some time, It's systems inactive and\n    - its cargo hold potentially containing valuable resources.\n",
            "choice_prompt": f"\n   >> What do you wish to do?\n  \n  {s} [1] {e}Board the mining vessel and scavenge its resources.\n  {s} [2]{e} Put our new weaponry to the test, take no chances.\n {s}  [3]{e} Ignore the vessel and continue with the primary mission\n",
            "choice_1_text": "You decide to board the mining vessel and scavenge its resources.",
            "choice_2_text": "You unleash the destructive power of your new weapons, obliterating the vessel.",
            "choice_3_text": "You ignore the vessel and focus on the primary mission."
        },
        {
            
            "backstory": "   >> As our Borg probes continue their systematic exploration of the sector... \n   - Just before completing the assimilation process on the final planet in the system. \n   - Our advanced scanning technology detects an unusual spatial anomaly nearby.\n   - The anomaly exhibits unique energy patterns, suggesting an undiscovered phenomena.\n",
            "choice_prompt": f"\n   >> What do we wish to do?\n \n   {s}[1]{e} Dispatch a fleet of Borg probes to investigate the spatial anomaly and acquire data.\n  {s} [2]{e} Utilize our advanced weaponry to probe and analyze the anomaly.\n  {s} [3]{e} Disregard the anomaly and proceed with the primary mission, as it poses no threat.\n",
            "choice_1_text": "We deploy a fleet of Borg probes to thoroughly investigate\n   >> the spatial anomaly and assimilate any valuable data.",
            "choice_2_text": "We activate our advanced weaponry to probe and analyze the spatial anomaly,\n   >> ensuring we harness its potential for our collective's advancement.",
            "choice_3_text": "We prioritize the primary mission objectives and disregard the spatial anomaly,\n   >> as it does not present an immediate obstacle to our assimilation efforts."
        }, 
        {
            "backstory": "   >> As our Borg cube progresses with the systematic\n   >> assimilation of the planet's population... \n    - Just as the final stages of assimilation are underway. \n    - Starfleet vessels suddenly emerge from warp, launching an unexpected attack on our cube.\n    - Their actions indicate an intent to disrupt our assimilation process.\n",
            "choice_prompt": f"\n   >> What do we wish to do?\n \n  {s} [1]{e} Mobilize our Borg drones and counter-attack the Starfleet vessels.\n  {s} [2]{e} Activate defensive protocols and shields to withstand the incoming assault.\n  {s} [3]{e} Disregard the Starfleet attack and continue with the assimilation process.\n",
            "choice_1_text": "We mobilize our Borg drones and launch a counter-attack against the Starfleet vessels,\n   >> eliminating the threat to secure our survival and successful assimilation.",
            "choice_2_text": "We activate defensive protocols and reinforce our shields,\n   >> prioritizing the protection of our cube's critical systems and collective resources.",
            "choice_3_text": "We dismiss the Starfleet attack as insignificant interference and proceed with the assimilation process,\n   >> focusing on the completion of our primary mission objectives regardless of their actions."
        },   
    ]
    
    def check_assimilation_events(self, system, player, backstories):
        if all(planet.is_assimilated() for planet in selected_system.planets):
            
            # Randomly select a backstory
            backstory_index = random.randint(0, len(backstories) -1)  # Subtract 1 to stay within the list indices
            backstory = backstories[backstory_index]  # Retrieve the actual backstory dictionary

            backstory_text = backstory["backstory"]
            choice_prompt_text = backstory["choice_prompt"]
            choice_1_text = backstory["choice_1_text"]
            choice_2_text = backstory["choice_2_text"]
            choice_3_text = backstory["choice_3_text"]
            
            type_text(f"\n   >> Drone, you have consolidated power within the {selected_system.name}.\n")
            type_text("   >> We are Borg.\n")
            type_text("   \n")
            type_text(backstory_text)  # Print the randomly chosen backstory
            
            type_text(choice_prompt_text)  # Print the choice prompt
            choice = input("\n   >> Enter your choice 1, 2 or 3 : ")  # Get the player's choice
            
            if choice == "1":
                type_text(f"\n   >> {choice_1_text}\n")
                if backstory_index == 0:
                    result = random.choice([True, False])
                    if result == True:
                        player.increase_processing()
                    elif result == False:
                        player.decrease_processing(50)
                        type_text("   >> SIGNAL LOST ... \n")
                    else:
                        pass
                    
                elif backstory_index == 1:
                    result = random.choice([True, False])
                    if result == True:
                        player.increase_processing()
                    elif result == False:
                        player.decrease_processing(50)
                        type_text("   >> SIGNAL LOST ... \n")
                    else:
                        pass
                    
                elif backstory_index == 2:
                    result = random.choice([True, False])
                    if result == True:
                        player.increase_processing()
                    elif result == False:
                        player.decrease_processing(50)
                        type_text("   >> SIGNAL LOST ... \n")
                    else:
                        pass
                
            elif choice == "2":
                type_text(f"\n   >> {choice_2_text}\n")
                if backstory_index == 0:
                    result = random.choice([True, False])
                    if result == True:
                        player.increase_attack()
                        print(f"   >> You get an attack {sword_icon}    bonus: +2")

                    elif result == False:
                        player.decrease_attack(4)
                        type_text("   >> Systems malfuntioning ... \n")
                        print(f"   >> You loose attack {sword_icon}   points: - 2")
                    else:
                        pass
                    
                if backstory_index == 1:
                    result = random.choice([True, False])
                    if result == True:
                        player.increase_attack()
                        print(f"   >> You get an attack {sword_icon}   bonus: +2")

                    elif result == False:
                        player.decrease_attack(4)
                        type_text("   >> Systems malfuntioning ... \n")
                        print(f"   >> You loose attack {sword_icon}   points: - 2")
                    else:
                        pass
                    
                if backstory_index == 2:

                    result = random.choice([True, False])
                    if result == True:
                        player.increase_defence(20)
                        print(f"   >> You get a defence {shield_icon}  bonus: +20")

                    elif result == False:
                        if player.defence > 0:
                            player.defence = 0 - 2
                            print(f"   >> Our defences have STOPPED regenerating and will need time to repair.")
                        else:
                            player.decrease_attack(7)
                            type_text("   >> Systems malfuntioning ... \n")
                            print(f"   >> You loose some attack points {sword_icon}: -5")
                    else:
                        pass
            
            elif choice == "3":
                type_text(f"\n   >> {choice_3_text}\n")
                if backstory_index == 0:
                    player.decrease_processing(10)
                    type_text("   >> A small amount of power was expended for this mission ... \n")
                if backstory_index == 1:
                    player.decrease_processing(10)
                    type_text("   >> A small amount of power was expended for this mission ... \n")
                    
                if backstory_index == 2:
                    player.decrease_processing(10)
                    type_text("   >> A small amount of power was expended for this mission ... \n")
                
            else:
                type_text("   >> Invalid input. Please enter 1 or 2.")
            # Handle invalid choice

# Define AttackManager Class   
class AttackManager:
    used_resistance_levels = []  # Class variable to store used resistance levels

    @staticmethod
    def attack(system, attack_power, player):  # Update the resistance level within a randomised range
        """
        The attack method is a static method because it doesn't need access to any specific instance or class variables.
        It takes the system, attack_power, and player as parameters and performs the attack calculations accordingly.
        """
        # Color Yellow
        ys = "\033[33m"
        ye = "\033[0m"
        if player.level < 6:
            lower_bound = max(1 + random.randint(-3, 3), 1)
            upper_bound = 15 + random.randint(-3, 3)
            resistance_level = AttackManager.get_unique_resistance_level(lower_bound, upper_bound)
            system.enemy_resistance = resistance_level
        elif player.level >= 6 and player.level <= 10:
            lower_bound = max(18 + random.randint(-3, 5), 1)
            upper_bound = 30 + random.randint(-3, 5)
            resistance_level = AttackManager.get_unique_resistance_level(lower_bound, upper_bound)
            system.enemy_resistance = resistance_level
        elif player.level >= 11 and player.level <= 16:
            lower_bound = max(35 + random.randint(-6, 5), 1)
            upper_bound = 55 + random.randint(-3, 5)
            resistance_level = AttackManager.get_unique_resistance_level(lower_bound, upper_bound)
            system.enemy_resistance = resistance_level
        else:
            lower_bound = max(45 + random.randint(-3, 10), 1)
            upper_bound = 75 + random.randint(-3, 10)
            resistance_level = AttackManager.get_unique_resistance_level(lower_bound, upper_bound)
            system.enemy_resistance = resistance_level
        
        success_chance = 0  # Initialize success_chance to zero
        
        if system.enemy_resistance !=0:
            success_chance = attack_power / system.enemy_resistance
        print(f"\n  {ys} -+++- {ye}Attacking", system.name, "with resistance level:", system.enemy_resistance)
        print(f" {ys}  -+++-{ye} Engagement Probability: {round(success_chance, 2)}\n")
        return success_chance >= 1

    @classmethod
    def get_unique_resistance_level(cls, lower_bound, upper_bound):  # Generate a unique resistance level that hasn't been used before
        """
        The get_unique_resistance_level method is a class method because it needs access to the 
        used_resistance_levels class variable to check for unique resistance levels. 
        The method generates a random resistance level within the given range and ensures
        it hasn't been used before by checking against the used_resistance_levels list. 
        If the generated resistance level is not unique, it generates another one until a unique level is found.
        Once a unique level is obtained, it is added to the used_resistance_levels list to prevent reuse.
        """
        resistance_level = random.randint(lower_bound, upper_bound)
        while resistance_level in cls.used_resistance_levels:
            resistance_level = random.randint(lower_bound, upper_bound)
        cls.used_resistance_levels.append(resistance_level)
        return resistance_level
    
# Define the help class  
class HelpSection:
    # Color Yellow
    ys = "\033[33m"
    ye = "\033[0m"
    
    def display(self):
        ys = "\033[33m"
        ye = "\033[0m"
        type_text(f"\n   >> {ys}Need Help?:{ye}\n")
        print("   1. Level Up")
        print("   2. Upgrades")
        print("   3. Objective")
        print("   4. System Names")
        print("   5. Exit")

    def show_level_up(self):
        ys = "\033[33m"
        ye = "\033[0m"
        print(f"\n   >>{ys} Level Up:{ye}")
        type_text("   >> As you level up, your baseline values increase.\n")
        type_text("      - Each planet assimilated increases the drone's level.\n")
        type_text("      - Each level up adds +2 to your attack and +2 to your defense.\n")
        type_text("      - Baseline values represent your base attack and defense without upgrades.\n")

    def show_upgrades(self):
        ys = "\033[33m"
        ye = "\033[0m"
        print(f"\n   >>{ys} Upgrades:{ye}")
        type_text("   >> Upgrades cost power and are applied immediately and affect your stats.\n")
        type_text("      - Each upgrade's values are subsequently applied per level.\n")
        type_text("      - When a new upgrade is selected, the previous upgrade is replaced.\n")
        type_text("      - Upgrades can enhance your attack, defense, or other abilities.\n")
        type_text("      - Be wary of the upgrade deficiencies that may adversely impact your stats.\n")

    def show_objective(self):
        ys = "\033[33m"
        ye = "\033[0m"
        print(f"\n   >> {ys}Borg Directive:{ye}")
        type_text("   >> The main objective of the game is to assimilate planets and collect power.\n")
        type_text("   >> Assimilation of each planet grants you power as a valuable resource.\n")
        type_text("   >> Power assimilated contributes to your collective score.\n")
        type_text("   >> Assimilated power fuels the enhancement of your drone.\n")
        type_text("   >> Your ultimate goal is to achieve a high score and secure a place on the leaderboard.\n")

    def show_system_names(self):
        ys = "\033[33m"
        ye = "\033[0m"
        print(f"\n   >> {ys}System Names:{ye}")
        type_text("   1. ALPHA\n")
        type_text("   2. BETA\n")
        type_text("   3. GAMMA\n")
        type_text("   4. DELTA\n")
        type_text("   5. EPSILON\n")

# Load systems data
def load_systems_data():
    systems_data = [
        {
            "name": "Alpha System",
            "enemy_resistance": random.randint(25, 60),
            "planets": [
                Planet("Earth", {"processing": random.randint(20, 50)}, 1, random.randint(10000, 1000000000)),
                Planet("Vulcan", {"processing": random.randint(20, 50)}, 1, random.randint(10000, 1000000000)),
                Planet("Klingon", {"processing": random.randint(20, 50)}, 1, random.randint(10000, 1000000000)),
                Planet("Romulus", {"processing": random.randint(20, 50)}, 1, random.randint(10000, 1000000000)),
                Planet("Andoria", {"processing": random.randint(20, 50)}, 1, random.randint(10000, 1000000000))
            ]
        },
        {
            "name": "Beta System",
            "enemy_resistance": random.randint(9, 60),
            "planets": [
                Planet("Cardassia Prime", {"processing": random.randint(20, 50)}, 1, random.randint(10000, 1000000000)),
                Planet("Bajor", {"processing": random.randint(20, 50)}, 1, random.randint(10000, 1000000000)),
                Planet("Ferenginar", {"processing": random.randint(20, 50)}, 1, random.randint(10000, 1000000000)),
                Planet("Qo'noS", {"processing": random.randint(20, 50)}, 1, random.randint(10000, 1000000000)),
                Planet("Trill", {"processing": random.randint(20, 50)}, 1, random.randint(10000, 1000000000))
            ]
        },
        {
            "name": "Gamma System",
            "enemy_resistance": random.randint(9, 60),
            "planets": [
                Planet("Betazed", {"processing": random.randint(20, 50)}, 1, random.randint(10000, 1000000000)),
                Planet("Risa", {"processing": random.randint(20, 50)}, 1, random.randint(10000, 1000000000)),
                Planet("Tellar Prime", {"processing": random.randint(20, 50)}, 1, random.randint(10000, 1000000000)),
                Planet("Q'uorath", {"processing": random.randint(20, 50)}, 1, random.randint(10000, 1000000000)),
                Planet("Federation Outpost 112", {"processing": random.randint(20, 50)}, 1, random.randint(10000, 1000000000))
            ]
        },
        {
            "name": "Delta System",
            "enemy_resistance": random.randint(1, 30),
            "planets": [
                Planet("Vorta", {"processing": random.randint(20, 50)}, 1, random.randint(10000, 1000000000)),
                Planet("Founders' Homeworld", {"processing": random.randint(20, 50)}, 1, random.randint(10000, 1000000000)),
                Planet("Breen Homeworld", {"processing": random.randint(20, 50)}, 1, random.randint(10000, 1000000000)),
                Planet("Talax", {"processing": random.randint(20, 50)}, 1, random.randint(10000, 1000000000)),
                Planet("Ocampa", {"processing": random.randint(20, 50)}, 1, random.randint(10000, 1000000000))
            ]
        },
        {
            "name": "Epsilon System",
            "enemy_resistance": random.randint(9, 50),
            "planets": [
                Planet("Nimbus III", {"processing": random.randint(20, 50)}, 1, random.randint(10000, 1000000000)),
                Planet("Rigel VII", {"processing": random.randint(20, 50)}, 1, random.randint(10000, 1000000000)),
                Planet("Sheliak", {"processing": random.randint(20, 50)}, 1, random.randint(10000, 1000000000)),
                Planet("Tribble Homeworld", {"processing": random.randint(20, 50)}, 1, random.randint(10000, 1000000000)),
                Planet("Deneb IV", {"processing": random.randint(20, 50)}, 1, random.randint(10000, 1000000000))
            ]
        }
    ]
    return systems_data
    
# Assimilate a planet within a system
def attack_system(system, player):
    initial_upgrade_applied = True
    success = AttackManager.attack(system, player.attack, player)
    if success:
        while True:
            main_loop= False  # Stop the main loop
             
            type_text("   >> We are Borg. Existence as you know it is over. Resistance is futile.\n")
            # Display the available planets for assimilation
            print("\n   >> Available planets for assimilation:")
            for i, planet in enumerate(system.planets):
                s = "\033[32m"  # Green
                e = "\033[0m"
                if planet.is_assimilated():
                    print(f"   {str(i + 1)}.{s} {''.join(chr(822) + c for c in planet.name)} {e}")  # Put a line through planet names that have been assimilated
                else:
                    print(f"   {i + 1}. {planet.name}")
                        
            type_text("\n   >> Select a planet to assimilate: ")
            try:
                choice = int(input())  # Convert choice to an integer

                if choice not in range(1, 6):
                    print("   >> Invalid system index. Please try again.")
                else:
                    choice -= 1   # Adjust the choice to match the index
                    assimilated = system.assimilate_planet(choice, player, destroy_planet=True)
                    if assimilated:
                        player.level += 1
                        player.increase_attack()
                        player.increase_defence(increase = 2)
                        type_text(f"\n   >> You have assimilated {system.planets[choice].name.upper()} ")
                        choice = input("\n   >> Enter any key: ")
                        if choice == '':  
                            if selected_upgrade is not None:
                                if initial_upgrade_applied:
                                    player.apply_upgrade(selected_upgrade, 0)  # Apply the upgrade without deducting processing power
                                else:
                                    player.apply_upgrade(selected_upgrade, player.processing)
                                    initial_upgrade_applied = True
                            break
                        # if planets all assimilated what happens??? add here
                        
                        break  # Break back to main loop
                    else:
                        print("   >> Assimilation failed!\n")
                        return player.health  # Return player's health before loop broken
                        break  # Break the loop
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
            print("   >> We have successfully counterattacked the enemy planet!")
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
        
# Time delay function
def type_text(text, delay=0.02):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

# Game over
def game_over():
    level = ""
    score = ""
    player.display_game_finished()
    player.leaderboard_player(level, score)
    type_text("\n   >> GAME OVER\n")
    sys.exit()

# When run.py is loaded programme runs
if __name__ == "__main__":
    

    # Load upgrades data
    upgrades = Upgrades.load_upgrades_data("❤️", "⚔️", "🛡️")
    systems_data = load_systems_data()
    
    s = "\033[32m"  # Green
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
    
    # Game initialization
    type_text("                     Drone, you are now part of the Collective.")
    print("")
    type_text("\n                     >> Enter your name:")
    player_name = input(" ")
    player = Player()
    player.name = player_name
    systems_data = load_systems_data()
    systems = []

    # Create system objects
    for system_data in systems_data:
        system = System(system_data["name"], system_data["enemy_resistance"], system_data["planets"])
        systems.append(system)
        
    # Game Icons
    heart_icon = "❤️"
    sword_icon = "⚔️"
    shield_icon = "🛡️"
    power_icon = "⚡️"
    planet_icon = "🌍"
    # cube = "▣"

    # Game loop
    main_loop = True
    selected_upgrade = None
    initial_upgrade_applied = False

    upgrade_applied = False
    while main_loop:
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
            
                    if system_index == "q":  # Breaking the game loop and exiting the system, for expanded player choice
                        level = ""
                        score = ""
                        player.leaderboard_player(level, score)
                        game_over()
                    else:
                        system_index = int(system_index) - 1  # Indexing the stystems for player input
                        if system_index in range(len(systems)):
                            selected_system = systems[system_index]
                            if all(planet.is_assimilated() for planet in selected_system.planets):
                                type_text(f"   >> {selected_system.name} is under our control. Please select another destination.\n")
                                continue  # Go back to the beginning of the loop.
                            attack_system(selected_system, player)
                            
                            if all(all(planet.is_assimilated() for planet in system.planets) for system in systems):
                                type_text("\n   >> Congratulations! You have assimilated all systems. You win!\n")
                                game_over()    
                            break
                        else:
                            type_text("   >> Invalid system index. Please try again.")
                except ValueError:
                    type_text("   >> Invalid input. Please enter a valid system index 1, 2, 3, 4, 5.")
             
            if not player.is_alive():
                game_over()
        elif choice == "u":
            type_text("\n   >> Available Upgrades:\n")  # Display available upgrades
            print(f"   >> Costs power {power_icon} : - 100\n")
            upgrades_available = [upgrade for upgrade in upgrades if upgrade not in player.upgrades] 
            
            while True:
                for i, upgrade in enumerate(upgrades_available):
                    print(f"   {i + 1}. {upgrade.name}")
                    
                choice = input("\n   >> Select an upgrade to apply (or 'b' to go back): ")

                if choice == "b":  # Give the player the option to go back to the beginning of the outer loop
                    break
                
                try:
                    """
                    The player has the option to apply an upgrade costing 100 power, 
                    these values will be applied immediately and each subsequent level.
                    Until the upgrade is replaced.
                    """
                    choice = int(choice) - 1 
                    if choice in range(len(upgrades_available)):
                        selected_upgrade = None
                        selected_upgrade = upgrades_available[choice]
                      
                        if player.processing >= 100:
                            player.apply_upgrade(selected_upgrade, player.processing)
                            initial_upgrade_applied = True
                            upgrade_applied = True
                            previous_upgrade = selected_upgrade  # Keep track of the previously selected upgrade
                        else:
                            type_text("\n   >> Insufficient processing power. Upgrade not applied.\n")
                            if upgrade_applied:
                                selected_upgrade = previous_upgrade  # Revert back to the previously selected upgrade
                                break
                            elif not upgrade_applied:
                                selected_upgrade = None
                                break
                        break
                            
                except ValueError:
                    type_text("   >> Invalid input. Please enter a valid upgrade index or 'b' to go back.\n")       

        elif choice == "l":
            display_leaderboard(player)
            type_text("\n  >> would you like to continue? (y/n) \n")
            type_text("  >> ")
            choice = input().lower()
            if choice == "y":
                continue
            else:
                type_text("\n  >> System exiting ...")
                sys.exit()
        elif choice == "h":  # Help section 
            help_section = HelpSection()
            while True:
                help_section.display()
                type_text("\n   >> Enter the number of the section you want to view: ")
                section_choice = input()

                if section_choice == "1":
                    help_section.show_level_up()
                elif section_choice == "2":
                    help_section.show_upgrades()
                elif section_choice == "3":
                    help_section.show_objective()
                elif section_choice == "4":
                    help_section.show_system_names()
                elif section_choice == "5":
                    type_text("\n   >> Exiting Help Section...\n")
                    print("")
                    break
                else:
                    type_text("\n   >> Invalid section choice. Please enter a number between 1 and 5.")

                print("\n   >> Press any key to continue", end=" ")
                input()
                
        elif choice == "q":
            game_over()
        else:
            type_text("   >> Invalid key. Please try 'a', 'u', 'l' and 'q'.")
           
