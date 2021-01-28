import requests

OMN_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_params = {
    "appid": "66e845ec3278679a11006a40dc7d4191",
    "lat": -23.52178,
    "lon": -47.4796,
    "exclude": "current,minutely,daily"
}


response = requests.get(url=OMN_endpoint, params=api_params)
response.raise_for_status()
data = response.json()
will_rain = False
for hour in range(0,12):
    if data["hourly"][hour]["weather"][0]["id"] < 700:
        will_rain = True
if will_rain == True:
    print("Bring an umbrella!")