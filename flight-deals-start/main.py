from data_manager import DataManager
from flight_data import FlightData
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

sheet = DataManager()

# sheet.asign_iata()
# sheet.update_google_sheet()
# sheet.fetch_iata_price()
check_prices = FlightData(sheet.prices)

check_prices.find_cheapest()