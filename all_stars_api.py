from flask import Flask ,jsonify
from data import star_data

app = Flask(__name__)

@app.route("/")

def index():
    return jsonify({
        "data" : star_data,
        "message" : "success"
    }),200

if __name__ == "__main__":
    app.run(debug=True)