import requests, json 

api_key = "dd15ff4fdf60749c09461e291bf6cd2c"
city_name = input("Enter city name : ") 
url = f"http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city_name}"
response = requests.get(url).json()
with open('python.json', 'w') as f:
    json.dump(response, f, indent=4)
if response["cod"] != "404": 
	y = response["main"] 
	current_temperature = y["temp"] 
	current_pressure = y["pressure"] 
	current_humidiy = y["humidity"] 
	z = response["weather"] 
	weather_description = z[0]["description"] 
	print(" Temperature (in kelvin unit) = " +
					str(current_temperature) +
		"\n atmospheric pressure (in hPa unit) = " +
					str(current_pressure) +
		"\n humidity (in percentage) = " +
					str(current_humidiy) +
		"\n description = " +
					str(weather_description)) 

else: 
	print(" City Not Found ") 
