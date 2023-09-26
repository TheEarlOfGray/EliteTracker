# EliteTracker
## Author - Earl Gray

## Objective

* To create a CRUD application with utilisation of supporting tools,
methodologies and technologies that encapsulate all core modules
covered during training.

Broken down this project has the following requirements:

-Create an app in Python that utilises CRUD functionality\
-Deploy front end using Flask\
-Track project progress using Scrum style board\
-Include use of external SQL database\
-Testing\
-Documentation\
-Repository of code base


## Project Initiation

I propose to create an app that allows the user to track Various player characters and the ships that they pilot in the popular video game Elite: Dangerous. Users will thus be able to input details for each player character they choose to track including their combat rank, create new ship models to track ship types, and then also add the individual ships that player characters regularly pilot, including an estimated armament rating and tags that briefly denote the appearance for quick reference. The User should be able to view a list of the individual ships owned by any one player character. \
\
The implicit CRUD functionality of this app will include:

* CREATE\
  -Add Pilots\
  -Add Ships\
  -Add Pilots Ships
  
* READ\
  -View Pilots\
  -View Pilots Ships arrayed by individual Pilot
  
* UPDATE\
  -Edit the details of all items in the database
  
* DELETE\
  -Remove any individual item from the database
  

## Planning, Design and Project Tracking

### ERD

I began with a basic entity relationship diagram designed around the relationships I expected these entities to have, with the assumption that these may change slightly in the development process. My initial design looked thus:
![Elite Dangerous Adversary Tracker(1)](https://user-images.githubusercontent.com/80707106/126901614-b1de3fdf-c96d-4e1a-9722-137cb8f24eac.png)

The following design is the updated model actually used in the project.\ 
The first change occurred when I realised that a composite key was an unneccessary complication. Instead I simply related the two main tables to the association table using the primary keys. Other changes were minimal changes to the desired attributes. Most notably to remove the fatuous attribute 'base engine rating' from the ship type table.
![Elite The Dangerous](https://user-images.githubusercontent.com/80707106/126901573-4fcfc3ba-4c1d-4d21-92a7-0bb147a128ef.png)

The main point of the relational data between these entities is the use of specific, already registered Pilots and Ship types when inputting data for individually named ships.

### Jira Board

I decided on using Jira as the provider for my project board as I wished a little experience in using software widely used in industry. My use of the software was basic but I was easily able to visualise the work I was doing and hed yet to complete so it certainly fulfilled it's function.
![JiraBoard](https://user-images.githubusercontent.com/80707106/126902122-492b2dc8-83ab-4a2c-8473-b09f5dfa8558.png)

### Risk Assessment

My risk assessment, though basic, attempted to percieve possible threats to the project. The entries with proposed Control Measures as opposed to implemented were considered and noted later on towards the end of the project.
![RiskAssessment](https://user-images.githubusercontent.com/80707106/126902336-9c4b2105-76c6-4373-89d3-64cd61696b2e.png)


## Front End

The entry point for the app is the home page, navigated to with the '/' url suffix. The landing/home page simply directs the user to navigate the site using the menu options, and occasionally prints a message to confirm addition of Pilots or Ships. The style elements of the navigation bar are courtesy of Bootstrap 3.
![HomePageLanding](https://user-images.githubusercontent.com/80707106/126904455-50526b24-dd86-452f-9521-76ee0bd9c7ed.png)

And when a Pilot is added for example:
![HomePageMessage](https://user-images.githubusercontent.com/80707106/126904529-7b645218-021f-498b-be66-a7272a0baa18.png)

From this (and any) page the user can add Pilots, with the form creating an entry for the Pilot that persists in the database on reciept of a valid form submission.
![AddPilot](https://user-images.githubusercontent.com/80707106/126904776-1ca2e811-b5d4-4290-9f79-74ded58f5464.png)

The functionality for adding a Ship model is exactly the same but there is something of a difference when adding a specific ship, as this table element can only be created with links to both an existing Pilot and an existing Ship type.
![AddPilotShip](https://user-images.githubusercontent.com/80707106/126904947-a1f4e4fe-7dbc-4a22-a88c-4b3ef5612a04.png)


## Testing and Automation

The app consists of several unit tests designed to test each aspect of the apps functionality, namely the routing and use of CRUD functionality.
The test coverage of these functions is 100% as seen in the image below,
![TestsCoverage](https://user-images.githubusercontent.com/80707106/126905419-8ea9285a-366a-430c-91bb-bbb32cc4432f.png)

and should any of these tests fail this can be tracked in the terminal.
![TestsFail](https://user-images.githubusercontent.com/80707106/126905430-949940d2-8495-416c-bd65-953fae184251.png)

As it currently stands the app passes all of the tests to be run. These tests can be found in the test folder in the main directory.
![TestsPassed](https://user-images.githubusercontent.com/80707106/126905492-76bc62c1-dfac-4387-bcc6-2c0466377517.png)

To achieve a somewhat automated process Jenkins has been installed and can be used to run the tests on the latest build pushed to GitHub. First Jenkins clones the repo and starts a virtual environment,
![JenkinsSuccess](https://user-images.githubusercontent.com/80707106/126905558-4656da1b-2fec-499a-a1b5-0fe030230183.png)

and then proceeds to install all of the required packages,
![InstallingRequirements](https://user-images.githubusercontent.com/80707106/126905570-753d1756-7314-4df7-8cf1-bc336feb0624.png)

followed by running the tests, ensuring they all pass and then removing the installation.
![JenkinsRunsTests](https://user-images.githubusercontent.com/80707106/126905596-7ccc131c-9cf1-429e-8c02-bc59dc80ccb0.png)

Jenkins is currently set to run this automation from any branch of the GitHub repo on the click of a button, however for future development Jenkins would most likely be set to run tests automatically on pushing to the repos 'Main' branch.

## The Future

The app is suitable for continued development, most notably allowing for the editing of the individual player characters ships, which was outside of the scope of this project. Nonetheless, work has been done in the routes to ensure this further development is easily implemented.\
![RoutingFuture](https://user-images.githubusercontent.com/80707106/126906242-987e156a-f7e9-45d1-8443-51c8d6b56471.png)

As it stands the user can delete existing ships as well as adding new ones, whilst they are able to update only the player character and ship types as these are the more likely to change through time.


## Acknowledgements

Thanks and credit go to w3schools for their basic navbar HTML code utilising CSS provided by Bootstrap3.\
Thanks and credit go to Bootstrap3 for the style elements.\
Most thanks go to Oliver Nichols, Ryan Wright and Victoria Sacre for teaching and guidance.

Elliot was here...

