from django.shortcuts import render
from . import token
import requests
from time import sleep

# Create your views here.
def index(request):
	api = token.WEATHER_API_KEY
	city = 'Las Vegas'
	url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(city,api)
	responsed = requests.get(url).json()
	
	#print(responsed.json())
	#sleep(1)
	
	weather = {
		'city': city,
		'temp': responsed['main']['temp'],
		'desc': responsed['weather'][0]['description'],
		'icon': responsed['weather'][0]['icon']

	}

	dic = {'weather':weather}
	return render (request, 'weatherApp/home.html', dic)