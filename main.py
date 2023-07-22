import requests

api_key="YOUR API KEY"
my_phone_number_twilio = "ENTER YOUR TWILIO PHONE NUMBER "
my_real_phone = "ENTER YOUR REAL PHONEN NUMBER"

parameters={
            "lat":78.9988, #your latitude
            "lon":75.784912, #your longitude
            "appid":api_key 
            }
response=requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data=response.json()
weather_slice = wheather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

import os
from twilio.rest import Client
account_sid = 'YOUR ACCOUNT SID'
auth_token = 'YOUR AUTH TOKEN'

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today .Remember to bring an ☔ ",
        from_='my_phone_number_twilio',
        to='my_real_phone'
    )
print(message.status)
