import os
import requests
from dotenv import load_dotenv
load_dotenv()

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):

        self._sheety_token = os.environ.get("SHEETY_TOKEN")
        self.SHEETY_BASE_ENDPOINT ="https://api.sheety.co/d78e6677c5ed06410b698ff2922c94e6/flightDeals/prices"
        self.SHEETY_PUT = f"{self.SHEETY_BASE_ENDPOINT}/[Object ID]"

        self.headers = {
            "Authorization": f"Bearer {self._sheety_token}"
        }
        self.destinations = {}
    def get_data(self):
        response = requests.get(url=self.SHEETY_BASE_ENDPOINT,headers=self.headers)
        data = response.json()
        return data["prices"]



    def update_data(self):
        for city in self.destinations:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{self.SHEETY_BASE_ENDPOINT}/{city['id']}",headers=self.headers,json=new_data)
            response.raise_for_status()







