from flask import Flask, request, jsonify
import util

app = Flask(__name__)

# Routine that return all the locations from json file
@app.route('/get_location_names')
def get_location_names():
    
    response = jsonify({
        'locations' : util.get_location_names()
    })
    
    response.headers.add('Access-Control-Allow-Orgin', '*')
    
    return response
    return 'Hi'

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction")
    app.run()     
