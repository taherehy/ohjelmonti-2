import requests

def get_random_chuck_norris_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)
    data = response.json()
    joke = data['value']
    return joke

def main():
    joke = get_random_chuck_norris_joke()
    print(joke)

if __name__ == "__main__":
    main()
