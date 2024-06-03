
# Model to import for util file.
# json-to extract the columns form json column file
#pickel to extract from pickle file
#and np


import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None
__floor = None
#cration of get estimated rent function.
def get_estimated_rent(newlyConst, balcony, hasKitchen, cellar, livingSpace, lift, noRooms, garden, floor, location):
    # location and floor values are found using indexing.
    location = location.lower()
    floor = floor.lower()

    try:
        loc_index = __data_columns.index(location)
    except ValueError:
        loc_index = -1

    try:
        floor_index = __data_columns.index(floor)
    except ValueError:
        floor_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = newlyConst
    x[1] = balcony
    x[2] = hasKitchen
    x[3] = cellar
    x[4] = livingSpace
    x[5] = lift
    x[6] = noRooms
    x[7] = garden

    if floor_index >= 0:
        x[floor_index] = 1
    if loc_index >= 0:
        x[loc_index] = 1

    prediction = __model.predict([x])[0]
    return round(float(np.exp(prediction)), 0)
# getting variable from pickle and json file
def load_saved_artifactes():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations
    global __model
    global __floor

    with open("./artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[17:]
        __floor = __data_columns[8:17]

    with open("./artifacts/berlin_price_model.pickle", 'rb') as f:
        __model = pickle.load(f)
    print("loading saved artifacts...done")
#creting funtion for location and floor columns
def get_location_name():
    return __locations

def get_floor_name():
    return __floor

if __name__ == '__main__':
    load_saved_artifactes()
    print(get_location_name())
    print(get_floor_name())
    print(get_estimated_rent(0, 0, 1, 1, 31, 1, 1, 0, 'apartment', 'Zehlendorf, Zehlendorf'))
