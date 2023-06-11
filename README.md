

# BorgLite 

# Code Institute Portfolio Project 3: Python Essentials - Back End CLI Game Deployed Via Heroku.
### To view the project please [click here](https://borglite.herokuapp.com/).
<br>

![Index page screenshot](/assets/images/amiresponsive.png)


### **Borglite Background:** 
A contemporary CLI (Command-Line Interface) game inspired by Star Trek and Retro Text-Based Games.
As a player, you have the unique opportunity to step into the shoes of one of the fiercest enemies in the universe: the Borg.

### **Inspired by Star Trek:**
Borglite takes inspiration from the vast and captivating Star Trek universe, renowned for its compelling narratives and memorable characters. In Borglite, you assume the role of a Borg, a cybernetic species driven by a relentless pursuit of perfection. Immerse yourself in the depths of space as you navigate through captivating storylines and encounter familiar Star Trek elements, all while striving to fulfill the Borg's insatiable thirst for power and assimilation.

### **Retro Text-Based Games:**
Borglite pays homage to the nostalgia of retro text-based games, where the power of imagination and storytelling thrived. With text-based interactions, Borglite encourages you to unleash your creativity and strategic thinking as you make decisions, engage in battles, and assimilate planets. The simple yet immersive text-based interface harks back to a bygone era of gaming while infusing it with contemporary twists.

### **Contemporary Strategic Gameplay:**
Borglite brings a contemporary edge to its strategic gameplay, allowing you to devise intricate plans and execute them to conquer systems and expand the Borg's influence. Engage in intense battles, utilize upgradeable abilities, and strategically assimilate planets to amass power and further your dominance. Each decision you make has consequences, requiring careful thought and consideration to outwit your opponents and climb the leaderboard.

### **Competitive Leaderboard:**
Borglite introduces a competitive element through its leaderboard system, pitting you against other players vying for supremacy. As you progress through the game, your actions and achievements contribute to your rank on the leaderboard. Can you rise above other players, asserting your dominance as the ultimate Borg commander? Climb the ranks, showcase your strategic prowess, and cement your place as a force to be reckoned with in the Borglite universe.

### **Gameplay:**

The objective of Borglite is to conquer various systems by attacking enemy planets and assimilating them under your control. <br>
Here's an expanded explanation of the gameplay:
<br>

* The game displays a list of available systems to attack. Each system is represented by an index number. Choose a system by entering the corresponding index.
* Once a system is selected, your drone will engage in battle with the enemy planets within that system. The battle outcome is determined by your drone's attack power and the enemy planet's resistance level.
* If your drone successfully defeats all the enemy planets in a system, you can assimilate the system and gain control over it. Assimilating a system brings it under your influence and contributes to your overall progress.
* As you progress in the game, you can earn power by assimilating planets. Power is a valuable resource that can be used to apply upgrades and enhance your drone's abilities. It can also be used to bypass the hacking mini game.
* The game provides a range of available upgrades that you can apply to your drone. These upgrades can increase your drone's attack power, defence, or health. Use your earned power strategically to choose the most beneficial upgrades.
* Along the way, you may encounter a hacking mini-game. This mini-game is randomly initiated when you breach a system without facing a counter-offensive from the enemy. If the hacking mini-game is activated, you will have the opportunity to play it, which acts as planetary defences.
* The aim of the game is to assimilate all the planets in that system while collecting as much power as possible. The game entails strategic decisions to progress and achieve a high score.
* The leaderboard keeps track of the top players based on their level and score. Aim to achieve the highest level and score possible to secure your position on the leaderboard and compete with other players.
* After viewing the leaderboard, you can choose to continue playing and conquer more systems, assimilate planets, and increase your score. Alternatively, you can choose to exit the game and have your level and score saved on the leaderboard, but only the top 10 are visible.
* By assimilating all planets, utilising upgrades wisely, engaging in hacking mini-games, and collecting power, you can strive for the highest score and dominate the leaderboard in Borglite.


## **Scope**

<br>

1. Gameplay Mechanics:

    * Interact with the game through a Command-Line Interface (CLI).
    * Engage in strategic battles and conquer enemy systems.
    * Assimilate planets to expand the Borg's control and gain power.
    * Utilize upgradeable abilities to enhance your drone's capabilities.
    * Encounter a hacking mini-game when breaching systems without counter-offensive.
    * Aim to achieve the highest score on the competitive leaderboard.

<br>    

2. Setting and Theme:

    * Draw inspiration from the Star Trek universe, particularly the formidable Borg species.
    * Combine elements of the Star Trek lore with a retro text-based gaming experience.
    * Create a contemporary twist by infusing strategic gameplay and leaderboard competition.

<br>    


3. User Interface and Experience:

    * Develop a user-friendly CLI interface for smooth interaction.
    * Provide clear instructions and prompts to guide the player through the game.
    * Implement intuitive controls and responsive gameplay mechanics.

<br>    

3. Game Progression and Difficulty:

    * Design a progression system that challenges players to strategize and adapt.
    * Increase the difficulty gradually as the player advances through the game.
    * Provide opportunities for players to unlock new abilities or upgrades.

<br>    

4. Leaderboard and Competition:

    * Implement a competitive leaderboard to showcase players' levels and scores.
    * Enable players to compare their progress and compete for the top positions.
    * Ensure fairness and accuracy in leaderboard calculations and updates.

<br>    

5. Limitations and Constraints:

    * Focus the gameplay on the Borg perspective and their conquest for assimilation.
    * Balance the game mechanics to provide an enjoyable and challenging experience.
    * Limit the scope to the CLI interface, emphasizing text-based interactions.
    * Using backend technologies brings certain challenges in terms of delivering a unique and engaging experience. The visual representations used in Borglite, specifically ASCII art, aims to create a visually distinctive atmosphere while maintaining the retro and text-based aesthetic.
    * By defining these aspects within the scope, the development of Borglite can be structured and executed effectively, ensuring a cohesive and engaging gaming experience for players.

 <br>   

## **Audience**

Borglite is designed for fans of the Star Trek universe, retro gaming enthusiasts, and players who enjoy strategic gameplay. The game appeals to those seeking a unique experience that combines elements from the iconic Star Trek franchise, nostalgic retro text-based games, and strategic challenges. Whether you are a Star Trek enthusiast looking to step into playing as the Borg, or a fan of retro gaming seeking a captivating adventure, or a player who enjoys strategic decision-making and competing for high scores, Borglite offers an accessible and visually distinctive journey. The game's intuitive command-line interface (CLI) and simplistic ASCII art provide a creative and engaging experience for a wide range of players.

## **User Stories**


* As a Star Trek fan, I want to experience the thrill of playing as the Borg, one of the iconic species from the franchise, to immerse myself in the vast and captivating Star Trek universe.

* As a retro gaming enthusiast, I am excited to engage in a text-based gaming experience reminiscent of classic games, where the power of imagination and storytelling take center stage.

* As a strategic player, I enjoy making thoughtful decisions and planning my moves strategically. I'm looking forward to devising intricate plans and executing them to conquer systems and expand the Borg's influence.

* As a competitive gamer, I thrive on challenges and enjoy comparing my progress with other players. The presence of a competitive leaderboard in Borglite adds an extra layer of motivation, as I can climb the ranks, showcase my strategic prowess, and compete with other players for the top positions.

* As a player seeking an accessible and visually distinctive journey, I appreciate the user-friendly Command-Line Interface (CLI) of Borglite. The simplicity of text-based interactions combined with visually appealing ASCII art creates a unique and engaging experience.

* As a player progressing through the game, I want to face increasing levels of difficulty to keep the gameplay challenging and engaging. I'm excited to unlock new abilities or upgrades as I advance, adding depth to my gameplay and rewarding my progression.

* As a player interested in the Star Trek lore, I look forward to encountering familiar elements from the franchise while playing Borglite. Whether it's encountering well-known characters or experiencing captivating storylines, I expect Borglite to provide a rich and immersive Star Trek experience.

* As a player concerned about fairness and accuracy, I trust that the leaderboard calculations and updates in Borglite are reliable. I want to be confident that my achievements and progress accurately reflect my performance in the game.

* As a player seeking a captivating adventure, I appreciate the well-defined scope of Borglite. By combining elements from the Star Trek universe, retro text-based games, and strategic challenges, Borglite offers a cohesive and engaging gaming experience that keeps me invested and entertained.

* As a player who enjoys exploring different gameplay mechanics, I'm excited to engage in strategic battles, upgrade my abilities, and experience the hacking mini-game in Borglite. These varied gameplay elements add depth and variety to the overall gaming experience.


# **Deployment**

To deploy the Borglite game on Heroku, follow these steps:

* Create a Heroku account if you don't have one.

* Once you're logged into Heroku, go to the "Apps" tab in the dashboard.

* Click on the "New" button and choose "Create a new app".

* Give your app a unique name.

* Choose a region that's closest to your target audience.

* Click the "Create" button to create your app.

* Open the app you just created and navigate to the "Settings" tab.

* Scroll down to the "Config Vars" section and click on the "Add" button.

* In the "KEY" field, enter "PORT" and in the "VALUE" field, enter "8000".

* In the "Buildpacks" section, click on the "Add" button.

* Add two buildpacks in the following order: Python and Node.js. The order is important.

* Now, navigate to the "Deploy" tab.

* In the "Deployment method" section, choose "GitHub" and connect your GitHub account.

* Select the repository that contains your Borglite game.

* Scroll down to the "Manual deploy" section.

* Choose the branch you want to deploy and click the "Deploy branch" button.

* Heroku will start deploying your app. Once the deployment is complete, you can access your app by clicking on the "View" button.

* You may run into potential errors if you have not To created a requirements.txt file, open your terminal or command prompt and run the following command:  <code>pip3 freeze > requirements.txt</code>

* This command generates a requirements.txt file based on the installed Python packages in your virtual environment. It captures the package names and their corresponding versions.

<br>

### **To run the Borglite game locally on your machine, follow these steps:** 

<br>

1. Ensure you have Python 3 installed on your machine.

2. Download the Borglite game source code from the GitHub repository. You can do this by clicking on the "Download ZIP" button on the repository page and extracting the contents to a folder of your choice. Alternatively, you can use the following command to clone the repository: <br>  <code> git clone https://github.com/your-username/your-repo.git </code>

4. Open a terminal or command prompt and navigate to the folder where you placed the game's source code.

5. To install the required dependencies, run the following command:  <code> pip install -r requirements.txt </code>

6. This will install all the necessary packages, however you may need install additional libraries that were used for the development of Borglite:  <code> pip install google-auth google-auth-oauthlib gspread tabulate </code>

<br>

### **Additionally, if you are using the Google Sheets API for the game, you need to provide your API credentials. Follow these steps to add your credentials as environment variables:**

<br>

a. Obtain the JSON file containing your API credentials from the Google Cloud Console.

b. Rename the JSON file to "credentials.json" and place it in the root directory of the Borglite game.

c. Copy the name of JSON file to .gitignore because it contains sensitive information about your google account.

d. Add boilerplate code for your API:
 <br>  
 <code>import gspread <br>
from google.oauth2.service_account import Credentials <br>


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets", <br>
    "https://www.googleapis.com/auth/drive.file", <br>
    "https://www.googleapis.com/auth/drive" <br>
    ]</code>

e.  You are now ready to run the game locally. Execute the following command:  <code> python3 game.py </code>


# **Python Game Logic Overview**
The Python game code represents a text-based strategy game where the player controls a collective of drones tasked with assimilating planets in different systems. The game follows a turn-based approach and involves attacking enemy systems, upgrading the player's abilities, and managing resources.

<br>

![flowchart](/assets/images/flowchart.png)

<br>

### **Main While loop**
<br>

* Loop Initialization:
    *   <code>main_loop = True <br>
            while main_loop == True:
        </code>
    *  The main_loop variable is set to True, indicating that the loop should continue running until explicitly terminated. The loop condition checks whether main_loop is still True, and if so, the loop body is executed.

<br>

* Choice Input and Processing:
    * The player is prompted to make a choice by entering a character. The input is processed and compared using an if-elif-else statement to determine the appropriate action based on the chosen option.
    * The player's choice is stored in the choice variable, which is initially an empty string. The <code>type_text()</code> function is used to display the prompt message to the player. The loop continues to prompt for input until a valid choice is entered (i.e., choice is not an empty string).

<br>

* Choice Handling:
    * Once the player's choice is obtained, it is processed to perform the corresponding action. The if-elif-else statement handles the different possible choices:
    * If the choice is <code>"a"</code>, the player is presented with a list of available systems to attack. They can select a system by entering the corresponding index.
    * If the choice is <code>"u"</code>, the available upgrades are displayed, and the player can choose an upgrade to apply by entering the corresponding index.
    * If the choice is <code>"l"</code>, the leaderboard is displayed, and the player is prompted to continue or exit the game.
    * If the choice is <code>"q"</code>, the player's score and level are saved to the leaderboard, and the game is terminated.
    * If none of the above options are chosen, an error message is displayed.

<br>

* Game Over Handling:
    * If the player's health reaches zero during an attack or if the player chooses to exit the game, the <code>game_over()</code> function is called to end the game.
    * <code>if not player.is_alive(): <br>  
    game_over() </code>
    * The <code>is_alive()</code> method checks if the player's health is zero or below, indicating that the player has been defeated.

<br>

* Continuation of Loop:
    * After completing an action, the loop continues from the beginning, displaying the player's stats and prompting for a new choice. This ensures that the game progresses in a continuous cycle until it is terminated.

### **Secondary While Loop: Attack System()**
The <code>attack_system(system, player)</code> function represents a secondary loop that is executed when the player successfully attacks a system. This loop allows the player to choose a planet from the attacked system to assimilate.

* Assimilation of a Planet:
    * Once the player successfully attacks a system, the <code>attack()</code> method from the AttackManager class is called to determine the success of the attack. If the attack is successful, the assimilation process begins.
    * A while loop is used to handle the planet assimilation process: <code>while True:</code>

<br>

* Stopping the Main While Loop:
    * At the start of the assimilation loop, the main_loop variable is set to False to stop the main game loop. This ensures that the player can only select a planet for assimilation and cannot perform any other actions until the process is complete: <code>main_loop = False</code>

<br>

* Displaying Available Planets:
    * The available planets for assimilation are displayed to the player. Each planet is listed with its corresponding index.
    * Once assimilated planets have a line passing through them as a visual to the player to remind them that they have assimilated that specific planet.
    * <code>if planet.is_assimilated(): <br>
        print(f"   {str(i + 1)}. {''.join(chr(822) + c for c in planet.name)} (Assimilated)") </code>

<br>

* Selecting a Planet for Assimilation:
    * The player's choice is obtained and validated. If the choice is valid, the <code>assimilate_planet()</code> method of the system object is called to assimilate the selected planet. If assimilation is successful, the player's level, attack power, and defense power are increased accordingly. A success message is displayed to the player.

<br>

* Counterattack if Assimilation Fails:
    * If the assimilation fails, indicating that the player's attack power was insufficient, a counterattack is initiated by randomly selecting a planet from the system to attack the player:
    * <code>enemy_planet = random.choice(system.planets) <br>
      enemy_planet.attack_player(player)</code>
    * The <code>attack_player()</code> method of the enemy_planet is called to damage the player. If the player's health reaches zero, the game over condition is triggered.

<br>

* Outcome Based on Attack Power:
    * After the counterattack, the outcome is determined based on the player's attack power and the enemy system's resistance. If the player's attack power is greater than the system's resistance, the enemy planet is ready to be assimilated and removed from the system as a player choice.
    * <code>system.planets.remove(enemy_planet)</code>

<br>

* Directive for Next Course of Action:
    * Once the assimilation or counterattack process is complete, the loop prompts the player to state their directives for the next course of action.
    * The player can then choose their next action by entering the corresponding choice in the main game loop.

<br>

### **Player and Upgrades**

The Player class represents the player's collective and tracks their attributes. It has properties like name, health, attack_power, defense_power, and level. The player can apply upgrades to enhance their abilities.

The upgrades are defined in the Upgrades class, which uses a dictionary to store the upgrade details. Each upgrade is associated with a key, such as 'processing_power', and the corresponding value represents the enhancement it provides.

### **Systems and Planets**

The game consists of different systems, each represented by the System class. The System class has properties like name, enemy_resistance, and planets (a list of Planet objects).

The system and planet data is loaded from the <code>load_systems_data()</code> function. It uses a dictionary to store the system details, with each key representing the system name and its corresponding value containing the system's attributes. Similarly, each planet within a system is represented as a dictionary.

To access the planets within a system, the code iterates over the planets list using a for loop. This allows the game to retrieve and manipulate individual planets within a system.

### **Attack and Assimilation**

The AttackManager class plays a central role in managing the attack mechanism in the game. It calculates the success chance of an attack by considering both the player's attack power and the resistance level of the enemy system. By utilizing formulas and probability calculations, the game determines the outcome of the attack.

If the attack is successful, meaning the player's attack power exceeds the enemy system's resistance level, the <code>attack_system()</code> function is invoked. This function presents the player with a list of available planets within the system for assimilation and allows them to choose a target. The code employs iteration to display the available planets and handles the planet selection process.

On the other hand, if the attack fails due to the resistance level being too high, the enemy system retaliates with a counterattack. A specific planet from the system is selected to launch the counterattack on the player. This adds an element of challenge and unpredictability to the game, as the player must be prepared to defend against such counterattacks.

To ensure greater variation in the game and make it progressively challenging, the resistance levels of the systems are stored in a variable called <code>used_resistance_levels</code>. This variable keeps track of the resistance levels that have been used before, ensuring that each turn in the game has a unique resistance level. This prevents the repetition of resistance levels and adds diversity to the gameplay experience.By incorporating counterattacks and unique resistance levels, the game becomes more dynamic and strategic.

### **Game Flow and User Interaction**

The game follows a loop structure to provide a continuous gameplay experience. The main game loop allows the player to choose actions and interact with the game world until specific conditions are met (e.g., the player's health reaches zero or the player chooses to quit).

The game utilizes user input prompts and displayed messages to interact with the player. This is achieved using the <code>input()</code> and <code>print()</code> functions. The <code>type_text()</code> function is introduced to add a typewriter effect to the displayed messages for a better user experience. Not only that but it adds to the retro experience of the game.

### **Game Over**
When the game ends, if the player's health reaches zero, their final statistics are displayed, indicating the end of the game.

### **Logic Overview: leaderboard.py Module**

* Import Required Modules:
    * gspread: A library for accessing Google Sheets.
    * Credentials from google.oauth2.service_account: A module for handling Google API credentials.
    * tabulate module: A library for creating tables from data.

<br>

* Define Scope and Credentials:
    * Define the required scopes for accessing Google Sheets.
    * Load the credentials from the creds.json file.
    * Authorize the credentials with the specified scopes.
    * Authorize the Google Sheets API using the authorized credentials.

<br>

* Open Google Sheet:
    * Open the specified Google Sheet (e.g., "borglite_rank").
    * Access the "leaderboard" worksheet within the Google Sheet.

<br>

* Update Leaderboard:
    * Define the <code>update_leaderboard(player)</code> function.
    * Retrieve the existing leaderboard data from the worksheet.
    * Extract the headers and scores from the retrieved data.
    * Calculate the player's rank based on their score.
    * Update the ranks of other players based on the player's rank.
    * Check if the player's score already exists in the leaderboard.
        * If it exists, update the existing entry with the player's rank, name, level, and score.
        * If it doesn't exist and the player's score is not zero, add the player's data as a new entry.
    * Sort the leaderboard data based on scores in descending order.
    * Update the ranks based on the sorted order.
    * Insert the headers back into the sorted data.
    * Write the updated leaderboard data to the worksheet.

<br>

* Display Leaderboard:
    * Define the <code>display_leaderboard(player)</code>function.
    * Retrieve the leaderboard data from the worksheet.
    * Extract the headers and table data (top 10 scores) from the retrieved data.
    * Display the leaderboard data in a table using the tabulate module.

<br>

Note: The <code>update_leaderboard(player)</code> function is responsible for updating the leaderboard with the player's data, while the <code>display_leaderboard(player)</code> function displays the leaderboard to the player in a table format.

The leaderboard.py module is imported and used in the run.py main file, where the game interface interacts with the leaderboard functionality. The <code>update_leaderboard()</code> and <code>display_leaderboard()</code> functions are called as needed within the game's logic flow to update and display the leaderboard data.

## **Bugs**

**List of known bugs:**




**List of fixed bugs**




## **Technologies**

* [Github](https://github.com/) 
    * Hosted the project's repository. 

* [Gitpod](https://gitpod.io/) 
    * Utilised an IDE with version control capabilities to edit and create files.

* [Github Pages](https://pages.github.com/) 
    * Used to deploy the website.

* [Slack](https://slack.com/intl/en-gb/) 
    * Used a platform to connect with my mentor and fellow course alumni.


## **Testing**

### **Testing User Stories**

| User Story   | Fulfilment | 
| ------------------------------------------------------------------ |:---------------------------------------------| 
As a Star Trek enthusiast, I wish to immerse myself in the captivating Star Trek universe by playing as the Borg, one of the iconic species from the franchise. | The player starts the game as the Borg and becomes part of the collective. 
| As a player, I want to strategise and plan my actions carefully to ensure the success of the Borg collective in conquering new territories and assimilating other civilisations. | The game provides strategic choices and decision-making opportunities for the player to assess their stats, manage resources, and upgrade their character. The player needs to balance their upgrades carefully, considering the bonuses and debuffs associated with each upgrade, to ensure survival and progress onto the leaderboard. 
| As a player, I want to customise and upgrade my Drone as part of the Borg collective. | The game includes options for the player to customise their Borg collective through text-based choices. By collecting power and making strategic decisions, the player can unlock new abilities, technologies, or drones. These choices directly impact their overall strategy, adaptability, and progression within the game. 
| As a player, I want to experience short events after assimilating a system, where I have multiple choices with different outcomes, to further expand upon my journey and the consequences of my actions. | After assimilating a system, the player will encounter short events that present them with three choices. Each choice leads to a different outcome, adding depth to the player's journey and reflecting the consequences of their actions. These events provide narrative variety and contribute to the overall gameplay experience. 
| As a player, I want to engage in the hacking mini-game when encountering defended planets, where I can showcase my skills and intelligence by overcoming security measures to successfully assimilate the planet. | When the player encounters a defended planet, they will be presented with a hacking mini-game. The mini-game will challenge the player to solve puzzles, bypass security systems. Successfully completing the mini-game will allow the player to assimilate the planet and continue their conquest. 
| As a player, I want a comprehensive help section within the game that provides clear instructions and guidance on how to play the overall game, including the mechanics, controls, and strategies involved. | The game includes a dedicated help section accessible from the main menu. The help section provides detailed instructions, explanations of game mechanics, controls, and strategies. It covers various aspects of gameplay, including attacking systems and upgrading the character. However, not all will be revealed as that would remove the challenge.

### **Testing functionality**

| Input     | Result   | Intention   |
| ------------------------------------------------------------------ |:---------------------------------------------| :---------------------------------------------------------|


### **Testing on different devices**



## **Credits**

Developed by **Rhys.Alexander.Few**

### **Code**

**Peer Review**

* **Adam Boley** 
    *  - [Github](https://github.com/AdamBoley).

<br>

* **Antonio Rodriguez** 
  


**Other Resources**


**Bibliography:**









