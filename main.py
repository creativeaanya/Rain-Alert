import requests
import smtplib
import os

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

parameters = {
    "lat": 30.2672, #33.3075,
    "lon": 97.7431, #-111.8449,
    "appid": "f2d69fab5eda3fa56be94debfc5188f9",
    "cnt": 4,
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters) 
response.raise_for_status() 
data = response.json()

# My Code:
weather_id = [item["weather"][0]["id"] for item in data["list"]]
for item in weather_id:
    if item < 700:
        email_response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
        email_response.raise_for_status()
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs="aanyatester@yahoo.com", msg="Subject: Rain alert!\n\nMake sure to bring an umbrella ☔.")
        break
        
# Alternate Code:
    # will_rain = False
    # for hour_data in data["list"]:
    #     condition_code = hour_data["weather"][0]["id"]
    #     if int(condition_code) < 700:
    #         will_rain = True
    #         
    # if will_rain:
    #    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#             connection.starttls()
#             connection.login(user=MY_EMAIL, password=MY_PASSWORD)
#             connection.sendmail(from_addr=MY_EMAIL, to_addrs="aanyatester@yahoo.com", msg="Subject: Rain alert!\n\nMake sure to bring an umbrella ☔.")
