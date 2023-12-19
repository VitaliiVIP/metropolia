import requests
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def get_weather(api_key, city_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    if response.status_code == 200:
        weather_description = data["weather"][0]["description"]
        temperature_kelvin = data["main"]["temp"]
        temperature_celsius = kelvin_to_celsius(temperature_kelvin)
        print(f"Weather in {city_name}: {weather_description}")
        print(f"Temperature: {temperature_celsius:.2f} °C")
    else:
        print(f"Failed to get weather data. Status Code: {response.status_code}")
        print(data)
if __name__ == "__main__":
    api_key = "476126fe02b3a9c9f20f80827f7ede38"
    city_name = input("Enter the name of the municipality: ")
    get_weather(api_key, city_name)
