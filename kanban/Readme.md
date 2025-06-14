## Project Name
 - Software Engineering & DevOps (Level 6)
 - Software Engineering & Agile module (Level 5)
# Introduction to project
This project is built around a ticket logging kanban board system for Worldline, Customer Information Systems (CIS) team.
This application will allow the team to evolve and change it's ticket/task logging systems, therefore catering for the change in demand and increase work output and client satisfaction.
# Summary of application 
- The purpose of the application is to improve speed and quality of the current kanban board
- Allows a user to sign in and sign out
- Made it so a new user can sign up and assign a user name and password
- Code gets uploaded to its GitHub repository 
# Current Process 
Current process is currently slow and inefficient, and requires constant alterations to deal with change in demand. These issues are looking to be resolved through this Kanban ticket logging system allowing for improved efficiency.
# Different Levels of users 
1) admin 
2) non admin (By Default)
# Level of users and what each can do 
- admin can (Create, read, update, delete) the tickets
- non admin can (Create, read) the tickets
# Install dependencies 
- Bootstrap add on for CSS and HTML on VS code app
- Django python on VS code app
# How to run the environment 
- use command "python manage.py runserver" in terminal when in the correct file location
- Enter "localhost" in internet url
# Security measures added (Level 6)
- Admin user can access admin page 
- Admin user can view the logging in and logging out history
- When signing up a new user there are password requirements and restrictions
- Admin user can view all active accounts
- Only admin user can create create and edit tickets
- A django.yml file has been created to run the build and tests 
- django.yml tests if the application has the most recent updated python version
# Future enhancements 
- Allow the non-admin user to use update and delete tickets
- Add further css to make the application look more presentable
- Expanding on the Kanban board making a priority scale for each ticket
- Making different zones to move the ticket across from, backlog-assigned-in progress-review-done