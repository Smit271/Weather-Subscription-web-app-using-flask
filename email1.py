##--> Importing Libraries
from email import message                     ##--> From Email Module importing message class
import smtplib as s                           ##--> smtplib Module as SMTP connection
from Current_Weather_API import Weather_detail##--> Made Module for extracting weather details
from datetime import date		              ##--> For printing Date in log file 
import mysql.connector

today = date.today()


def get_data_from_txt():
    names = []
    mail_ids = []
    city_names = []
    with open('subscribers.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            name = line.split(',')[0].capitalize()
            mail_id = line.split(',')[1]
            city_name = line.split(',')[2].strip().capitalize() 
            names.append(name)
            mail_ids.append(mail_id)
            city_names.append(city_name)
    f.close()
    return names, mail_ids, city_names


def get_weather_details(cities):
    details = []
    for city in cities:
        details.append(Weather_detail(str(city)).weather())
        #temp = details[2]
        #discription = details[1]
    return details


#weather = Weather_detail('ranip')
def sending(name, addresss, city_name, detail):                                ##--> Method to send mails to subscribed users
    ob = s.SMTP("smtp.gmail.com", 587)
    ob.starttls()
    ob.login("botofsmitpanchal@gmail.com", "botofsmitpanchal123")
    subject = f"Today's Weather for you {name}"
    body    = "City : {}\nWeather Type : {}\nTemperature(C) : {}\n".format(city_name, detail[1], detail[2])
    message = "Subject:{}\n\n{}".format(subject, body)
    listofAddress = addresss  ##--> Subscribed User
    try:
        ob.sendmail("botofsmitpanchal@gmail.com", listofAddress, message)
    except:
        pass

    #print(f"Successfull sent to {listofAddress}\nDate: {today}\n")
    ob.quit()
#city, weather_type, temp_c = weather.weather()


def main():
    names, mail_ids, city_names = get_data_from_txt()
    weather_details = get_weather_details(city_names)
    for i in range(len(mail_ids)):
        sending(names[i], mail_ids[i], city_names[i], weather_details[i])

main()