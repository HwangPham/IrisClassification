from flask import Flask, json, request, jsonify
from joblib import load
from flask_cors import CORS, cross_origin

model = load('FlowerAPI/model/saved_models/model.joblib')

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/', methods = ['GET', 'POST'])
# @app.route('/')
@cross_origin()

def basic():
    if request.method == 'POST':
        # language = request.json['lang']
        data = request.get_json()
        X_test = [x for x in data.values()]
        y_pred = model.predict([X_test])
        return jsonify({'predicted_value': str(y_pred[0])})
        # return jsonify({'lang': language})
    return ''

if __name__ == '__main__':
    app.run(debug = True)