
import requests, json

#CITY = input("Choisissez votre ville pour connaitre la météo > ")

URL = "https://raw.githubusercontent.com/AurianaJones/projet-scaping.github.io/adrien_api_py/APIpython/run_results.json"

response = requests.get(URL)




if response.status_code == 200:   #si la réponse est 200 c'est qu'on a accès à l'API
   data = response.json()
   title = data['title']
 #  name = data['name']

      
   print(f"title: {title[0]['name']}")


#   print(f"name: {name}")

else:
   print("Error in the HTTP request")
