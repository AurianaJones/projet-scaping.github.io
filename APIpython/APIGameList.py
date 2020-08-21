
import requests, json

#CITY = input("Choisissez votre ville pour connaitre la météo > ")

URL = "BASE_URL  + CITY + "&appid=" + API_KEY"

response = requests.get(URL)




if response.status_code == 200:   #si la réponse est 200 c'est qu'on a accès à l'API
   data = response.json()
   main = data['main']
   coord = data['coord']
   temperature = main['temp']
   humidity = main['humidity']
   pressure = main['pressure']
   report = data['weather']
   name = data['name']
   lon = coord['lon']
   lat = coord['lat']
   tempdegres = temperature - 273.15
   print(f"{CITY:-^30}")
   print(f"Ville: {name}")
   print(f"Temperature: {temperature} K")
   print(f"Temperature: {tempdegres} degres")
   print(f"Humidite: {humidity}")
   print(f"Pression: {pressure}")
   print(f"Temps: {report[0]['description']}")
   print(f"Longitude: {lon} Lattitude: {lat}")

else:
   print("Error in the HTTP request")
