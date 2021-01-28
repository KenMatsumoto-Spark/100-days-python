import requests


# This class is responsible for talking to the Flight Search API.
class FlightSearch:
    def __init__(self, origin, destiny):
        self.origin = origin
        self.destiny = destiny

    def find_flights(self):
        tequila_endpoint = "https://tequila-api.kiwi.com/v2/search"

        headers = {
            "apikey": ""
        }

        fligh_params = {
            "fly_from": self.origin,
            "fly_to": self.destiny,
            "date_from": "18/01/2021",
            "date_to": "18/07/2021",
        }

        response = requests.get(
            url=tequila_endpoint,
            headers=headers,
            params=fligh_params
        )

        result = response.json()["data"]
        return result
