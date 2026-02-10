import random
import smtplib
import pandas
import datetime as dt
from secrets import password, my_email
now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
day_of_week = now.weekday()

df = pandas.read_csv("")

with open("quotes.txt") as file:
   lines = file.readlines()


# yahoo: smtp.mail.yahoo.com

message = random.choice(lines)

if day < 10:
    day = f"0{day}"

if month < 10:
    month = f"0{month}"
print(day, month)
if day_of_week == 0 :
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls() # makes connection secure trough Transport Layer Security (TLS)
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email, to_addrs="thomas.heideman@yahoo.com",msg=f"Subject:Monday Motivation {day} - {month} - {year}\n\n{message}")


