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
        
    def assimilated(self):
        self.assimilated = True
        
    def is_assimilated(self):
        return self.assimilated
        
# Main game loop
def main_game_loop():
    
    while True:
        
    

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