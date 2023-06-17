

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

# Interface

![Interface](/assets/images/borglite.png)

<br>

During the development process, I faced the challenge of creating a clear and visually appealing interface for a terminal-based game. To overcome this challenge, I decided to utilise ASCII art as a means to convey information to the player effectively.

Given the limitations of a terminal environment, I carefully selected and combined various ASCII designs sourced from reputable ASCII art repositories. My intention was to create a visually captivating experience by customising and incorporating these designs into the game's interface.

By leveraging ASCII art, I aimed to enhance the overall visual appeal of the game and provide players with a unique and engaging visual experience. Despite the challenges involved in working with ASCII art, my determination to fully realise its potential drove me to overcome any obstacles that arose during the implementation process.

To ensure an interesting presentation of information, I focused on incorporating the game's statistics and their dynamic updates. For example, I implemented a feature where the power statistic is processed and displayed as <code>f"Power {power_icon}"</code> using formatted strings. This approach allowed the interface to be updated as the game progressed by feeding the updated data to the player’s display.

By prioritising an intuitive and visually engaging interface and leveraging ASCII art and dynamic statistical display, I aimed to enhance the player's experience and provide them with an immersive text-based gameplay environment.

# Hacking mini-game 

![Hacking](/assets/images/hacking.png)

<br>

In the game I developed, I implemented a hacking mini-game inspired by the iconic "Matrix" movie's code rain effect. When players encounter a planet with defences, there is a chance for the hacking mini-game to be initiated.

The mini-game begins with an animated display of falling characters, resembling the code rain effect from the "Matrix." I used ASCII art and a set of code rain characters like |, /, -, and \ to create this effect.

To proceed with the hacking, players are presented with a six-digit access code they need to crack. I generated a random access code consisting of six digits, with two leading zeros to make it more challenging. Additionally, I added a fake code with one random digit to mislead the player.

Players are prompted to enter the access code by typing it in. The code they enter is then compared with the actual access code using a function called <code>check_code()</code>. This function checks each digit of the input code against the corresponding digit in the access code.

If the input code matches the access code, the hacking attempt is successful. Players gain access to the planet's defences, allowing them to proceed with assimilating the planet.

However, if the input code is incorrect, players have a limited number of attempts to guess the correct code. With each incorrect attempt, the remaining attempts are decremented, and the player is informed about the number of attempts left.

If players fail to guess the code within the given attempts, the hacking is considered unsuccessful. They may also take damage based on the player_damage calculation, which adds an element of risk and consequences to the hacking process.

The hacking mini-game aims to provide an interactive and engaging experience for players while drawing inspiration from the captivating visuals of the "Matrix" movie's code rain effect. It adds a sense of tension and challenge to the gameplay, requiring players to use their problem-solving skills to crack the access code and successfully infiltrate the planet's defences.

# Events 

<br>

The events section I created is triggered when all the planets in a selected system have been assimilated. It adds an exciting element to the game by presenting the player with unique scenarios and choices that affect their gameplay.

I implemented a function called <code>check_assimilation_events()</code> that handles different scenarios or backstories that occur during the assimilation process in the game. This function is called when all the planets in a selected system have been assimilated.

Here's how the events works:

1. The function receives the system, player, and backstories as parameters. The system represents the selected system in the game, the player represents the player's Borg character, and backstories is a list of different backstories or scenarios.

2. Inside the function, a random backstory is selected from the backstories list. This is done by generating a random index between 0 and the length of the backstories list. The selected backstory is then stored in the backstory variable.

3. The relevant information from the selected backstory is extracted, such as the backstory text, the choice prompt text, and the text for each choice. These values are stored in separate variables for later use.

4. The function displays some introductory text.

5. The selected backstory text is printed, providing the player with a narrative description of the current situation or event.

6. The choice prompt text is printed, presenting the player with a set of choices to respond to the event.

7. The player's choice is obtained through user input, and the chosen option is processed accordingly.

8. Based on the chosen option, specific actions are taken. These actions can include modifying the player's stats (such as increasing processing power, decreasing attack power, etc.) and displaying relevant messages.

9. Finally, the function handles any invalid input by providing an error message and prompting the player to make a valid choice.

The purpose of this events section is to introduce dynamic and engaging elements into the game, allowing players to make choices that impact their gameplay experience. The randomly selected backstories and corresponding choices add variety and unpredictability to the assimilation process, making each playthrough unique.

By incorporating different backstories and outcomes, the events section enhances the immersion and storytelling aspects of the game, providing players with a sense of agency and decision-making throughout their Borg assimilation journey.

# Future Works

<br>

Upon receiving feedback from test players, they suggested introducing events earlier in the game to break the repetitive cycle of continuously pressing similar buttons mapped on the keyboard. This valuable feedback highlighted the need for more diverse and engaging gameplay mechanics.

To address this feedback, I plan to implement events at earlier stages of the game within the given time frame. By introducing events sooner, players will experience a greater sense of variety and unpredictability, enhancing their overall gaming experience. These events will introduce new challenges, choices, and consequences, injecting excitement and breaking the monotony of gameplay.

Additionally, I would have liked to make the planets more unique and incorporate a wider variety of defences. While the assimilation process forms the core gameplay mechanic, having distinct planetary attributes and defences would have added depth and strategic elements to the game. Each planet could have possessed its own set of challenges, requiring the player to adapt their assimilation strategies accordingly.

Although time constraints prevented me from implementing these features during the development phase, I acknowledge their potential to enhance the game further. In future iterations or expansions, I would prioritise incorporating diverse planet characteristics and defences to create a richer and more immersive gameplay experience.

Overall, feedback from test players has provided valuable insights and ideas for future improvements. By incorporating early events and introducing varied planet attributes and defences, I aim to address player feedback, enhance gameplay diversity, and create a more engaging and dynamic game for all players to enjoy.

## **Optimization**

Throughout the development process, I have actively experimented with various builds and values to balance and optimise the game. It has been a challenging task to strike the right balance between difficulty and player engagement. While I have made significant progress in certain areas, there are still areas where further refinement is needed.

One area that I have identified for improvement is the game's difficulty progression. Currently, the game starts off relatively easy, making it accessible for players to grasp the mechanics and get accustomed to the gameplay. However, as the game progresses past level 17, the difficulty ramps up quite aggressively. This sudden increase in challenge may potentially frustrate players and hinder their overall enjoyment of the game.

Moving forward, I recognize the need to fine-tune the difficulty curve to ensure a more balanced and satisfying gameplay experience. This will involve carefully adjusting the parameters that govern the rate at which enemies spawn, their strength, and the resources available to the player. By striking a better balance between early and late-game challenges, I aim to create a more enjoyable and engaging experience for players of all skill levels.

Furthermore, in terms of optimization, I have made efforts to streamline the code and enhance performance. However, as with any complex project, there are always opportunities for further optimization. I will continue to identify and implement optimization techniques to improve the game's overall performance, ensuring smooth gameplay even on lower-end systems.

While balancing and optimization are ongoing processes, I acknowledge that further work is needed to achieve the desired level of refinement. As part of future work, I will continue to gather feedback from players and conduct thorough playtesting to address these areas of improvement. By refining the difficulty progression and optimising the game's performance, I aim to create a more polished and enjoyable experience for all players.

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

The game follows a loop structure to provide a continuous gameplay experience. The main game loop allows the player to choose actions and interact with the game world until specific conditions are met (e.g. if the player's health reaches zero or the player chooses to quit).

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

![leaderboard](/assets/images/leaderboard.png)

<br>

Note: The <code>update_leaderboard(player)</code> function is responsible for updating the leaderboard with the player's data, while the <code>display_leaderboard(player)</code> function displays the leaderboard to the player in a table format.

The leaderboard.py module is imported and used in the run.py main file, where the game interface interacts with the leaderboard functionality. The <code>update_leaderboard()</code> and <code>display_leaderboard()</code> functions are called as needed within the game's logic flow to update and display the leaderboard data.

## **Bugs**

**List of known bugs & errors:**

* Favicon Issue: The favicon could not be displayed on the Heroku app. Unfortunately, this issue could not be fixed as it might be a limitation or configuration issue specific to the Heroku platform. Alternative solutions or workarounds can be explored, such as using a different hosting platform or adjusting the favicon format.

### Module - run.py PEP8

In my project, I made a conscious decision not to conform to the PEP 8 guidelines regarding line length. The reason behind this choice was that I had an array of indentations for my strings, which allowed me to create a neater and less crowded display in the terminal for my text-based game.

Although I became aware of PEP 8 guidelines later on in the project, I decided not to adhere to the recommended 79-line length in order to maintain the visual aesthetics of the game. By adjusting the line length and indentation, I was able to achieve a more visually appealing presentation without compromising the functionality of the game.

I understand that adhering to coding conventions like PEP 8 is generally recommended for code consistency and maintainability. However, in this particular case, I prioritised the visual aspect of the game and made a deliberate choice to deviate from the guidelines.

It's worth noting that while style conventions provide guidance, they are not strict rules, and there can be situations where it's acceptable to deviate from them. As a developer, it's important to be aware of these conventions and understand when it's appropriate to follow or deviate from them, depending on the specific context and requirements of the project.

In the future, I will keep in mind the importance of adhering to coding conventions like PEP 8, as it can improve code readability and maintainability, especially when collaborating with others or returning to the code at a later stage.

* 7: E302 expected 2 blank lines, found 1
* 19: W293 blank line contains whitespace
* 20: E501 line too long (114 > 79 characters)
* 22: W291 trailing whitespace
* 23: E501 line too long (127 > 79 characters)
* 24: W291 trailing whitespace
* 25: E501 line too long (138 > 79 characters)
* 27: W293 blank line contains whitespace
* 35: W293 blank line contains whitespace
* 41: E501 line too long (89 > 79 characters)
* 42: W293 blank line contains whitespace
* 45: W293 blank line contains whitespace
* 52: W293 blank line contains whitespace
* 54: E231 missing whitespace after ','
* 57: W293 blank line contains whitespace
* 63: E501 line too long (83 > 79 characters)
* 71: W291 trailing whitespace
* 75: W293 blank line contains whitespace
* 76: E501 line too long (96 > 79 characters)
* 78: E501 line too long (111 > 79 characters)
* 82: E501 line too long (88 > 79 characters)
* 91: W291 trailing whitespace
* 93: W293 blank line contains whitespace
* 102: W291 trailing whitespace
* 103: E501 line too long (95 > 79 characters)
* 116: W293 blank line contains whitespace
* 119: W293 blank line contains whitespace
* 122: W293 blank line contains whitespace
* 125: W293 blank line contains whitespace
* 126: W291 trailing whitespace
* 128: E501 line too long (89 > 79 characters)
* 129: E501 line too long (154 > 79 characters)
* 129: W291 trailing whitespace
* 130: W291 trailing whitespace
* 131: E501 line too long (122 > 79 characters)
* 132: E501 line too long (208 > 79 characters)
* 132: W291 trailing whitespace
* 133: W291 trailing whitespace
* 134: E501 line too long (89 > 79 characters)
* 134: W291 trailing whitespace
* 135: E501 line too long (100 > 79 characters)
* 135: W291 trailing whitespace
* 136: E501 line too long (100 > 79 characters)
* 137: W605 invalid escape sequence '\`'
* 137: E501 line too long (89 > 79 characters)
* 138: E501 line too long (89 > 79 characters)
* 139: E501 line too long (89 > 79 characters)
* 139: W291 trailing whitespace
* 140: E501 line too long (89 > 79 characters)
* 140: W291 trailing whitespace
* 141: E501 line too long (100 > 79 characters)
* 142: E501 line too long (100 > 79 characters)
* 143: E501 line too long (100 > 79 characters)
* 144: E501 line too long (89 > 79 characters)
* 145: E501 line too long (100 > 79 characters)
* 146: W291 trailing whitespace
* 147: E501 line too long (111 > 79 characters)
* 148: E501 line too long (111 > 79 characters)
* 149: E501 line too long (133 > 79 characters)
* 150: E501 line too long (100 > 79 characters)
* 151: E501 line too long (89 > 79 characters)
* 153: W293 blank line contains whitespace
* 155: W293 blank line contains whitespace
* 156: W291 trailing whitespace
* 169: W293 blank line contains whitespace
* 171: E302 expected 2 blank lines, found 1
* 181: E501 line too long (144 > 79 characters)
* 181: W291 trailing whitespace
* 182: E501 line too long (124 > 79 characters)
* 186: E501 line too long (102 > 79 characters)
* 192: E501 line too long (102 > 79 characters)
* 198: E501 line too long (85 > 79 characters)
* 198: E203 whitespace before ','
* 203: W293 blank line contains whitespace
* 208: W293 blank line contains whitespace
* 212: E302 expected 2 blank lines, found 1
* 220: E501 line too long (90 > 79 characters)
* 222: W293 blank line contains whitespace
* 223: E501 line too long (132 > 79 characters)
* 237: E501 line too long (105 > 79 characters)
* 238: E501 line too long (84 > 79 characters)
* 253: E501 line too long (92 > 79 characters)
* 260: E501 line too long (101 > 79 characters)
* 262: W293 blank line contains whitespace
* 269: E501 line too long (87 > 79 characters)
* 301: E501 line too long (124 > 79 characters)
* 302: E501 line too long (100 > 79 characters)
* 304: E501 line too long (90 > 79 characters)
* 309: E501 line too long (96 > 79 characters)
* 329: E501 line too long (94 > 79 characters)
* 330: W293 blank line contains whitespace
* 336: W291 trailing whitespace
* 337: W293 blank line contains whitespace
* 344: E201 whitespace after <code>'('</Code>
* 344: E501 line too long (93 > 79 characters)
* 354: W293 blank line contains whitespace
* 359: E501 line too long (101 > 79 characters)
* 365: E501 line too long (109 > 79 characters)
* 366: E501 line too long (144 > 79 characters)
* 368: W293 blank line contains whitespace
* 373: E302 expected 2 blank lines, found 1
* 381: E501 line too long (105 > 79 characters)
* 389: E501 line too long (104 > 79 characters)
* 390: E501 line too long (82 > 79 characters)
* 398: W293 blank line contains whitespace
* 403: E501 line too long (116 > 79 characters)
* 406: E501 line too long (88 > 79 characters)
* 415: W293 blank line contains whitespace
* 422: E501 line too long (99 > 79 characters)
* 425: W293 blank line contains whitespace
* 426: E501 line too long (83 > 79 characters)
* 436: E501 line too long (82 > 79 characters)
* 439: E501 line too long (81 > 79 characters)
* 443: W291 trailing whitespace
* 460: E501 line too long (110 > 79 characters)
* 471: E501 line too long (96 > 79 characters)
* 472: E501 line too long (121 > 79 characters)
* 474: E501 line too long (121 > 79 characters)
* 475: E501 line too long (102 > 79 characters)
* 476: W293 blank line contains whitespace
* 483: E501 line too long (92 > 79 characters)
* 488: E501 line too long (100 > 79 characters)
* 489: W291 trailing whitespace
* 490: E501 line too long (101 > 79 characters)
* 493: E501 line too long (113 > 79 characters)
* 494: E501 line too long (116 > 79 characters)
* 497: E501 line too long (84 > 79 characters)
* 504: W293 blank line contains whitespace
* 507: W291 trailing whitespace
* 511: E501 line too long (393 > 79 characters)
* 512: E501 line too long (271 > 79 characters)
* 513: E501 line too long (97 > 79 characters)
* 514: E501 line too long (111 > 79 characters)
* 515: E501 line too long (86 > 79 characters)
* 518: W293 blank line contains whitespace
* 519: E501 line too long (371 > 79 characters)
* 520: E501 line too long (342 > 79 characters)
* 521: E501 line too long (151 > 79 characters)
* 522: E501 line too long (182 > 79 characters)
* 523: E501 line too long (191 > 79 characters)
* 524: W291 trailing whitespace
* 526: E501 line too long (370 > 79 characters)
* 527: E501 line too long (328 > 79 characters)
* 528: E501 line too long (200 > 79 characters)
* 529: E501 line too long (182 > 79 characters)
* 530: E501 line too long (232 > 79 characters)
* 531: W291 trailing whitespace
* 533: W293 blank line contains whitespace
* 536: W293 blank line contains whitespace
* 538: E225 missing whitespace around operator
* 538: E501 line too long (114 > 79 characters)
* 539: E501 line too long (96 > 79 characters)
* 546: W293 blank line contains whitespace
* 547: E501 line too long (105 > 79 characters)
* 551: W293 blank line contains whitespace
* 553: E501 line too long (95 > 79 characters)
* 554: W293 blank line contains whitespace
* 559: E712 comparison to True should be 'if cond is True
* 561: E712 comparison to False should be 'if cond is False
* 566: W293 blank line contains whitespace
* 569: E712 comparison to True should be 'if cond is True
* 571: E712 comparison to False should be 'if cond is False
* 576: W293 blank line contains whitespace
* 579: E712 comparison to True should be 'if cond is True
* 581: E712 comparison to False should be 'if cond is False
* 586: W293 blank line contains whitespace
* 591: E712 comparison to True should be 'if cond is True
* 593: E501 line too long (83 > 79 characters)
* 595: E712 comparison to False should be 'if cond is False
* 598: E501 line too long (83 > 79 characters)
* 601: W293 blank line contains whitespace
* 604: E712 comparison to True should be 'if cond is True
* 606: E501 line too long (82 > 79 characters)
* 608: E712 comparison to False should be 'if cond is False
* 611: E501 line too long (83 > 79 characters)
* 614: W293 blank line contains whitespace
* 618: E712 comparison to True should be 'if cond is True
* 620: E501 line too long (83 > 79 characters)
* 622: E712 comparison to False should be 'if cond is False
* 625: E501 line too long (112 > 79 characters)
* 629: E501 line too long (89 > 79 characters)
* 632: W293 blank line contains whitespace
* 637: E501 line too long (99 > 79 characters)
* 640: E501 line too long (99 > 79 characters)
* 641: W293 blank line contains whitespace
* 644: E501 line too long (99 > 79 characters)
* 645: W293 blank line contains whitespace
* 646: W293 blank line contains whitespace
* 647: E303 too many blank lines (2)
* 651: W291 trailing whitespace
* 652: E302 expected 2 blank lines, found 1
* 653: E501 line too long (81 > 79 characters)
* 656: E501 line too long (102 > 79 characters)
* 658: E501 line too long (120 > 79 characters)
* 659: E501 line too long (117 > 79 characters)
* 667: E501 line too long (98 > 79 characters)
* 672: E501 line too long (98 > 79 characters)
* 677: E501 line too long (98 > 79 characters)
* 682: E501 line too long (98 > 79 characters)
* 684: W293 blank line contains whitespace
* 686: W293 blank line contains whitespace
* 687: E225 missing whitespace around operator
* 689: E501 line too long (110 > 79 characters)
* 690: E501 line too long (87 > 79 characters)
* 694: E501 line too long (134 > 79 characters)
* 696: E501 line too long (95 > 79 characters)
* 696: W291 trailing whitespace
* 697: E501 line too long (84 > 79 characters)
* 697: W291 trailing whitespace
* 698: E501 line too long (89 > 79 characters)
* 699: E501 line too long (87 > 79 characters)
* 699: W291 trailing whitespace
* 700: E501 line too long (112 > 79 characters)
* 701: E501 line too long (105 > 79 characters)
* 708: W293 blank line contains whitespace
* 709: W291 trailing whitespace
* 710: E302 expected 2 blank lines, found 1
* 714: W293 blank line contains whitespace
* 730: E501 line too long (83 > 79 characters)
* 731: E501 line too long (91 > 79 characters)
* 732: E501 line too long (103 > 79 characters)
* 738: E501 line too long (99 > 79 characters)
* 739: E501 line too long (88 > 79 characters)
* 740: E501 line too long (96 > 79 characters)
* 741: E501 line too long (93 > 79 characters)
* 742: E501 line too long (104 > 79 characters)
* 748: E501 line too long (103 > 79 characters)
* 749: E501 line too long (97 > 79 characters)
* 750: E501 line too long (84 > 79 characters)
* 751: E501 line too long (83 > 79 characters)
* 752: E501 line too long (113 > 79 characters)
* 765: E302 expected 2 blank lines, found 1
* 771: E501 line too long (110 > 79 characters)
* 772: E501 line too long (111 > 79 characters)
* 773: E501 line too long (112 > 79 characters)
* 774: E501 line too long (112 > 79 characters)
* 775: E501 line too long (111 > 79 characters)
* 782: E501 line too long (120 > 79 characters)
* 783: E501 line too long (110 > 79 characters)
* 784: E501 line too long (115 > 79 characters)
* 785: E501 line too long (111 > 79 characters)
* 786: E501 line too long (109 > 79 characters)
* 793: E501 line too long (112 > 79 characters)
* 794: E501 line too long (109 > 79 characters)
* 795: E501 line too long (117 > 79 characters)
* 796: E501 line too long (113 > 79 characters)
* 797: E501 line too long (126 > 79 characters)
* 804: E501 line too long (110 > 79 characters)
* 805: E501 line too long (124 > 79 characters)
* 806: E501 line too long (120 > 79 characters)
* 807: E501 line too long (110 > 79 characters)
* 808: E501 line too long (110 > 79 characters)
* 815: E501 line too long (115 > 79 characters)
* 816: E501 line too long (114 > 79 characters)
* 817: E501 line too long (112 > 79 characters)
* 818: E501 line too long (122 > 79 characters)
* 819: E501 line too long (112 > 79 characters)
* 824: W293 blank line contains whitespace
* 826: E302 expected 2 blank lines, found 1
* 831: E225 missing whitespace around operator
* 832: W293 blank line contains whitespace
* 833: E501 line too long (101 > 79 characters)
* 840: E501 line too long (160 > 79 characters)
* 843: W293 blank line contains whitespace
* 852: E501 line too long (95 > 79 characters)
* 856: E251 unexpected spaces around keyword / parameter equals
* 856: E251 unexpected spaces around keyword / parameter equals
* 857: E501 line too long (105 > 79 characters)
* 859: W291 trailing whitespace
* 862: E501 line too long (133 > 79 characters)
* 864: E501 line too long (93 > 79 characters)
* 868: W293 blank line contains whitespace
* 872: E501 line too long (89 > 79 characters)
* 875: E501 line too long (83 > 79 characters)
* 878: E501 line too long (86 > 79 characters)
* 885: E501 line too long (83 > 79 characters)
* 887: E501 line too long (81 > 79 characters)
* 890: E501 line too long (87 > 79 characters)
* 893: E302 expected 2 blank lines, found 1
* 895: E501 line too long (90 > 79 characters)
* 900: W293 blank line contains whitespace
* 902: E302 expected 2 blank lines, found 1
* 908: E302 expected 2 blank lines, found 1
* 917: E305 expected 2 blank lines after class or function definition, found 1
* 918: W293 blank line contains whitespace
* 919: W293 blank line contains whitespace
* 920: E303 too many blank lines (2)
* 923: W293 blank line contains whitespace
* 939: W293 blank line contains whitespace
* 941: E501 line too long (80 > 79 characters)
* 952: E501 line too long (101 > 79 characters)
* 954: W293 blank line contains whitespace
* 971: W293 blank line contains whitespace
* 979: W293 blank line contains whitespace
* 980: W291 trailing whitespace
* 984: W293 blank line contains whitespace
* 985: E501 line too long (120 > 79 characters)
* 991: E501 line too long (102 > 79 characters)
* 994: E501 line too long (98 > 79 characters)
* 995: E501 line too long (133 > 79 characters)
* 996: E501 line too long (81 > 79 characters)
* 998: W293 blank line contains whitespace
* 999: E501 line too long (116 > 79 characters)
* 1000: E501 line too long (114 > 79 characters)
* 1001: W291 trailing whitespace
* 1004: E501 line too long (86 > 79 characters)
* 1006: E501 line too long (102 > 79 characters)
* 1007: W293 blank line contains whitespace
* 1011: E501 line too long (84 > 79 characters)
* 1013: E501 line too long (100 > 79 characters)
* 1013: W291 trailing whitespace
* 1014: W293 blank line contains whitespace
* 1018: W293 blank line contains whitespace
* 1019: E501 line too long (90 > 79 characters)
* 1021: E501 line too long (109 > 79 characters)
* 1023: W293 blank line contains whitespace
* 1026: E501 line too long (84 > 79 characters)
* 1026: W291 trailing whitespace
* 1027: E501 line too long (87 > 79 characters)
* 1030: W291 trailing whitespace
* 1034: W293 blank line contains whitespace
* 1036: E501 line too long (85 > 79 characters)
* 1039: E501 line too long (112 > 79 characters)
* 1041: E501 line too long (102 > 79 characters)
* 1043: E501 line too long (117 > 79 characters)
* 1049: W293 blank line contains whitespace
* 1051: E501 line too long (109 > 79 characters)
* 1051: W291 trailing whitespace
* 1063: W291 trailing whitespace
* 1067: E501 line too long (87 > 79 characters)
* 1083: E501 line too long (103 > 79 characters)
* 1087: W293 blank line contains whitespace
* 1092: W293 blank line contains whitespace

### Module - leaderboard.py PEP8

* 11: W291 trailing whitespace
* 16: E501 line too long (93 > 79 characters)
* 18: E302 expected 2 blank lines, found 1
* 26: E501 line too long (118 > 79 characters)
* 27: E501 line too long (117 > 79 characters)
* 36: E501 line too long (84 > 79 characters)
* 39: E501 line too long (91 > 79 characters)
* 45: E501 line too long (128 > 79 characters)
* 49: E501 line too long (103 > 79 characters)
* 60: E501 line too long (158 > 79 characters)
* 72: E302 expected 2 blank lines, found 1
* 74: E501 line too long (84 > 79 characters)
* 79: E501 line too long (149 > 79 characters)
* 83: W293 blank line contains whitespace

### **Explaining development choices:**

After seeking advice from my friend, he informed me that in most cases, it is considered best practice to include an else block to handle scenarios that don't meet the conditions of the if/elif statements. However, he also mentioned that if you are specifically anticipating certain values and want to handle them individually, using only if/elif statements without an else block can be acceptable. He provided an example from his job, where he checks URLs in this manner.

Regarding the use of "pass," (starting from line 559) he advised that it is more commonly employed in function and class definitions when you need a placeholder that doesn't perform any actions. For instance, he personally uses it while constructing form classes in Django.

He recommended documenting this specific approach, explaining the rationale behind omitting the else block or using "pass." 

### **Rationale:**

The syntax in the code (line 559) follows a specific structure to handle different scenarios based on the values of choice and <code>backstory_index</code>. Each section of the code corresponds to a specific combination of these values and performs certain actions accordingly.

The pass statement is used as a placeholder in the else blocks where no additional actions are required. It essentially acts as a no-operation statement, indicating that the code should continue execution without performing any specific operations in those cases.

The use of pass is justified when the intention is to explicitly omit any additional code execution for those specific scenarios. By using pass, it clearly communicates that no further actions are necessary and prevents any unintended behavior or potential errors that may arise from leaving the else blocks empty.

In summary, the pass statements are intentionally used to maintain the structure and flow of the code while explicitly indicating that no further operations are needed in those specific cases.

**List of fixed bugs**

* ZeroDivisionError: This error occurred due to a division by zero in the calculation of success_chance = attack_power / system.enemy_resistance. To fix this, a check can be added to ensure that system.enemy_resistance is not zero before performing the division. For example: <br>
<code>if system.enemy_resistance != 0: <br>
        success_chance = attack_power / system.enemy_resistance <br>
    else:</code>

* Upgrades Applied Without Power Requirement: The bug allowed upgrades to be applied without considering the power requirement. To fix this, an if statement can be added to check if the player has enough power before applying the upgrade. If there is not enough power, the upgrade should not be applied. 

* Terminal Display Issues: Some strings were too long for the terminal and caused formatting issues. To fix this, you can break the long strings into multiple lines or truncate them to fit within the available space. 

* Planet Invalid Key Resetting Loop: The bug caused the loop to reset when an invalid key was entered for planet selection. To fix this, a try-except block can be added around the input statement to catch any invalid input and handle it accordingly. 

* Attack Feature Randomness: The bug caused the attack feature to be predictable. To make it more random, you can store a list of numbers that have already been used for attacks and prevent their reuse. You can use the random.sample function to select a random number from the available range and remove it from the list of available numbers.


## **Technologies**

* [Github](https://github.com/) 
    * Hosted the project's repository. 

* [Gitpod](https://gitpod.io/) 
    * Utilised an IDE with version control capabilities to edit and create files.

* [Github Pages](https://pages.github.com/) 
    * Used to deploy the website.

* [Slack](https://slack.com/intl/en-gb/) 
    * Used a platform to connect with my mentor and fellow course alumni.

* [Lucidchart](https://www.lucidchart.com/pages/)
    * Used to create a flow chart.

* [Python-Tutor](https://www.python.org/)
    * Used to test code and research ideas.

* [CI Python Linter](https://pep8ci.herokuapp.com/)
    * Used to test pep8 compatibility.

* [Heroku](https://id.heroku.com/login)
    * Used to deploy my project.

<br>

## **Testing**

<br>

### **Testing User Stories**

| User Story   | Fulfilment | 
| ------------------------------------------------------------------ |:---------------------------------------------| 
As a Star Trek enthusiast, I wish to immerse myself in the captivating Star Trek universe by playing as the Borg, one of the iconic species from the franchise. | The player starts the game as the Borg and becomes part of the collective. 
| As a player, I want to strategise and plan my actions carefully to ensure the success of the Borg collective in conquering new territories and assimilating other civilisations. | The game provides strategic choices and decision-making opportunities for the player to assess their stats, manage resources, and upgrade their character. The player needs to balance their upgrades carefully, considering the bonuses and debuffs associated with each upgrade, to ensure survival and progress onto the leaderboard. 
| As a player, I want to customise and upgrade my Drone as part of the Borg collective. | The game includes options for the player to customise their Borg collective through text-based choices. By collecting power and making strategic decisions, the player can unlock new abilities, technologies, or drones. These choices directly impact their overall strategy, adaptability, and progression within the game. 
| As a player, I want to experience short events after assimilating a system, where I have multiple choices with different outcomes, to further expand upon my journey and the consequences of my actions. | After assimilating a system, the player will encounter short events that present them with three choices. Each choice leads to a different outcome, adding depth to the player's journey and reflecting the consequences of their actions. These events provide narrative variety and contribute to the overall gameplay experience. 
| As a player, I want to engage in the hacking mini-game when encountering defended planets, where I can showcase my skills and intelligence by overcoming security measures to successfully assimilate the planet. | When the player encounters a defended planet, they will be presented with a hacking mini-game. The mini-game will challenge the player to solve puzzles, bypass security systems. Successfully completing the mini-game will allow the player to assimilate the planet and continue their conquest. 
| As a player, I want a comprehensive help section within the game that provides clear instructions and guidance on how to play the overall game, including the mechanics, controls, and strategies involved. | The game includes a dedicated help section accessible from the main menu. The help section provides detailed instructions, explanations of game mechanics, controls, and strategies. It covers various aspects of gameplay, including attacking systems and upgrading the character. However, not all will be revealed as that would remove the challenge.

<br>

### **Testing functionality**

Decision               | Input                         | Expected Outcome                               | Actual Outcome                                 |
-----------------------| ----------------------------- | ---------------------------------------------- | -----------------------------------------------|
Enter your name        | Player enter's name           | Game starts with the entered name              | Game starts with the entered name              |
Attack a system        | Proceed -key press "a" or "A" | Initiates an attack on the selected system     | Initiates an attack on the selected system     |
Upgrade player         | Proceed -key press "u" or "U" | Opens the upgrade menu for the player          | Opens the upgrade menu for the player          |
Help                   | Proceed -key press "h" or "H" | Displays the available help options            | Displays the available help options            |
Leaderboard            | Proceed -key press "l" or "L" | Shows the leaderboard with rankings            | Shows the leaderboard with rankings            |
Select a system        | Index - 1-5                   | Initiates interaction with the selected system | Initiates interaction with the selected system |
Assimilate a planet    | Index - 1-5                   | Attempts to assimilate the selected planet     | Attempts to assimilate the selected planet     |
Events choice          | Index - [1], [2] and [3]      | Prompts the player to enter their choice       | Prompts the player to enter their choice       |
Error message          | Prompt for correct input      | Prompts the player to enter a valid input      | Prompts the player to enter a valid input      |
Hacking code           | Enter 6 digits - 0 - 9        | Prompts the player to enter a 6-digit code     | Prompts the player to enter a 6-digit code     |



## **Credits**

Developed by **Rhys.Alexander.Few**

### **Code**

**Peer Review**

* **Adam Boley** 
    * I express my heartfelt appreciation to my friend for attentively listening to my inquiries and generously offering me valuable information and constructive feedback. Their support has been immensely beneficial to me - [Github](https://github.com/AdamBoley).

<br>

* **Antonio Rodriguez** 
    * I extend my utmost gratitude to my mentor Antonio for consistently providing me with invaluable insights. He has always been a boundless well of knowledge and a constant source of inspiration.
  

**Bibliography:**

* Tutorial on YouTube - "Learn Python": [Youtube](https://www.youtube.com/watch?v=rfscVS0vtbw)

* FontSpace - Arcade Fonts: [Link](https://www.fontspace.com/category/arcade)
    * FontSpace offers a collection of arcade-style fonts. These fonts were used to create visually appealing headings and text styles within the game. The arcade fonts added a retro and nostalgic touch to the game's overall design.

* ASCII Art from ASCII.co.uk - Star Trek: [Link](https://ascii.co.uk/art/startrek)
    * ASCII.co.uk provides a selection of ASCII art, including a dedicated section for Star Trek-themed art. Some ASCII art from this website was incorporated into the game to enhance the visual experience and create a connection with the Star Trek universe.

* Code Institute - Love Sandwiches Tutorial: API Boilerplate Code and Tutorial
    * The Love Sandwiches tutorial from Code Institute offered guidance on working with APIs and provided boilerplate code for integrating a leaderboard feature into the game. This tutorial was instrumental in implementing the leaderboard functionality, allowing players to compete and track their scores.

* Stack Overflow - A community-driven question-and-answer website for programming: Accessible at [https://stackoverflow.com](https://stackoverflow.com). Stack Overflow is a valuable resource for troubleshooting coding issues, seeking solutions, and gaining insights from the programming community.
    * Boiler plate code for invoking the python script [Link](https://stackoverflow.com/questions/419163/what-does-if-name-main-do)

* GeeksforGeeks - Online platform with programming tutorials and articles: Visit [https://www.geeksforgeeks.org](https://www.geeksforgeeks.org) for a wide range of tutorials covering algorithms, data structures, and various coding concepts. It also provides examples and explanations related to game development.

* Real Python - Online platform offering in-depth Python tutorials and articles: Find practical resources at [https://realpython.com](https://realpython.com), including comprehensive Python tutorials, step-by-step guides, and examples relevant to game development.
    * How to convert Python objects into strings [Link](https://realpython.com/lessons/how-and-when-use-str/).

* Python.org - The official website for the Python programming language: Visit [https://www.python.org](https://www.python.org) for official news, updates, and resources related to Python, including the Python Package Index (PyPI) for accessing third-party libraries.

* Youtube - [Youtube](https://www.youtube.com/watch?v=3CoMsIiHabc) not strictly followed but was useful for my hacking mini game.

* Python Tutor - A web-based tool for visualizing Python code execution: Explore [https://pythontutor.com](https://pythontutor.com) to visually debug and understand how Python code works. It provides a step-by-step visualization of code execution.










