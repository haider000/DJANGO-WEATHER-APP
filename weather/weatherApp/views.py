from django.shortcuts import render,redirect
from . import token
import requests
from time import sleep

# Create your views here.

def index(request):
	if(request.method == 'POST'):
		city = request.POST['city']
		api = token.WEATHER_API_KEY
		url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(city,api)
		responsed = requests.get(url).json()		
		#print(responsed.json())
		sleep(1)		
		weather = {
			'city': city,
			'temp': responsed['main']['temp'],
			'desc': responsed['weather'][0]['description'],
			'icon': responsed['weather'][0]['icon']
		}
		dic = {'weather':weather}
		return render (request, 'weatherApp/weather.html', dic)
	return render(request,'weatherApp/home.html')