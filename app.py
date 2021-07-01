from flask import Flask, request, render_template
import pickle
import numpy as np
import json

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


def kochi():
    @app.route('/Kochi')
    def Kochi():
        return render_template('Kochi.html')

    __locations = None
    __data_columns = None
    model = pickle.load(open("Kochi_home_prices_model.pickle", "rb"))

    def get_estimated_price(input_json):
        try:
            loc_index = __data_columns.Kochi(input_json['location'].lower())
        except:
            loc_index = -1

        x = np.zeros(3)
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

    @app.route("/Kochi_prediction", methods=["POST"])
    def Kochi_prediction():
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

        return render_template('Kochi_prediction.html', result=result)


def chennai():
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
        x = np.zeros(85)
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

        return render_template('chennai_prediction.html', result=result)


def bangalore():
    @app.route('/bangalore')
    def bangalore():
        return render_template('bangalore.html')

    __locations = None
    __data_columns = None
    model = pickle.load(open("bangalore_home_prices_model.pickle", "rb"))

    def get_estimated_price(input_json):
        try:
            loc_index = __data_columns.bangalore(input_json['location'].lower())
        except:
            loc_index = -1
        x = np.zeros(146)
        x[0] = input_json['sqft']
        x[1] = input_json['bhk']
        x[2] = input_json['bath']
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

    @app.route("/bangalore_prediction", methods=["POST"])
    def bangalore_prediction():
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

        return render_template('bangalore_prediction.html', result=result)


def mumbai():
    @app.route('/mumbai')
    def mumbai():
        return render_template('mumbai.html')

    __locations = None
    __data_columns = None
    model = pickle.load(open("mumbai_home_prices_model.pickle", "rb"))

    def get_estimated_price(input_json):
        try:
            loc_index = __data_columns.mumbai(input_json['location'].lower())
        except:
            loc_index = -1
        x = np.zeros(48)
        x[0] = input_json['sqft']
        x[1] = input_json['bhk']
        x[2] = input_json['bath']
        if loc_index == 0:
            x[loc_index] = 1
        result = round(model.predict([x])[0], 2)
        # result = result * -1
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

    @app.route("/mumbai_prediction", methods=["POST"])
    def mumbai_prediction():
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

        return render_template('mumbai_prediction.html', result=result)


def delhi():
    @app.route('/delhi')
    def delhi():
        return render_template('delhi.html')

    __locations = None
    __data_columns = None
    model = pickle.load(open("delhi_home_prices_model.pickle", "rb"))

    def get_estimated_price(input_json):
        try:
            loc_index = __data_columns.delhi(input_json['location'].lower())
        except:
            loc_index = -1
        x = np.zeros(83)
        x[0] = input_json['sqft']
        x[1] = input_json['bath']
        x[2] = input_json['bhk']
        if loc_index == 0:
            x[loc_index] = 1
        result = round(model.predict([x])[0], 2)
        result = result * -1
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

    @app.route("/delhi_prediction", methods=["POST"])
    def delhi_prediction():
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

        return render_template('delhi_prediction.html', result=result)


def kolkata():
    @app.route('/Kolkata')
    def Kolkata():
        return render_template('Kolkata.html')

    __locations = None
    __data_columns = None
    model = pickle.load(open("kolkata_home_prices_model.pickle", "rb"))

    def get_estimated_price(input_json):
        try:
            loc_index = __data_columns.Kolkata(input_json['location'].lower())
        except:
            loc_index = -1
        x = np.zeros(100)
        x[0] = input_json['sqft']
        x[1] = input_json['bath']
        x[2] = input_json['bhk']
        if loc_index == 0:
            x[loc_index] = 1
        result = round(model.predict([x])[0], 2)
        result = result * 2
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

    @app.route("/Kolkata_prediction", methods=["POST"])
    def Kolkata_prediction():
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

        return render_template('Kolkata_prediction.html', result=result)


kochi()
chennai()
bangalore()
mumbai()
delhi()
kolkata()

if __name__ == '__main__':
    print("Starting Python Flask Server")
    app.run(debug=True)
