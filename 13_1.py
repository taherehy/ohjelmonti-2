from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# تابعی برای دریافت یک شوخی تصادفی از API شاک نوریس
def fetch_random_joke():
    response = requests.get("https://api.chucknorris.io/jokes/random")
    if response.status_code == 200:
        joke_data = response.json()
        return joke_data.get('value', 'Failed to fetch joke')
    else:
        return 'Failed to fetch joke'

# مسیری برای دریافت یک شوخی تصادفی از شاک نوریس
@app.route("/random-joke")
def random_joke():
    joke = fetch_random_joke()
    return jsonify({"joke": joke})

if __name__ == "__main__":
    app.run(debug=True)
