import random 
import sys

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