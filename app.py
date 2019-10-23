# <--- Deps --->
from flask import Flask, render_template, request
from joblib import load
from random import randint

app = Flask(__name__)
if __name__ == '__main__':
    app.run()
@app.route('/')
def predict():
        bathrooms = request.get_json['bathrooms']
        bedrooms = request.get_json['bedrooms']
        squarefeet = request.get_json['squarefeet']
        yearbuilt = request.get_json['yearbuilt']
        inputs = [bathrooms, bedrooms, squarefeet, yearbuilt]
        pipeline = load('algorithm.sav')
        estimate = pipeline.predict([inputs])[0]
        return(flask.jsonify(j=estimate))
