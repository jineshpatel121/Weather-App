import tkinter as tk
from tkinter import messagebox

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
unitLabel = tk.Label(root,text = "Units: ", font =("Comfortaa", 24), width=10)
unitLabel.place(x = 30, y = 65)

# Units Box
unitBox = tk.Entry(root, width = 20)
unitBox.place(x = 200, y = 65)


# Check Weather Button
checkButton = tk.Button(root, text = "Check Weather", font = ("Impact", 18))
checkButton.place(x=120, y=115)


# Weather Result Label
weatherResult = tk.Label(root, text = "The Weather Is: ", font = ("Comfortaa", 24))
weatherResult.place(x=100, y=160)

# Weather Result Box
weatherBox = tk.Text(root, width=30, height=10, font=("Comfortaa", 14), bg="gray25", fg="gray25", relief="sunken", bd=3)
weatherBox.place(x=50, y=200)

root.mainloop()