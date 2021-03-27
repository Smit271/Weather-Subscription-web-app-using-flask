import requests as re   ##--> Request module to request URL from web
import json             ##--> To read json formatted data from web 

class Weather_detail():
    def __init__(self, name):
        self.name = name

    def weather(self):          ##--> method of extracting weather detail from openweathermap API 
        baseurl = 'https://api.openweathermap.org/data/2.5/weather'
        params_dict = {}
        params_dict["APPID"] = '73e1c5ed8a461e6d28983aa53f2faffc'
        #params_dict['zip'] = input("Enter City")  --by zip code
        #params_dict['q'] = input("Enter City Name : \t")
        try :
            params_dict['q'] = self.name
            res = re.get(baseurl, params=params_dict)
            page = res.json()
            #print(page)
            weather_type = page['weather'][0]['description']
            #print(weather_type)
            temp_c = round((page['main']['temp'] - 273.15), 2)
            #print(temp_c)
            details = [page['name'], weather_type, temp_c]
        except:
            weather_type = 'Spelling Mistake'
            temp_c = 0
            details = ['City Not Found', weather_type, temp_c]
        return details
