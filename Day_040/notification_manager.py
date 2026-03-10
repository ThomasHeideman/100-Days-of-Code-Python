import os
import requests
import smtplib
from dotenv import load_dotenv

load_dotenv()


class NotificationManager:

    def __init__(self):

        self.telegram_token = os.environ.get("TELEGRAM_TOKEN")
        self.telegram_id = os.environ.get("TELEGRAM_ID")
        self.url = f"https://api.telegram.org/bot{self.telegram_token}/sendMessage"
        self.email= os.environ.get("EMAIL")
        self.email_password = os.environ.get("EMAIL_PASSWORD")

    def send_message(self, message_body):
        """Sends Telegram message with passed text."""
        params = {
            "chat_id": self.telegram_id,
            "text": message_body,
            "parse_mode": 'HTML',
            "disable_web_page_preview": True
        }

        response = requests.get(self.url, params=params)
        response.raise_for_status()
        print(f"Telegram alert sent!")

    def send_email(self,recipient, message):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()  # makes connection secure trough Transport Layer Security (TLS)
            connection.login(user=self.email, password=self.email_password)
            connection.sendmail(from_addr=self.email, to_addrs=recipient,
                                msg=message.encode('utf-8'))


