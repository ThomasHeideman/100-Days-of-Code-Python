import requests
from datetime import datetime, timezone
from secrets import password, my_email,my_send_to_mail
import smtplib
import time

MY_LAT = 52.266750
MY_LONG = 4.748940

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

def is_it_dark():
    """
        Checks the sunrise and sunset times for the current location and compares them to the current time.
        :return: Boolean (True if it is currently dark, False if it is light).
        """
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now_utc = datetime.now(timezone.utc)
    if time_now_utc.hour >= sunset or time_now_utc.hour <= sunrise:
        return True
    return False


def send_email():
    """
        Establishes a connection to the SMTP server and sends a notification email to the user.
        :return: None
        """
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_send_to_mail,
                            msg="Subject:Look up!\n\nInternational Space Station is overhead!")


def track_iss():
    """
        Fetches the current ISS position, calculates the distance to the user's location,
        and triggers an email if conditions (proximity and darkness) are met.
        :return: None
        """
    response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
    response_iss.raise_for_status()
    data_iss = response_iss.json()

    iss_latitude = float(data_iss["iss_position"]["latitude"])
    iss_longitude = float(data_iss["iss_position"]["longitude"])

    lat_diff = abs(MY_LAT - iss_latitude)
    lng_diff = abs(MY_LONG - iss_longitude)

    iss_close = lat_diff < 5 and lng_diff < 5

    is_dark = is_it_dark()
    status_light = "DARK" if is_dark else "LIGHT️"

    if lat_diff < 5 and lng_diff < 5:
        proximity = "Overhead       [||||]"
    elif lat_diff < 10 and lng_diff < 10:
        proximity = "Nearby         [||| ]"
    elif lat_diff < 20 and lng_diff < 20:
        proximity = "In Range       [||  ]"
    else:
        proximity = "Out of Range   [|   ]"

    print("-" * 45)
    print(f"Time (UTC):     {datetime.now(timezone.utc).strftime('%H:%M:%S')}")
    print(f"Status:         {status_light}")
    print(f"ISS Position:   Lat {iss_latitude}, Lng {iss_longitude}")
    print(f"Proximity:      {proximity}")

    if iss_close and is_dark:
        print("-" * 45)
        print("RESULT:   ISS is overhead! Mail sent... ")

        send_email()
    elif iss_close and not is_dark:
        print("-" * 45)
        print("RESULT:   The ISS is passing overhead, but the sky is too bright")

    print("=" * 45)


while True:
    try:
        track_iss()
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Scanning complete. Waiting 60s...")
        time.sleep(60)
    except requests.exceptions.RequestException as e:
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Connection error: {e}")
        print("Retrying in 60 seconds...")
        time.sleep(60)
    except KeyboardInterrupt:
        print('\nManual break by user')
        break