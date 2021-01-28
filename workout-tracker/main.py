import requests
from datetime import datetime
APP_ID =
API_KEY =
today = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%H:%M:%S")
nutrition_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint =

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

exercise_description = input("Describe your exercises: ")
nutrition_params = {
    "query": exercise_description,
    "gender": "male",
    "weight_kg": 60,
    "height_cm": 167,
    "age": 28
}

sheety_headers = {
    "Content-Type": "application/json",
    "Authorization":
}

response = requests.post(url=nutrition_endpoint, headers=headers, json=nutrition_params)
data = response.json()["exercises"]

for index in range(0, len(data)):
    sheety_post_params = {
        "workout": {
            "date": today,
            "time": time,
            "exercise": data[index]["name"].title(),
            "duration": data[index]["duration_min"],
            "calories": data[index]["nf_calories"]
        }
    }

    response = requests.post(url=sheety_endpoint, headers=sheety_headers, json=sheety_post_params)






