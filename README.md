

# BorgLite 

# Code Institute Portfolio Project 3: Python Essentials - Back end game deployed via Heroku.
### To view the project please [click here](https://borglite.herokuapp.com/).
<br>

![Index page screenshot]()


## **Background**





## **Scope**





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

2. Download the Borglite game source code from the GitHub repository. You can do this by clicking on the "Download ZIP" button on the repository page and extracting the contents to a folder of your choice. Alternatively, you can use the following command to clone the repository:  <code> git clone https://github.com/your-username/your-repo.git </code>

4. Open a terminal or command prompt and navigate to the folder where you placed the game's source code.

5. To install the required dependencies, run the following command:  <code> pip install -r requirements.txt </code>

6. This will install all the necessary packages, including the additional libraries:  <code>google-auth==2.19.1, google-auth-oauthlib==1.0.0, gspread==5.9.0, tabulate==0.9.0</code>

<br>

### **Additionally, if you are using the Google Sheets API for the game, you need to provide your API credentials. Follow these steps to add your credentials as environment variables:**

<br>

a. Obtain the JSON file containing your API credentials from the Google Cloud Console.

b. Rename the JSON file to "credentials.json" and place it in the root directory of the Borglite game.

c. Copy the name of JSON file to .gitignore because it contains sensitive information about your google account.

d. Add boilerplate code for your API: <br>  <code> import gspread <br>
from google.oauth2.service_account import Credentials <br>


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets", <br>
    "https://www.googleapis.com/auth/drive.file", <br>
    "https://www.googleapis.com/auth/drive" <br>
    ]

 </code>

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









