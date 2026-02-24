import os
import requests
from dotenv import load_dotenv

load_dotenv()

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.telegram_token = os.environ.get("TELEGRAM_TOKEN")
        self.telegram_id = os.environ.get("TELEGRAM_ID")
        self.url = f"https://api.telegram.org/bot{self.telegram_token}/sendMessage"

    def send_telegram_message(self, flight_details):
        url = f"https://api.telegram.org/bot{self.telegram_token}/sendMessage"
        lowest = flight_details.price
        origin = flight_details.dept_airport
        destination = flight_details.dest_airport
        dept_date = flight_details.dept_date
        return_date = flight_details.return_date

        text = f'''
        <b>Low price alert!🔔</b>
        
        From 🛫:  {origin}
        To 🛬: {destination}
        On: {dept_date} 
        Until: {return_date}
        
        <b>Only €{lowest} </b>
        '''

        params = {
            "chat_id": self.telegram_id,
            "text": text,
            "parse_mode": 'HTML',
            "disable_web_page_preview": True
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        print("Success! Check your phone!")
