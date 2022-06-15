# Simple Task Management System
## Project Description
This program is written in python and was designed to assist a small business in managing 
tasks assigned to each member of a team. Its functions include logging-in with a team member
specific name and password and providing the user with differnt task managing options.

The user may store, display and edit tasks and the user set to admin my add users and generate
reports regarding tasks and users registered with the program.

## Functionality
First, the program will prompt the user for their name and password. The program will compare
the users input to those in a txt file called 'users.txt', and if they match the user is logged in.

The user is then provided with a menu containing the options: add tasks, view user specific tasks and
view all tasks while only the admin profile may add users, generate reports and view the statistics of the team.

Depending on the menu option seleceted by the user, the program will either read from and/or write to a txt
file called 'tasks.txt' and when the admin generates a report, the information and stats regarding all tasks
will be written to a txt file called 'task_overview.txt' and the information and stats regarding all team members
will be written to a txt file called 'user_overview.txt'.

## Contributors
I developed this program on my own and it was reviewed by the HyperionDev code reviewers.
