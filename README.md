# Event manager API

## Functional
This project implements an api for adding and receiving events by the user

## Preperations
Use this commad in Terminal 'git clone https://github.com/MaksRedka/Event_manager_Poly-tech.git' to copy this repo to your foldel

Then you can create virual environment or install dependencies to your PC
Use this commad 'python -m pip install -r requirements.txt' in Terminal to install dependencies

## How to start project
1. In the terminal, go to the folder where the 'manage.py' file is located
2. Use command 'python manage.py runserver' to start your server
3. You can enter this link '127.0.0.1:8000/events/api/' or use any programs like Postman

## Django Admin
You can add event or user by login in Django Admin
1. Enter the link '127.0.0.1:8000/admin/'
2. Login: admin Password: admin

## How to get Token
There are a few ways to get user Token
1. Enter Django Admin and copy it
2. Use Posrman or any request system, send POST request to this link 'http://127.0.0.1:8000/events/api-token-auth/' with username and passwor

Example for Mac:
'http post http://127.0.0.1:8000/api-token-auth/ username=admin password=admin'

Example for something like Postman:
![image](https://user-images.githubusercontent.com/79270764/217400019-4d6d9d29-df0b-40f7-9287-5fcc44bc326a.png)

## API requests
You can post and get Events, to do this look at examples below

POST Example:
![image](https://user-images.githubusercontent.com/79270764/217400234-b135d3f7-9de6-4f9b-8a0b-22035c8569b9.png)

GET Example:
![image](https://user-images.githubusercontent.com/79270764/217400292-5894feed-8527-4b0b-a721-ebf443c6f132.png)

## Testing
If you want to run tests you need to start server
Then type in Terminal 'python manage.py test' from folder with manage.py file

**Good Luck**
