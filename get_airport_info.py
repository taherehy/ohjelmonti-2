import requests

# Määritä palvelimen osoite
base_url = 'http://127.0.0.1:5000'

# Määritä ICAO-koodi
ICAO_code = 'EFHK'

# Tee GET-pyyntö palvelimelle
response = requests.get(f'{base_url}/kenttä/{ICAO_code}')

# Tarkista vastauksen tila
if response.status_code == 200:
    # Tulosta vastauksen sisältö
    print(response.json())
else:
    print('Virhe:', response.status_code)
