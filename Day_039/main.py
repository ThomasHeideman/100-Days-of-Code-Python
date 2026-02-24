from data_manager import DataManager
from flight_data import find_cheapest
from flight_search import FlightSearch
from notification_manager import NotificationManager
import time
from datetime import datetime, timedelta

DEPT_AIRPORT_CODE = "AMS"

dm = DataManager()
fs = FlightSearch()
nm= NotificationManager()

# sheet_data = dm.get_data()
sheet_data = [{'city': 'Paris', 'iataCode': 'PAR', 'lowestPrice': 454, 'id': 2}, {'city': 'Frankfurt', 'iataCode': 'FRA', 'lowestPrice': 452, 'id': 3}, {'city': 'Tokyo', 'iataCode': 'TYO', 'lowestPrice': 485, 'id': 4}, {'city': 'Hong Kong', 'iataCode': 'HKG', 'lowestPrice': 551, 'id': 5}, {'city': 'Istanbul', 'iataCode': 'IST', 'lowestPrice': 95, 'id': 6}, {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'lowestPrice': 414, 'id': 7}, {'city': 'New York', 'iataCode': 'NYC', 'lowestPrice': 240, 'id': 8}, {'city': 'San Francisco', 'iataCode': 'SFO', 'lowestPrice': 260, 'id': 9}, {'city': 'Dublin', 'iataCode': 'DBN', 'lowestPrice': 378, 'id': 10}]

for destination in sheet_data:
    if destination["iataCode"] == "":
        iata = fs.get_iata(destination["city"])
        destination["iataCode"] =iata
        time.sleep(1)


dm.destinations = sheet_data
# dm.update_data()

# Search flights:
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))
for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")
    flights = fs.search(
        DEPT_AIRPORT_CODE,
        destination["iataCode"],
        tomorrow,
        six_month_from_today
    )

    cheapest_flight = find_cheapest(flights)
    print(f"{destination["city"]}: €{cheapest_flight.price}")

    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        nm.send_telegram_message(cheapest_flight)

    time.sleep(2)



