import os
import smtplib
import pandas
import random
import datetime as dt

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

now = dt.datetime.now()
week_day = now.weekday()
with open("quotes.txt", "r") as file_data:
    quotes_list = file_data.readlines()
    random_quote = random.choice(quotes_list)



with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
    if week_day == 1:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="juniorkassehinjk@gmail.com",
            msg=f"From: {my_email}\nSubject:Monday Motivation\n\n{random_quote}"
        )



