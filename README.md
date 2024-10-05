Weather App with SMS and GUI

This project contains a Python-based weather application that includes functionality to display weather information via a GUI and send weather updates through SMS. The project uses multiple scripts to implement different features of the application.

Project Structure:
- sms.py: Contains functionality to send weather updates via SMS. It integrates with an external API to send the messages.
- weatherApp.py: A command-line based weather application that fetches weather data from a weather API and displays it in the terminal.
- weatherAppGUI.py: Implements a graphical user interface (GUI) version of the weather app using Tkinter. It allows users to input a city name and receive weather information displayed in a GUI window.
- weatherAppSMS.py: Combines the SMS functionality with the weather application. This script allows the user to receive weather updates through SMS by sending the weather data to a provided phone number.
- weatherGUI.py: Script focuses on creating a simple GUI for displaying weather information based on user input.

Getting Started:

Prerequisites:

To run this project, you will need:
- Python 3.x
- requests library (for API calls)
- Tkinter (for GUI)
- Twilio (for sending SMS)


Running the Project:

1. Command-line Weather App:
   Run weatherApp.py to fetch and display weather information in the terminal.
   python weatherApp.py

2. GUI Weather App:
   Run weatherAppGUI.py or weatherGUI.py to use the graphical user interface version of the weather app.
   python weatherAppGUI.py

3. Weather SMS App:
   Run weatherAppSMS.py to fetch weather data and send it via SMS using Twilio.
   python weatherAppSMS.py

4. Send SMS Directly:
   Run sms.py to send an SMS containing weather information.
   python sms.py

Future Enhancements:
- Expand support for more APIs.
- Add more customization options for the GUI.

