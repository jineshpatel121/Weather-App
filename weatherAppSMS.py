import requests
import smtplib
import sys
import time

def weather():
    apiKey = '6f1f8ca74f48910feab6f914906402f9'
    city = input("Enter your city: ")
    units = input("Do you want info in Imperial (I) or Metric (M)?: ")

    if units.upper() == "M":
        units = "metric"
        displayUnit = "°C"
        speedUnit = "km/h"
    elif units.upper() == "I":
        units = "imperial"
        displayUnit = "°F"
        speedUnit = "mph"
    else:
        print("Invalid unit type. Using standard units.")
        units = "standard"
        displayUnit = "°K"
        speedUnit = "m/s"
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units={units}&appid={apiKey}"

    response = requests.get(url)
    status = response.status_code

    if status == 200:
        data = response.json()
        temp = int(data["main"]["temp"])
        condition = data["weather"][0]["description"]
        winds = data["wind"]["speed"]

        weatherResult = (
            f"Temperature: {temp} {displayUnit}\n"
            f"Condition: {condition.title()}\n"
            f"Wind Speed: {round(winds, 1)} {speedUnit}"
        )
    else:
        weatherResult = f"Error Code: {status}: {data.get('message', 'Unable to retrieve weather data.')}"
    
    return weatherResult

CARRIERS = {
    "att": "@sms.att.net",
    "tmobile": "@tmomail.net",
    "verizon": "@vtext.com",
    "sprint": "@messaging.sprintpcs.com",
    "metro" : "@mymetropcs.com"
}

EMAIL = "codesjay2@gmail.com"
PASSWORD = "ekrd esxg fkae tanf"

def send_message(phone_number, carrier, message):
    recipient = phone_number + CARRIERS[carrier]
    auth = (EMAIL, PASSWORD)

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(auth[0], auth[1])
        
        server.sendmail(auth[0], recipient, message.encode("utf-8"))
        print(f"Message sent to {recipient} successfully.")
        
        server.quit()
    except Exception as e:
        print(f"Failed to send message: {e}")

if __name__ == "__main__":
    results = weather()
    
    # Default phone number, carrier, and message
    phone_number = "19299556322"  # Replace with your actual phone number
    carrier = "tmobile"  
    message = results

    send_message(phone_number, carrier, message)

    print(f"These results were sent: {results}")
