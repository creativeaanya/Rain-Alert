##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas
import random
import smtplib

from_mail = "akshay.gaonkar07@gmail.com"
password = "wiyubqxotxxqtfbh"

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

now = dt.datetime.now()
month = now.month
day = now.day

data = pandas.read_csv("birthdays.csv")
data_dict = data.to_dict("records")
print(data_dict)

for data_object in data_dict:
    if data_object["month"] == now.month and data_object["day"] == now.day:
        random_letter_index = random.randint(1, 3)
        with open(f"letter_templates/letter_{random_letter_index}.txt", "r") as file:
            content = file.read()
        updated_content = content.replace("[NAME]", data_object["name"])
        print(updated_content)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=from_mail, password=password)
            to_mail = f"{data_object["email"]}"
            connection.sendmail(from_mail, to_mail, f"Subject: Happy Birthday Wish\n\n{updated_content}")
