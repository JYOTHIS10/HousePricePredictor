from flask import Flask, render_template, request
import pickle
import numpy as np
import json

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/chennai')
def chennai():
    return render_template('chennai.html')


__locations = None
__data_columns = None
model = pickle.load(open("cheenai_home_prices_model.pickle", "rb"))


def get_estimated_price(input_json):
    try:
        loc_index = __data_columns.chennai(input_json['location'].lower())
    except:
        loc_index = -1
    x = np.zeros(94)
    x[0] = input_json['sqft']
    x[1] = input_json['bath']
    x[2] = input_json['bhk']
    if loc_index == 0:
        x[loc_index] = 1
    result = round(model.predict([x])[0], 2)
    print(result)
    return result


def get_location_names():
    return __locations


def load_saved_artifacts():
    print("Loading the saved artifacts...start !")
    global __data_columns
    global __locations
    global model

    with open("columns.json") as f:
        __data_columns = json.loads(f.read())["data_columns"]
        __locations = __data_columns[3:]


@app.route("/chennai_prediction", methods=["POST"])
def chennai_prediction():
    if request.method == 'POST':
        input_json = {
            "location": request.form['sLocation'],
            "sqft": request.form['Squareft'],
            "bhk": request.form['uiBHK'],
            "bath": request.form['uiBathrooms']
        }
        result = get_estimated_price(input_json)

        if result > 10000000:
            result = round(result / 10000000, 2)
            result = str(result) + ' Crore'
        else:
            result = round(result / 100000, 2)
            result = str(result) + ' Lakhs'

    return render_template('chennai_prediction.html', result = result)


if __name__ == '__main__':
    print("Starting Python Flask Server")
    load_saved_artifacts()
    app.run(debug=True)
