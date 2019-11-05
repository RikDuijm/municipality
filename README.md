# Problems in your neighbourhood – responsive application

This application is developed for a city council and serves 3 purposes:

1. It helps the user to quickly inform the municipality about issues in the neighbourhood. This can be for example: a hole in the ground, street waste,  loose tiles on the sidewalk, a broken lamppost, a broken tree blocking the road, etc. etc.
The user can check if someone else reported the problem and if not, report it himself in a few, quick steps.
2. It helps the municipality to safe time: since the user can check if an issue is reported, the municipality won’t receive reports / calls of the same problem over and over again.
3. It helps the municipality to show transparency towards its citizens by reporting what they do to solve problems and by showing how many problems they actually do solve!

- [**View the website here!**](#)
- [**View website development in Cloud9!**](https://github.com/RikDuijm/municipality/)

## Contents Table
1. [**UX**](#ux)
    - [The Audience](#audience)
    - [User Stories](#user-stories)
    - [The application](#application)
    - [User Experience](#user-experience)
    - [Design Ideas](#design-ideas)
    - [Wireframes](#wireframes)

2. [**Functionality and Features**](#features)
    - [Existing Features](#existing-features)
    - [Features Left to Implement](#features-left-to-implement)

3. [**Technologies Used**](#technologies-used)

4. [**Testing**](#testing)
   - [Manual Testing](#manual-testing)
   - [Automated Testing](#automated-testing)
   - [Note for Code Institute](#note)

5. [**Deployment**](#deployment)

6. [**Credits**](#credits)
    - [**Contents**](#contents)
    - [**Help with code**](#help-with-code)
    - [**Acknowledgements**](#acknowledgements)

## <a name="ux"></a>UX
### <a name="audience"></a>The Audience
**Who is the target audience?**<br>
The citizens of a given municipality.

### <a name="user-stories"></a>User Stories
**As the municipality, I would like to serve my citizens by offering an application that:**<br>
- gives a quick overview on reported problems and the status of those problems
- gives a possibility to quickly report problems

**Furthermore, as the municipality, I would like to make sure that:**<br>
- only registered citizens can report a problem.
- citizens cannot comment or delete reports

**As a user I’d like to:**<br>
- see if problems in my neighbourhood are reported to the municipality.
- see what is being done to solve those problems
- have the possibility to report a problem as quickly as possible, without any hassle and to see a written proof that I’ve reported this.

### <a name="application"></a>The application
**What are we making?**<br>
Given the obvious desire of a municipality to serve its citizens as transparently as possible, we want to set up a clean, fast and well-arranged application, which gives the user the opportunity to quickly scan for reported problems in his neighbourhood. If the user sees that something isn’t reported yet, he has to log in – to minimize the possibility if misuse of the app. After logging in, the user can report a new issue quickly and sees that is has been reported.
The whole process must be easy and painless, something very refreshing for the citizens after earlier experiences. This new elected guys actually can think!

The municipality wants the user to first check if a problem is already reported, to minimize the problems that are reported several times. Therefore, on the homepage the first thing that a user can do is to check by street name if a problem is already registered. Afterwards he has to login, to be able to report a new issue. This is to minimalize the abuse of the page.

Only administrators of the municipality can delete or comment (informing the public about what’s being done) on a problem. So there must be 2 environments on the website, based on the rights of a user (citizen or administrator).

**Why does the user want this?**<br>
The user / the citizen wants firstly to be able to see if a problem is already reported, and secondly communicate problems with the municipality without hassle / having to waste time in a phone call. Finally he wants to see his report back, so that he’s sure that the municipality has to do something about it.

### <a name="user-experience"></a>User Experience
**What makes a good user experience?**<br>
- Presenting an easy navigable, comprehensive tool to search for problems in a given street and, if a problem is not reported yet, to report it easily.
- To lower the threshold for a citizen to communicate with the municipality, it must take the least amount of time possible to report a problem.
- The idea that the municipality act upon reported problems.

### <a name="design-ideas"></a>Design Ideas
The website must be accessible. The user must be able to navigate quickly and intuitively and must easily find all relevant information. Given the fact that it’s a website of a city council it also must have a business-like and lean design.
Based on those ideas, I made the following choices:

**Font**<br>
I chose the Font 'Roboto', sans-serif because this is a soothing, modern letter. This contributes to the clarity of the page.

**Colours**<br>
I chose to work with only three colours: a bright red, a black font and a clear white background. This also contributes to the clarity of the page, but shows also its business-like character and a certain authority.

**Content**<br>
The website is mobile first. The user must be able to report a problem on the spot, not having to start up his computer to do so. It means that the amount of information presented must be minimized. When entering the website it must be clear that reporting a problem is an easy, quick and painless process.

**Progress bar**<br>
To emphasize the ease of reporting an issue we make use of a progress bar, already in 25% when entering the website. That’s how quick it is!

**Images**<br>
Although the website must look visually nice, images are of no importance. It’s all about functionality. Therefore, the only image you see is the municipality arms.

### <a name="wireframes"></a>Wireframes
This is a mobile first app. I expect the client to use this app mostly on a mobile phone walking on the street and noticing something, or maybe on a tablet afterwards. I don’t expect many users to use a desktop, but it’s certainly also designed for that, especially since most administrator might use a desktop.

The whole design and the choices I made are based on that assumption. I made six mobile wireframes, reflecting the process of reporting a problem described above.
1 [initial screen](https://github.com/RikDuijm/municipality/blob/master/user-design-experience/Municipality%20App%201.jpg)<br>
2 [screen after searching on street name](https://github.com/RikDuijm/municipality/blob/master/user-design-experience/Municipality%20App%202.jpg)<br>
3 [screen for log in](https://github.com/RikDuijm/municipality/blob/master/user-design-experience/Municipality%20App%203.jpg)<br>
4 [overview of reports](https://github.com/RikDuijm/municipality/blob/master/user-design-experience/Municipality%20App%204.jpg)<br>
5 [form to report a problem](https://github.com/RikDuijm/municipality/blob/master/user-design-experience/Municipality%20App%205.jpg)

Basically I created exactly what I had in mind, with the following exceptions:

In wireframe 4 it was possible for a user to comment on a problem. To minimize possible abuse (or complaint about the time it takes for the municipality to act upon something) I decided to make this option not available for the public, but only for the administrator. Also, the position of the button “comment” (and “delete”) has changed, and are not placed vertically instead of horizontally, because of readability issues on a mobile phone.

Initially I was thinking about creating a Dashboard with information about the amount of problems the municipality solved. However I decided to not develop this, but move on with my studies. Basically I’m behind my schedule because of personal problems distracting me.

**Larger screens**<br>
There is hardly any difference between the mobile and larger screens. Because of that I didn’t feel the necessity to create wireframes for larger screens.

## <a name="features"></a>Functionality and Features
### <a name="existing-features"></a>Existing features
**Search functionality**<br>
The municipality wants the user to first search if a problem is already reported. On the homepage there is a search functionality with the instruction “1. Look for reported problems – enter street name”.

**Login and Registration functionalities**<br>
After searching for reported problems in a given street the user has the possibility to login to report a new problem. Obviously therefore he also has the possibility to register himself. In this application he can choose username and password, but obviously in real life it would be possible that he has to register with this full name and id-number, for example. If a user wants to register with an existing username, he gets a message that that username is already taken. After registering the user is automatically sent to the login page, where he has to provide his credentials. If he makes a typo logging in he receives a message to try it again.

**Report form**<br>
After successfully logging in the user is sent to the page where he can use a form to report a problem. His username is already selected and not changeable and also the date / time of the report is filled-in already. He can only fill out the street name and the problem he is reporting. Optionally he can also send in a photo taken of the photo. This photo enters the database. However, it won’t show on the website.

**Overview of reports**<br>
After submitting the form the user is sent to a general overview of all the reported problems. The most recently reported problem will be on top of the list, so the user will see his report immediately. He can click on the report to see if the municipality already posted a reaction.

**Navigation bar and environment for admin**<br>
There is also a navigation bar on top of the page. If a user logs in using the navigation bar, he technically can report a problem at once, without having to look if it’s already reported. Obviously I could choose to delete the login in the navigation bar, but a user can also be an administrator, and I’ve chosen to maintain the login so that the administrator can enter the system as quickly as possible. He can do so to provide his credentials (for now Username: admin,  Password: admin) and he get an overview of all the reports, most recently reported first. Here, he can comment on reports or delete them, something a regular user cannot do. Obviously the administrator can also search per street name.

**Footer**<br>
Allows the user to see the contact details and opening hours of the municipality and their social media canals (Facebook, Instagram, Twitter). None are clickable for now.

### <a name="features-left-to-implement"></a>Features left to Implement
**Dashboard**<br>
To show how many problems there has been reported per street / how long it took to solve what type of problems. This might be desirable for the municipality to show off how fantastic a job they are doing, or maybe to make clear that they need more infrastructure / resources to do the job.

**Pictures of problems on website**<br>
For now, people can send in a file / photo with the form. Obviously this could help the municipality to get a quick and clear impression on the (urgency of a) problem. It could also help a user to understand whether this is the problem he also wanted to report or not.
I figured out how to retrieve this internally using the filename, but not how to retrieve this on the website in a nice and consistent manner. So for now, I maintained the possibility for the user to send in a file, but it won’t show in the report.

## <a name="ux"></a>Technologies Used
•	I used HTML, CSS, Python (Pymongo), Flask, Jinja2 jQuery and JavaScript.<br>
•	IDE: I used Gitpod.<br>
•	I used Bootstrap for the grid system of the page, the form and the progress bar.<br>
•	I used the libraries Re and Bcrypt for the search and register/login functionality respectively.<br>
•	I used Tempus Dominus as a date / time picker<br>
•	Google fonts has been used for the fonts.<br>
•	I used Font Awesome for the icons in the footer of the website and icons8.com for the icon in the navigation bar / in the background of the page.<br>
•	JQuery was used to pre-set the date and time in the form.<br>
•	JavaScript to make it impossible for a user to use spaces in his username when registering.<br>
•	Google Chrome developer tools<br>
•	Bash / Ubuntu to commit my project and to push it to Github (CHECK)<br>
•	Github for version control<br>
•	Heroku for users to view the deployed version of the website.

## <a name="testing"></a>Testing
### <a name="manual-testing"></a>Manual testing<br>
#### Responsive testing ####<br>
#### Testing different browsers ####<br>

#### Testing the functionality ####
I tested the functionalities by going through the steps a user should take to report a problem.

**1. Search Functionality**..
...1. Filling in a street name that is already in the database (because a problem has been reported):..
    Expected result: street name + problem. Works correctly.
    2. Testing if the search functionality is case sensitive
    Expected result: not case sensitive. I tested this by filling in lower key, capital letters and a combination of upper and lower. Works correctly.
    3. Testing if all the reports about a given street show up
    Expected result: all reports show up. Works correctly.
    4. Testing what happens if a street is not in the database
    Expected result: no results shown. Works correctly.

**2. Login Functionality**
    1. Does the button login show in all possible scenarios of step 1?
    Expected result: yes. Works correctly.
    2. User (citizen) fills in correct credentials
    Expected result: he is redirected to the “add report” page, and the message “Welcome [username]” is shown. His username is already filled-in and the user cannot change this. Also the date is already filled-in. This is changeable.
    Works correctly.
    3. User (citizen) fills in unknown username but correct password
    Expected result: receives message “wrong credentials. Works correctly.
    4. User (citizen) fills in correct username but incorrect password
    Expected result: receives message “wrong credentials. Works correctly.
    5. Administrator fills in correct credentials
    Expected result: he is redirected to an overview of all reported problems. This is the administration environment, in which admin may comment on a problem or delete it. Regular user cannot reach this. Message “Logged in as Admin” is shown.
    Works correctly
    6. Administrator fills in wrong username but correct password
    Expected result: receives message “wrong credentials. Works correctly.
    7. Administrator fills in correct username but incorrect password
    Expected result: receives message “wrong credentials. Works correctly.

**3 Register Functionality**
1: User chooses a username that already exists.
Expected result: user receives a message “username already taken”. Works correctly.

2: User chooses a username that doesn’t exist yet.
Expected result: he is redirected to the login page. Works correctly. However: the user doesn’t have to log in anymore – he’s already logged in automatically after registering. Since this actually speeds up the process for the user, I choose to leave it like this, but redirect immediately to the “add report” page.

3: User tries to have a space in his username (so he wants it to exist of 2 separate words, i.e. first and last name).
Expected result: this is automatically disabled. Works correctly.

D: Create Report Functionality
1: User files a report, describing the problem, entering the street name, and possibly adjust the date / time. He also can optionally upload a photo of the problem.
Expected result: after submitting he’s redirected to an overview of all the reported problems, last report (his own) shown first.
Works correctly.

2: User doesn’t mention the street name:
Expected result: upon submitting he gets a message that he has to do so before he’s able to file the report. Works correctly.

3: User doesn’t mention what the problem is:
Expected result: upon submitting he gets a message that he has to do so before he’s able to file the report. Works correctly.

E1: Read Functionality (reported problems, regular user)
Expected result if logged in as regular user:
Page that shows all the reports, ordered by date/time, latest filed report shown first. Reports show name of the street, reported problem, date and username of the person that filed the report. Toggle function that shows the response of the municipality as soon as there is a response.
Works correctly.

E2: Read Functionality (reported problems, administrator)
Expected result if logged in as administrator:
Page that shows all the reports, ordered by date/time, latest filed report shown first. Reports show name of the street, reported problem, date and username of the person that filed the report. Toggle function that shows the response of the municipality as soon as there is a response.

In this environment every item has 2 buttons: Comment and Delete.

E2.1 Update Functionality (comment button):
The admin can comment on the report, with full rights to update / change every field. Additionally he can add a reply of the municipality (i.e.: we’re working on it, problem solved, etc.). After submitting the admin is redirected to the list of reported problems, where he can check his update.
Works correctly.

E.2.2 Delete Functionality (delete button):
The admin can delete a report. Report disappears from the list of reported problems.
Works correctly.

F Logout Functionality:
When clicked upon the user is logged out and redirected to the homepage.
Works correctly.



### <a name="automated-testing"></a>Automated Testing
**Validation services**<br>
The following validation services were used to check the validity of my code.

- W3C Markup Validation Service was used to validate HTML.
- W3C CSS validation was used to validate CSS.
- JSHint was used to validate JavaScript.

### <a name="note"></a>Note for Code Institute
After finishing my first Milestone Project I made a complaint that we hadn't had a single lesson about testing our code, but that you expect us to be able to do this. The reply I received:<br>
I have passed your valuable feedback over to the learning Success Team. I have spoken to someone from the team and they agreed that more information about testing and deployment is due. This is being looked into and in the process of being improved.<br>
I again made a complaint upon starting this Milestone Project:<br>
So far we only got a quick introduction to Jasmine with only 1 specific example. I feel that in the Milestone Projects there's an emphasis on the importance of testing, that isn't reflected in the course and based on this 1 lesson I can't create automated testing for this project.<br>

Now, with the third milestone, again I don’t feel that we received enough – if any – instructions or practice about how to test our projects. I really feel that if you think this is important you should teach us well how to do this. I don’t think I have received the tools to be able to do so.

## <a name="deployment"></a>Deployment

## <a name="credits"></a>Credits
### <a name="contents"></a>Contents

**Icons on Maps**<br>
The icons for the maps were taken from icons8.com and  are free of use as long as you put a link to the website - which I did in the footer.

### <a name="help-with-code"></a>Help with code

## <a name="acknowledgements"></a>Acknowledgements
Thanks to my mentor Spencer Barriball and fellow student Peter Lenting for discussing ideas and providing help on several occasions.

