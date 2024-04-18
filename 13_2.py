from flask import Flask, jsonify

app = Flask(__name__)
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='ihmiset',
         user="root",
         password="tt1000",
         autocommit=True
         )


@app.route('/kenttä/<ICAO>')
def get_airport_info(ICAO):
    airport = airport_database.get(ICAO)
    if airport:
        return jsonify({"ICAO": ICAO, "Name": airport["Name"], "Municipality": airport["Municipality"]})
    else:
        return jsonify({"error": "Lentokenttää ei löytynyt"}), 404

if __name__ == '__main__':
    app.run(debug=True)
