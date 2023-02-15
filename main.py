#Alex Gonzalez
import requests
import json

# Function to get weather information from OpenWeatherMap API based on zip code or city name
def get_weather_info(zip_code_or_city):
    # API key for OpenWeatherMap
    API_KEY = "646b2a69458c87a50e7af13a0e660764"

    # API endpoint for getting weather information
    API_ENDPOINT = f"http://api.openweathermap.org/data/2.5/weather?appid={API_KEY}&"

    # Check if the user entered a zip code or a city name
    if zip_code_or_city.isdigit():
        # User entered a zip code
        API_ENDPOINT += f"zip={zip_code_or_city},us"
    else:
        # User entered a city name
        API_ENDPOINT += f"q={zip_code_or_city}"

    # Try to get the weather information from the API
    try:
        response = requests.get(API_ENDPOINT)

        # Check if the API request was successful
        if response.status_code == 200:
            # Parse the JSON data from the API response
            weather_data = json.loads(response.text)

            # Extract the necessary information from the weather data
            city = weather_data["name"]
            temperature = weather_data["main"]["temp"] - 273.15
            humidity = weather_data["main"]["humidity"]
            weather_description = weather_data["weather"][0]["description"]

            # Return the weather information in a readable format
            return f"City: {city}\nTemperature: {temperature:.1f}°C\nHumidity: {humidity}%\nWeather: {weather_description}"
        else:
            # Return an error message if the API request was not successful
            return "An error occurred while getting weather information."
    except:
        # Return an error message if a connection to the API could not be established
        return "Could not establish a connection to the weather service."

# Main function
def main():
    while True:
        # Ask the user for their zip code or city
        zip_code_or_city = input("Enter your zip code or city name: ")

        # Get the weather information
        weather_info = get_weather_info(zip_code_or_city)

        # Print the weather information
        print(weather_info)
        print()

# Run the main function
if __name__ == "__main__":
    main()
