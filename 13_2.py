from flask import Flask, jsonify

app = Flask(__name__)

# Simuloitu lentokenttätietokanta
airport_database = {
    "EFHK": {"Name": "Helsinki Vantaa Airport", "Municipality": "Helsinki"},
    # Lisää tarvittaessa muita lentokenttiä
}

# GET-pyyntö kenttä/:ICAO
@app.route('/kenttä/<ICAO>')
def get_airport_info(ICAO):
    airport = airport_database.get(ICAO)
    if airport:
        return jsonify({"ICAO": ICAO, "Name": airport["Name"], "Municipality": airport["Municipality"]})
    else:
        return jsonify({"error": "Lentokenttää ei löytynyt"}), 404

if __name__ == '__main__':
    app.run(debug=True)
