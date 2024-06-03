from flask import Flask, request, jsonify
from flask_cors import CORS
import util

app = Flask(__name__)
CORS(app)

@app.route('/get_location_name')
def get_location_name():

    response = jsonify({
        'locations': util.get_location_name()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get_floor_name')
def get_floor_name():
    response = jsonify({
        'floors': util.get_floor_name()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_rent', methods=['POST'])
def predict_rent():
    data = request.form
    print("Received Data:", data)
    newly_constructed = int(data['newly_constructed'])
    balcony = int(data['balcony'])
    has_kitchen = int(data['has_kitchen'])
    cellar = int(data['cellar'])
    living_space = float(data['living_space'])
    lift = int(data['lift'])
    no_of_rooms = int(data['no_of_rooms'])
    garden = int(data['garden'])
    floor = data['floor']
    locations = data['location']
    estimated_rent = util.get_estimated_rent(newly_constructed, balcony, has_kitchen, cellar, living_space, lift, no_of_rooms, garden, floor, locations)
    return jsonify({'estimated_rent': estimated_rent})

if __name__ == "__main__":
    print("Starting python Flask server for Rent Prediction...")
    util.load_saved_artifactes()  # Make sure to load artifacts before running the server
    app.run()

