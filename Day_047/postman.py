import smtplib
import os

from dotenv import load_dotenv

load_dotenv()


class PostMan:
    def __init__(self):
        self.MAIL = os.environ.get("EMAIL")
        self.MAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")
        self.RECIPIENT = os.environ.get("RECIPIENT")

    def send(self,message):
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=self.MAIL, password=self.MAIL_PASSWORD)
            connection.sendmail(from_addr=self.MAIL, to_addrs=self.RECIPIENT, msg=message)