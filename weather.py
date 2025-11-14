import requests

API_key = "05096f46373cd41c68d2ad49c22d4908"
URL = "https://api.openweathermap.org/data/2.5/weather"

def main():
    city = input("Enter city: ")
    params = {"q":city, "appid":API_key, "units":"metric"}
    resp = requests.get(URL, params = params)
    data = resp.json()
    print(f"{city} temperature:{data['main']['temp']} °c")

if __name__ == "__main__":
    main()