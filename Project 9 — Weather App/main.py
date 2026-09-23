import requests

city = input("Enter city name: ")

url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"

response = requests.get(url)
data = response.json()

if "results" in data:
    latitude = data["results"][0]["latitude"]
    longitude = data["results"][0]["longitude"]
    city_name = data["results"][0]["name"]

    weather_url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={latitude}&longitude={longitude}"
        f"&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
    )

    weather_response = requests.get(weather_url)
    weather = weather_response.json()

    current = weather["current"]

    print("\n🌤️ Weather Information")
    print("----------------------")
    print("City:", city_name)
    print("Temperature:", current["temperature_2m"], "°C")
    print("Humidity:", current["relative_humidity_2m"], "%")
    print("Wind Speed:", current["wind_speed_10m"], "km/h")

else:
    print("❌ City not found.")