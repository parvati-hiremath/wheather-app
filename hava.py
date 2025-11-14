import requests

API_key = "05096f46373cd41c68d2ad49c22d4908"
URL = "https://api.openweathermap.org/data/2.5/weather"

def main():
    city = input("Enter city: ").strip()
    if not city:
        print("Error:City name cannot be empty.")
        return

    try:
        params = {"q":city,"appid":API_key, "units":"metric"}
        resp = requests.get(URL, params = params)
        resp.raise_for_status() #throws 404/500
        data = resp.json() 
        print(f"{city} temperature: {data['main']['temp']} °c")

    except requests.exceptions.HTTPError as h:
        print("API error:{h}")

    except KeyError:
        print("Error: Expected data from API not received.")

    except Exception as e:
        print(f"Unknown error:{e}")

if __name__  == "__main__":
    main()