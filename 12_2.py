import requests

def main():
    # Kysytään käyttäjältä paikkakunnan nimi
    city = input("Syötä paikkakunnan nimi: ")

    api_key = "369593b839dba7c012839ac4e1b6731b"

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    # Lähetetään API-pyyntö
    response = requests.get(url)

    # Tarkistetaan, onko vastaus onnistunut (status code 200)
    if response.status_code == 200:
        data = response.json()

        # Haetaan lämpötila kelvin-asteina
        temperature_kelvin = data['main']['temp']

        # Muunnetaan lämpötila Celsius-asteiksi
        temperature_celsius = temperature_kelvin - 273.15

        # Haetaan säätilan kuvaus
        weather_description = data['weather'][0]['description']

        # Tulostetaan säätila ja lämpötila
        print(f"Sää paikkakunnalla {city}: {weather_description}")
        print(f"Lämpötila: {temperature_celsius:.2f}°C")
    else:
        print("Virhe: Paikkakuntaa ei löytynyt tai jotain meni pieleen.")

if __name__ == "__main__":
    main()
