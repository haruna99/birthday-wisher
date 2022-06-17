import datetime as dt
import pandas as pd
import random
import smtplib

EMAIL = "haruna99.test@yahoo.com"
PASSWORD = "qasypgytpyupysaq"

now = dt.datetime.now()
month = now.month
day = now.day
birthdays = pd.read_csv("birthdays.csv")
today_birthdays = [{'name': row['name'], 'email': row['email']} for (index, row) in birthdays.iterrows()
                   if row.month == month if row.day == day]

for birthday in today_birthdays:
    letter_choice = random.randint(1, 3)
    with open(f"letter_templates/letter_{letter_choice}.txt") as file:
        letter_file = file.read()
        letter = letter_file.replace("[NAME]", birthday['name'])

    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=birthday["email"],
            msg=f"Subject: Happy Birthday\n\n{letter}"
        )



