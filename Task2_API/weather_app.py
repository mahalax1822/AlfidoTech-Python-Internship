import requests

API_KEY = "cfe738242256fe00db6c0dba2bd67077"

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

try:
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        print("\nWeather Details")
        print("-" * 30)
        print("City:", data["name"])
        print("Temperature:", data["main"]["temp"], "°C")
        print("Feels Like:", data["main"]["feels_like"], "°C")
        print("Humidity:", data["main"]["humidity"], "%")
        print("Weather:", data["weather"][0]["description"])
        print("Wind Speed:", data["wind"]["speed"], "m/s")

    else:
        print("Error:", data["message"])

except requests.exceptions.RequestException:
    print("Network error! Please check your internet connection.")