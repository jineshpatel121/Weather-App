import requests
import pandas as pd
import folium
from folium.plugins import HeatMap

def get_AQI():
    
    # Set your OpenWeather API key here
    apiKey = ' '

    # Read the CSV file (assuming it's named 'dfw_cities.csv')
    data = pd.read_csv('/Users/jineshpatel/Documents/Projects/Python/Weather/DFW_Cities.csv')  # Update this with the correct path

    # Convert the DataFrame into a list of dictionaries for the locations list
    locations = data.to_dict('records')

    # AQI to color mapping (Green to Red scale)
    def getAQI_Color(aqi):
        # Good
        if aqi == 1:
            return 'green'
        # Fair
        elif aqi == 2:
            return 'yellow' 
        # Moderate
        elif aqi == 3:
            return 'orange'
        # Poor   
        elif aqi == 4:
            return 'red'
        # Very Poor      
        elif aqi == 5:
            return 'purple' 
        # Unknown
        else:
            return 'gray'  

    # Fetch air quality data for each location
    def getAQ(lat, lon):
        url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={apiKey}"
        response = requests.get(url)
        data = response.json()
        return data['list'][0]['main']['aqi']  # Air Quality Index (1-5 scale)

    # Create a map centered around DFW
    dfw_map = folium.Map(location=[32.7767, -96.7970], zoom_start=9)

    # Get air quality data for all locations
    for location in locations:
        aqi = getAQ(location['lat'], location['lon'])
        color = getAQI_Color(aqi)

        # Add circle markers to the map with AQI color
        folium.CircleMarker(
            location=[location['lat'], location['lon']],
            radius=15,
            color=color,
            fill=True,
            fill_color=color,
            fill_opacity=0.2,
            popup=f"{location['name']} - AQI: {aqi}"
        ).add_to(dfw_map)

    # Add legend (color-coded for AQI)
    legend_html = """
    <div style="position: fixed;
        bottom: 50px; left: 50px; width: 150px; height: 120px;
        background-color: white; border:2px solid grey; z-index:9999;
        font-size:14px;">
        &nbsp; <b>AQI Scale</b> <br>
        &nbsp; <i style="background:green;color:white;padding:3px;">Good (1)</i><br>
        &nbsp; <i style="background:yellow;color:black;padding:3px;">Fair (2)</i><br>
        &nbsp; <i style="background:orange;color:black;padding:3px;">Moderate (3)</i><br>
        &nbsp; <i style="background:red;color:white;padding:3px;">Poor (4)</i><br>
        &nbsp; <i style="background:purple;color:white;padding:3px;">Very Poor (5)</i><br>
    </div>
    """

    dfw_map.get_root().html.add_child(folium.Element(legend_html))

    # Save map as HTML file
    dfw_map.save("DFW_AirQuality_Heatmap.html")

    print("DFW Air Quality Index Heatmap has been generated and saved as DFW_AirQuality_Heatmap.html.")
