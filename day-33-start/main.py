import requests
from datetime import datetime
import math
import smtplib
import time
MY_LAT = 37.7510
MY_LON = -97.8220
MY_EMAIL = "a@gmail.com"
MY_PASSWORD = "senha"
PARAMETERS = {
    "lat": MY_LAT,
    "lng": MY_LON,
    "formatted": 0
}
my_position = (37.7510, -97.8220)

def catch_iss_location():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    data = response.json()
    longitute = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])
    iss_position = (longitute, latitude)
    return iss_position

def is_iss_close():
    iss_position = catch_iss_location()
    if math.hypot(my_position[0]-iss_position[0], my_position[1]-iss_position[1]) <= 5:
        return True
    return False

def is_dark():
    response = requests.get("http://api.sunrise-sunset.org/json", params=PARAMETERS)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()

    if sunset < time_now.hour < sunrise -1:
        return True
    return False


while True:
    time.sleep(60)
    if is_iss_close() and is_dark():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up\n\nThe ISS is above you in the sky."
        )