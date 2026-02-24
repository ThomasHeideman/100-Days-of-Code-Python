import os
import requests
from dotenv import load_dotenv
import datetime
load_dotenv()

class FlightSearch:

    def __init__(self):
        self._api_key = os.environ.get("AMADEUS_KEY")
        self._api_secret = os.environ.get("AMADEUS_SECRET")
        self.iata_endpoint = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
        self.auth_endpoint = "https://test.api.amadeus.com/v1/security/oauth2/token"
        self.search_endpoint =  "https://test.api.amadeus.com/v2/shopping/flight-offers"
        self.token = self._get_token()
        self.tomorrow=datetime.date.today() + datetime.timedelta(days=1)
        self.headers = {
            "Authorization": f"Bearer {self.token}"
        }

    def _get_token(self):
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
        }
        auth_data = {
            "grant_type": "client_credentials",
            "client_id": self._api_key,
            "client_secret": self._api_secret
        }

        response = requests.post(url=self.auth_endpoint, headers=headers, data=auth_data)
        token = response.json()
        return token['access_token']

    def get_iata(self,city):

        params = {
            "keyword": city,
            "max": "2",
            "include": "AIRPORTS"
        }
        amadeus_response = requests.get(url=f"{self.iata_endpoint}",headers=self.headers, params=params)
        if amadeus_response.status_code != 200:
            print(f"Status code: {amadeus_response.status_code}")
            print(f"Response text: {amadeus_response.text}")
            return "ERROR"
        data = amadeus_response.json()
        try:
            iata_code = data["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city}.")
            return "Not Found"

        return iata_code

    def search(self,dep_code, dest_code,dep_date,return_date):

        params = {
            "originLocationCode": dep_code,
            "destinationLocationCode":dest_code,
            "departureDate":dep_date.strftime("%Y-%m-%d"),
            "returnDate": return_date.strftime("%Y-%m-%d"),
            "adults" : 1,
            "nonStop": "true",
            "currencyCode" : "EUR",
            "max": 10,
        }
        response = requests.get(url=f"{self.search_endpoint}", headers=self.headers, params=params)

        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print("There was a problem with the flight search.\n"
                  "For details on status codes, check the API documentation:\n"
                  "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api"
                  "-reference")
            print("Response body:", response.text)
            return None


        return response.json()

