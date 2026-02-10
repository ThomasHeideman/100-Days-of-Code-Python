import random
import smtplib
import datetime as dt
import pandas

now = dt.datetime.now()
this_year = now.year
this_month = now.month
this_day = now.day

my_email = "xxxxxxpythonprojectxxx@gmail.com"
password = "XXXXXXXXXXXXXXXX"

df = pandas.read_csv("birthdays.csv")
today = (this_month,this_day)

birthdays = df[(df['day'] == this_day) & (df['month'] == this_month)]


with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    for index, row in birthdays.iterrows():
        birthday_name = row["name"]
        birthday_email = row["email"]
        with open(f"letter_templates/letter_{random.randint(1,3)}.txt", mode="r") as file:
            txt = file.read()
            msg = txt.replace("[NAME]",birthday_name)
            connection.sendmail(from_addr=my_email, to_addrs=birthday_email, msg= f"Subject:Happy Birthday!\n\n{msg}")


