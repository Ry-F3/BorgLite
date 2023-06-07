

# BorgLite 

# Code Institute Portfolio Project 3: Python Essentials - Back End CLI Game Deployed Via Heroku.
### To view the project please [click here](https://borglite.herokuapp.com/).
<br>

![Index page screenshot](/assets/images/amiresponsive.png)


### **Borglite background:** 
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




## **Audience**





## **User Stories**


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

 * You are now ready to run the game locally. Execute the following command:  <code> python3 game.py </code>

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









