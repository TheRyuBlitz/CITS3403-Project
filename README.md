# Agile-Web-Development-Project


Web Project Specification: Online Formative Assessment
Due 6pm, May 17, 2021

This project is worth 30% of your final grade in the unit must be done in groups of two to four for CITS3403 students. For CITS5505 students, it should be done in pairs.

A Marking Criterion is now available

Project Description
For this project you are required to build an online formative assessment. That is, you should write a web application that simulates a learning experience like a laboratory, and applies some assessment and feedback at the end. The application should be written using HTML, CSS, Flask, AJAX, JQuery, and Bootstrap. The application should allow uses to register, progress through a series of activities saving their progress, complete an assessment at the end, and receive meaningful feedback on their performance. The context of the questions and the type of assessment mechanism is up to you.

Example contexts you could use are:

Educational assessment, like w3schools.
Science laboratories, like this titration lab.
Aural training, to teach people to discern different intervals in music.
A boardgame tutor, like this chess tutor.
Unconcious bias training, like this site.
Aim to focus on one small aspect of learning, so the the exercises, assessment and feedback can be done in about 10 minutes.
Think carefully about the design of the application. It should be:

Informative, so that it presents engaging nontrivial information and skills
Reliable, so that it is not frustrating to use
Intuitive, so that it is easy for a user to complete the assessment and recieve feedback
Engaging, so that it looks good and presents sufficient context for the questions being asked.
The web application should be styled to be interesting and engaging for a user in the selected context. It should offer several views including:
A user view that can view the material, save progress, complete assessments and see the results of completed assessments with some feedback.
A general view that can just view aggregate assessment results, and usage statistics.
In addition to the web application, you should create a private GitHub project that includes a readme describing:

the purpose of the web application, explaining both the context and the assessment mechanism used.
the architecture of the web application.
describe how to launch the web application.
describe some unit tests for the web application, and how to run them.
Include commit logs, showing contributions and review from both contributing students
Group Registration is now available.

Getting Started: Select Website Purpose and Style
Find a partner(s) with (ideally with common interests) and come up with a theme for your application. Discuss styling, how the application is likely to be used, and precisely what functaionality it should offer.

Criteria: Front-end (50%)
The web application must be functional so that the user can access all material and complete the assessment.
The webpage must be implemented using HTML5, CSS and Javascript (or a subset thereof).
All resources used (inlcuding pictures, javascript libraries, css) must be full referenced.
The website must use HTML5, and CSS. The HTML and CSS must pass this validator.
The website must work on Chrome, Firefox and Microsoft Edge
The website should have at least six pages/sections:
one promoting the theme and purpose to users;
a registration/login page for new or returning users;
one or more pages presenting content to users;
one or more pages for users to complete assessments;
one page giving feedback to the user;
one page showing aggregate results and usage statsitics
There must be a consistent style (via css file) for all pages yet each page should be easily identifiable.
Marking Scheme
HTML5 - style, maintainability, validation 10%
CSS -style, maintainability 10%
Javascript-code quality, validation of user generated data, execution 15%
Style - look and feel, usability 10%
Content - coherence, effectiveness 5%
Criteria: Backend functionality (50%)
The second part of the project criteria is the back end functionality of web application. The web application should be implmented using Flask (any additional libraries/modules require unit coordinator approval), and provide at least the following functionality:

A user account and login feature, (as a minimum for administrators)
A method to complete tests and store progress.
A method to assess submissions.
A method to see assessments.
Students should submit a complete Flask application providing the functionality of the project. This should be submitted as a zip including

a full readme.md, describing the design and development of the application, and giving instructions on how to launch from local host.
the git log, showing commits from both partners
all source code, with comments and attributions for any external libraries.
a requirements.txt file, listing all packages used. To build the requirements.txt file for your virtual environment, use the command: pip freeze > requirements.txt while your virtual environment is active.
Do not submit the virtual environment directory, or the .git directory. These are overly large, not required and will result in a penalty if they are submitted.
Marking Scheme
Codecode quality, complexity of task, execution 10%
Persistence and User authentication Database schema and models10%
Testing Unit tests and Selenium Tests10%
Design Purpose and level of complexity10%
Collaboration Git logs and agile processes 10%
The Marking Criterion will be available by the midsemester break.

Demonstration Schedule
In week 12 all members of each team must present and demonstrate their project. A schedule will be set up for demonstrations by week 8.
