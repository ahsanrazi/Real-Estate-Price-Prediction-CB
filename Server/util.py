import json
import pickle
import numpy as np

# Global Variables
__locations = None
__data_columns = None
__model = None

def get_estimated_price(location, sqft, bath, bhk):
    
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index>=0:
        x[loc_index] = 1

    return round(__model.predict([x])[0],2)


def get_location_names():
    return __locations


# Load the saved artifacts
def load_saved_artifacts():
    print('Loading saved artifacts...Start')
    global __data_columns
    global __locations
    global __model
    
    with open("C:\\Ahsan\\AI\\Real-Estate-Price-Prediction-CB\\Server\\artifacts\\columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]
        
    with open("C:\\Ahsan\\AI\\Real-Estate-Price-Prediction-CB\\Server\\artifacts\\banglore_home_price_model.pickle", "rb") as f:
        __model = pickle.load(f)
        
    print("Loading Artifacts is Done...")
    
if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar',1000, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2)) # other location
    print(get_estimated_price('Ejipura', 1000, 2, 2))  # other location