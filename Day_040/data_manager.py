import os
import requests
from dotenv import load_dotenv

load_dotenv()


class DataManager:

    def __init__(self):
        self._sheety_token = os.environ.get("SHEETY_TOKEN")
        self.SHEETY_PRICES_ENDPOINT = os.environ["SHEETY_PRICES_ENDPOINT"]
        self.SHEETY_USERS_ENDPOINT = os.environ["SHEETY_USERS_ENDPOINT"]

        self.headers = {
            "Authorization": f"Bearer {self._sheety_token}"
        }
        self.destination_data = {}
        self.user_data = {}
        self.user_mails = []

    def get_destination_data(self):

        response = requests.get(url=self.SHEETY_PRICES_ENDPOINT, headers=self.headers)
        response.raise_for_status()
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{self.SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=self.headers
            )
            print(f"Status update: {response.status_code}")

    def get_customer_emails(self):
        response = requests.get(url=self.SHEETY_USERS_ENDPOINT, headers=self.headers)
        response.raise_for_status()
        data = response.json()
        self.user_data = data["users"]

        return self.user_data

