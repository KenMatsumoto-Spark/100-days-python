from flight_search import FlightSearch

LONDON_IATA = "LON"
class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, iata_price_data):
        self.iata_prices = iata_price_data

    def find_cheapest(self):

        for city in self.iata_prices:
            search = FlightSearch(LONDON_IATA, city)
            result = search.find_flights()
            cheapest_flight = result[0]
            for flight in result:
                if flight["price"] > cheapest_flight["price"]:
                    cheapest_flight = flight

            if self.iata_prices[city] > cheapest_flight["price"]:
                text = f"Low Price alert! Only {cheapest_flight['price']}, to fly from London-{cheapest_flight['flyFrom']} to {cheapest_flight['cityTo']}-{cheapest_flight['flyTo']}."
                print(text)

