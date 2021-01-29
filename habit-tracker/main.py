import requests
from datetime import datetime
# creating a user ----------------------------------------------------------------------------
pixela_endpoint = ""

TOKEN = 
USERNAME = ""
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# creating a graph --------------------------------------------------------------

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

GRAPH_ID = "graph1"

graph_params = {
    "id": GRAPH_ID,
    "name": "Cycling-graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

# posting a pixel --------------------------------------------------------------

posting_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now().strftime('%Y%m%d')

posting_pixel_params = {
    "date": today,
    "quantity": "30.2"
}

# response = requests.post(url=posting_pixel_endpoint, json=posting_pixel_params, headers=headers)
# print(response.text)

# putting(updating) a pixel --------------------------------------------------------------
updating_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"

updating_pixel_params = {
    "quantity": "100.2"
}

# response = requests.put(url=updating_pixel_endpoint, json=updating_pixel_params, headers=headers)
# print(response.text)

# deleting a pixel -------------------------------------------------------------
deleting_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"

response = requests.delete(url=deleting_pixel_endpoint, headers=headers)
print(response.text)