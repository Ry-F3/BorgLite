import random

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
    for i in range(len(input_code)):
        if input_code[i] != str(access_code[i]):
            return False
    return True

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

# Start the code rain animation
print_code_rain(access_code)

# Game loop
attempts_left = 3
while attempts_left > 0:
    # Read user input
    input_code = input("Enter the access code (6 digits): ")

    # Check if the input code is correct
    if check_code(input_code, access_code):
        print("Access granted. Hacking successful!")
        break
    else:
        attempts_left -= 1
        if attempts_left > 0:
            print("Access denied. {} attempts left.".format(attempts_left))
        else:
            print("Access denied. Hacking failed.")

# Automate cracking if failed attempts
if attempts_left == 0:
    print("Automated cracking in progress...")
    automated_code = automate_crack(access_code)
    print("Access code: {}".format(automated_code))
