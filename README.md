## Weather App with SMS, GUI, and Air Quality Heatmap

This project contains a Python-based weather application that includes functionality to display weather information via a GUI, genrate a color coded heat map of Air Quality Index and send weather updates through SMS. The project uses multiple scripts to implement different features of the application.

## Project Structure:

- sms.py: Contains functionality to send weather updates via SMS, using the Twilio API for message delivery.
- weatherApp.py: A command-line based weather application that fetches real-time weather data from the OpenWeather API and displays it in the terminal.
- weatherAppGUI.py: Implements a graphical user interface (GUI) version of the weather app using Tkinter. It allows users to input a city name and receive weather information in a GUI window.
- weatherAppSMS.py: Combines the SMS functionality with the weather application. This script allows the user to receive weather updates via SMS by sending the weather data to a provided phone number.
- weatherAppAQI.py: Allows users to choose between fetching weather data or generating an Air Quality Index (AQI) heatmap for the DFW area.
- weatherGUI.py: Focuses on creating a simple GUI for displaying weather information based on user input using Tkinter.
- AQIHeatMap.py: Generates an air quality heatmap for the DFW area, using OpenWeather API to display color-coded AQI levels.
- DFW_Cities.csv: Contains city data (latitude, longitude, and name) for generating the AQI heatmap.

## Getting Started:

### Prerequisites:
To run this project, you will need:
- Python 3.x
- requests library (for API calls)
- Tkinter (for GUI)
- Twilio (for sending SMS)
- Pandas (for processing the DFW Cities CSV)
- folium (for generating the heatmap)

### Running the Project:

1. Command-line Weather App:
   Run weatherAppAQI.py to choose to fetch and display weather information in the terminal or generate a heat map of the Air Quailty.

2. GUI Weather App:
   Run weatherAppGUI.py or weatherGUI.py to use the graphical user interface version of the weather app.
   python weatherAppGUI.py

3. Weather SMS App:
   Run weatherAppSMS.py to fetch weather data and send it via SMS using Twilio.
   python weatherAppSMS.py

4. Send SMS Directly:
   Run sms.py to send an SMS containing weather information.
   python sms.py

## Future Enhancements:
- Expand support for additional weather and air quality APIs.
- Add more customization options for the GUI.
- Improve the visualization of the heatmap with interactive features.

