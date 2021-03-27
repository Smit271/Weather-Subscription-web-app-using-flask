## Live Project on Intertnet link
- http://smit271.pythonanywhere.com/

## Weather Web app and Subscription to daily updates
- This project is getting weather details from https://api.openweathermap.org/data/2.5/weather
- and then show it user in backend i used flask with sqlite database.
- user can also subscibe to it to get daily mails about weather.
- In this i used bootstrap to customize my html page.

## Directory/file  : Work

- static : hold 'css' and 'javascripts' files
- templates : hold 'HTML' and 'image' files
- Current_Weather_API.py : python file to get weather details
- app.py : flask file to start server
- email1.py : python file to send mail to all subscribed users
- form.py : python file generating forms using WTF
- requirement.txt : External library name & versions
- subscribers.db/ txt : Database file


## Requirements

- First run following command to download external library
- python3 -m pip install -r requirement.txt
- After completed go to Run part.


## How to start Flask-Server

- Go to project directory then run following command
- python3 app.py
- go to link given in terminal during starting kernel

## Send emails to Subscribed users

- Run python3 emails.py 


