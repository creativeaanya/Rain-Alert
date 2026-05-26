import smtplib
import random as rd
import datetime as dt
import pandas

my_email = ''
password = ''

#--------DATE MATCH CHECK-------#
now = dt.datetime.now()
day = now.day
month = now.month
data = pandas.read_csv('birthdays.csv').to_dict(orient='records')

# Check if today matches a birthday in the birthdays.csv
for birth in data:
    if birth['month']==month and birth['day']==day:
        file_path = f"letter_templates/letter_{rd.randint(1,3)}.txt"
        with open(file_path,'r') as f:
            content = f.read()
        content=content.replace('[NAME]',birth['name'])
        #Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=birth['email'],
                                msg=f'Subject:Happy Birthday\n\n{content}')




