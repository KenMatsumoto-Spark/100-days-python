import requests

class DataManager:
    def __init__(self):
        self.iata_codes = []
        self.prices = {
            "PAR": 90,
            "BER": 42,
            "TYO": 485,
            "SYD": 551,
            "IST": 95,
            "KUL": 414,
            "NYC": 240,
            "SFO": 260,
            "CPT": 378
        }

    def asign_iata(self):
        tequila_endpoint = "https://tequila-api.kiwi.com/locations/query"
        sheety_endpoint = "https://api.sheety.co/8e7ef2b96e4469909514ca725390ed64/flightDeals/prices"

        read_sheety_response = requests.get(url=sheety_endpoint)

        cities = [places['city'] for places in read_sheety_response.json()["prices"]]

        for city in cities:

            headers = {
                "apikey": ""
            }

            city_params = {
                "term": city
            }
            read_tequila_response = requests.get(url=tequila_endpoint, headers=headers, params=city_params)
            self.iata_codes.append(read_tequila_response.json()["locations"][0]["code"])


    def update_google_sheet(self):

        sheety_endpoint = "https://api.sheety.co/8e7ef2b96e4469909514ca725390ed64/flightDeals/prices"

        sheety_headers = {
            "Content-Type": "application/json"
        }

        for index in range(2, len(self.iata_codes)+2):
            new_params = {
                "price": {
                "iataCode": self.iata_codes[index-2]
                }
            }
            update_sheety_response = requests.put(url=f"{sheety_endpoint}/{index}", headers=sheety_headers,
                                                  json=new_params)

    def fetch_iata_price(self):
        sheety_endpoint = "https://api.sheety.co/8e7ef2b96e4469909514ca725390ed64/flightDeals/prices"

        read_sheety_response = requests.get(url=sheety_endpoint)

        self.prices = {places['iataCode']: places["lowestPrice"] for places in read_sheety_response.json()["prices"]}
