import requests

API_KEY = "your_api_key_here" # OpenWeatherMap nunchi free key tisuko
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric" # Celsius kosam
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if response.status_code == 200:
            print(f"\n--- Weather in {data['name']} ---")
            print(f"Temperature: {data['main']['temp']}°C")
            print(f"Feels like: {data['main']['feels_like']}°C")
            print(f"Weather: {data['weather'][0]['description']}")
            print(f"Humidity: {data['main']['humidity']}%")
            print(f"Wind Speed: {data['wind']['speed']} m/s")
        else:
            print(f"Error: {data['message']}")

    except Exception as e:
        print(f"Something went wrong: {e}")

if __name__ == "__main__":
    print("Welcome to Weather App!")
    while True:
        city = input("\nEnter city name or 'exit' to quit: ")
        if city.lower() == 'exit':
            break
        get_weather(city)
