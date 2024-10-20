import requests
def get_weather():

    apiKey = '6f1f8ca74f48910feab6f914906402f9'

    city = input("Enter your city: ")

    units = input("Do you want info in Imperial(I) or Metric(M): ")

    if (units.upper() == "M"):
        units = "metric"
        displayUnit = " C Degrees"
        speedUnit = " km/s"
    elif (units.upper() == "I"):
        units = "imperial"
        displayUnit = " F Degrees"
        speedUnit = " mph"
    else:
        units = "standard"
        displayUnit = " K Degrees"
        speedUnit = "m/s"


    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units={units}&appid={apiKey}"

    # Access the url
    response = requests.get(url)

    # Get server code 
    status = response.status_code


    if (status == 200):
        data = response.json() # This gets the actual data(temp,time,etc..)
        temp = int(data["main"]["temp"])
        condition = data["weather"][0]["description"]
        winds = data["wind"]["speed"]

        print(f"Tempture: {temp} {displayUnit}")
        print(f"It Is: {(condition.upper())}")
        print(f"It is {round(winds,1)} {speedUnit}")
    else:
        print(f"Error Code: {status}")
