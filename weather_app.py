import requests

class WeatherApp:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather?"
        self.favourites = []

    def fetch_weather(self, city):
        url = f"{self.base_url}q={city}&appid={self.api_key}"
        response = requests.get(url)
        return response.json()

    def display_weather(self, city):
        weather_data = self.fetch_weather(city)
        if weather_data.get('cod') != 200:
            print("Error: City not found.")
            return

        temp = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        print(f"Weather in {city}:")
        print(f"Temperature: {temp}K, Description: {description}")

    def add_favourite(self, city):
        if len(self.favourites) < 3 and city not in self.favourites:
            self.favourites.append(city)
            print(f"{city} added to favourites.")
        else:
            print("Error: Can't add more than 3 cities or duplicate.")

    def list_favourites(self):
        if not self.favourites:
            print("No favourite cities.")
            return
        for city in self.favourites:
            self.display_weather(city)

    def update_favourites(self):
        print("Current favourites:", self.favourites)
        remove_city = input("Enter the name of the city to remove: ")
        if remove_city in self.favourites:
            self.favourites.remove(remove_city)
            new_city = input("Enter the name of the new city to add: ")
            self.add_favourite(new_city)
        else:
            print("City not in favourites.")

    def run(self):
        while True:
            choice = input("\n1. Check weather\n2. Add favourite city\n3. List favourite cities\n4. Update favourite cities\n5. Exit\nEnter choice: ")
            if choice == '1':
                city = input("Enter a city name: ")
                self.display_weather(city)
            elif choice == '2':
                city = input("Enter a city name to add to favourites: ")
                self.add_favourite(city)
            elif choice == '3':
                self.list_favourites()
            elif choice == '4':
                self.update_favourites()
            elif choice == '5':
                break
            else:
                print("Invalid choice.")

if __name__ == "__main__":
    API_KEY = 'api_key'  # no api key for this time, just testing :)
    app = WeatherApp(API_KEY)
    app.run()
