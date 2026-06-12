##################### Normal Starting Project ######################
import os
import datetime as dt
import smtplib
import pandas as pd

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. e.g.
#name,email,year,month,day
#YourName,your_own@email.com,today_year,today_month,today_day

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Create a tuple from today's month and day using datetime. e.g.
now = dt.datetime.now()
today_month = now.month
today_day = now.day


# HINT 2: Use pandas to read the birthdays.csv
df = pd.read_csv("birthdays.csv")
# HINT 3: Use dictionary comprehension to create a dictionary from birthday.csv that is formated like this:
# birthdays_dict = {
#     (birthday_month, birthday_day): data_row
# }
birthdays_dict = {
    (row.month, row.day): row
    for (index, row) in df.iterrows()
}
today = (today_month, today_day)
#Dictionary comprehension template for pandas DataFrame looks like this:
# new_dict = {new_key: new_value for (index, data_row) in data.iterrows()}
#e.g. if the birthdays.csv looked like this:
# name,email,year,month,day
# Angela,angela@email.com,1995,12,24
#Then the birthdays_dict should look like this:
# birthdays_dict = {
#     (12, 24): Angela,angela@email.com,1995,12,24
# }

#HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:
if today in birthdays_dict:
    birthday_person = birthdays_dict[today]

    letter_num = random.randint(1, 3)

    with open(f"letter_templates/letter_{letter_num}.txt") as letter_file:
        letter_contents = letter_file.read()

    letter_contents = letter_contents.replace(
        "[NAME]",
        birthday_person["name"]
    )
    my_email = os.environ.get("MY_EMAIL")
    password = os.environ.get("MY_PASSWORD")

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(my_email, password)

        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday\n\n{letter_contents}"
        )
# 4. Send the letter generated in step 3 to that person's email address.
# HINT 1: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
# HINT 2: Remember to call .starttls()
# HINT 3: Remember to login to your email service with email/password. Make sure your security setting is set to allow less secure apps.
# HINT 4: The message should have the Subject: Happy Birthday then after \n\n The Message Body.



