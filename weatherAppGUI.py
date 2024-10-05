import requests
import tkinter as tk
from tkinter import messagebox
import smtplib
import sys
 

def weather():
    apiKey = '6f1f8ca74f48910feab6f914906402f9'
    city = cityEntry.get()
    units = unitEntry.get()

    if units.upper() == "C":
        units = "metric"
        displayUnit = "°C"
        speedUnit = "km/h"
    elif units.upper() == "F":
        units = "imperial"
        displayUnit = "°F"
        speedUnit = "mph"
    else:
        messagebox.showwarning("Input Error", "Please enter 'C' for Celsius or 'F' for Fahrenheit.")
        return

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units={units}&appid={apiKey}"

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        temp = int(data["main"]["temp"])
        condition = data["weather"][0]["description"]
        winds = data["wind"]["speed"]

        weatherResult = (
            f"Temperature: {temp} {displayUnit}\n"
            f"Condition: {condition.title()}\n"
            f"Wind Speed: {round(winds, 1)} {speedUnit}"
        )
    
    else:
        weatherResult = f"Error fetching data: {data.get('message', 'Unknown error')}"

    # Clear the Text widget before inserting new result
    weatherBox.delete('1.0', tk.END)
    weatherBox.insert(tk.END, weatherResult)

root = tk.Tk()
root.title("Weather APP")
root.geometry("400x400")
root.configure(bg="gray12")

# Enter city Labl
label = tk.Label(root,text = "Enter City", font =("Comfortaa", 24), width=10)
label.place(x = 30, y = 25)

# Enter city name box
cityEntry = tk.Entry(root, width = 20)
cityEntry.place(x = 200, y = 30)

# Units Label
unitLabel = tk.Label(root,text = "Units(F or C): ", font =("Comfortaa", 24), width=10)
unitLabel.place(x = 30, y = 65)

# Units Box
unitEntry = tk.Entry(root, width = 20)
unitEntry.place(x = 200, y = 65)


# Check Weather Button
checkButton = tk.Button(root, text = "Check Weather", font = ("Impact", 18), command = weather)
checkButton.place(x=120, y=115)


# Weather Result Label
weatherResult = tk.Label(root, text = "The Weather Is: ", font = ("Comfortaa", 24))
weatherResult.place(x=100, y=160)

# Weather Result Box
weatherBox = tk.Text(root, width=30, height=10, font=("Comfortaa", 18), bg="white", fg="black", relief="sunken", bd=3)
weatherBox.place(x=50, y=200)

root.mainloop()
