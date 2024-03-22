import urllib.request
import json
from django.shortcuts import render


import requests



def index(request):

    if request.method == 'POST':
        city = request.POST['city']
        url = "https://weather-api138.p.rapidapi.com/weather"


        headers = {
            "X-RapidAPI-Key": "81fc798222msha2449c6c4b8d317p1b9d2cjsnbf5c36c2b349",
            "X-RapidAPI-Host": "weather-api138.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params={"city_name":city})


        # source = urllib.request.urlopen(f'https://api.openweathermap.org/data/3.0/onecall?lat=33.44&lon=-94.04&appid={"f8cd275b618cead523c928876adaa5fd"}').read()
        list_of_data = response.json()

        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ', '
            + str(list_of_data['coord']['lat']),

            "temp": str(round(int(list_of_data['main']['temp'])- 273.15)) + ' °C',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            'main': str(list_of_data['weather'][0]['main']),
            'description': str(list_of_data['weather'][0]['description']),
            'icon': list_of_data['weather'][0]['icon'],

        }
        print(data)
    else:
        data = {}

    return render(request, "main/index.html", data)