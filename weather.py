import urllib.request
import json


def get_weather(city):

  url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=adcb882ea837148878722e69044dc372'

  request = urllib.request.urlopen(url)
  result = json.loads(request.read())

  #print(result)

  temp_c = round(result["main"]["temp"] - 273.15,2)
  #0K − 273.15 = -273.1°C

  return temp_c