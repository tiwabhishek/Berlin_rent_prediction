## Server file that lets flash server run on .py file.
# Import important libraries
from flask import Flask, request, jsonify
from flask_cors import CORS
import util
#  Flask application inctence.
app = Flask(__name__)
# Enabling CORS(Cross origin resource sharing)
CORS(app)
Defining a route to get location names
@app.route('/get_location_name')
def get_location_name():
    # Creating a JSON response with location names obtained from util module
    response = jsonify({
        'locations': util.get_location_name()
    })
    # Add header to allow cross-origin requests
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
#Defining a route to get floor names same as location
@app.route('/get_floor_name')
def get_floor_name():
    response = jsonify({
        'floors': util.get_floor_name()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
# Defining a route to predict rent, allowing only POST method
@app.route('/predict_rent', methods=['POST'])
def predict_rent():
    # Info form data from the POST request
    data = request.form
    print("Received Data:", data)
    # Data that needs to be chnaged.
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
     # estimated rent from util module using extracted fields
    estimated_rent = util.get_estimated_rent(newly_constructed, balcony, has_kitchen, cellar, living_space, lift, no_of_rooms, garden, floor, locations)
    return jsonify({'estimated_rent': estimated_rent})
# Entry point for running the Flask application
if __name__ == "__main__":
    print("Starting python Flask server for Rent Prediction...")
    #loading artificats from util file
    util.load_saved_artifactes()  
    app.run()

