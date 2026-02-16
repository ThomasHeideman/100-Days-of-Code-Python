import requests
from secrets import open_weather_key, telegram_token, telegram_id, twillio_auth_token, twillio_account_sid
from twilio.rest import Client
parameters = {
# "q": "Aalsmeer",
"appid": open_weather_key,
"units": "metric",
"lat" : 52.266750,
"lon" : 4.748940,
"cnt":4
}

response = requests.get(url=f"https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()

will_rain = False
for item in data["list"]:
    condition_code = item['weather'][0]["id"]
    if condition_code < 700:
        will_rain = True
        break


def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{telegram_token}/sendMessage"
    params = {
        "chat_id": telegram_id,
        "text": text
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    print("Success! Check your phone!.")

def send_whatsapp_message(text):
    account_sid = twillio_account_sid
    auth_token = twillio_auth_token
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=text,
        to='whatsapp:+31642727696'
    )

    print(message.sid)

will_rain = True

if will_rain:
    message = "☔ Thomas, it's going to rain in Aalsmeer! Bring your umbrella! "
    send_telegram_message(message)
    send_whatsapp_message(message)




