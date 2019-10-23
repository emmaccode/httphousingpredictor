import flask
import json
from flask import Flask, render_template, request
from joblib import load
import pandas as pd
# <--- Deps --->
# (Main)
app = Flask(__name__)
if __name__ == '__main__':
    app.run()

@app.route('/')
def template():
    try:
        bathrooms = request.args['bathrooms']
        bedrooms = request.args['bedrooms']
        squarefeet = request.args['squarefeet']
        yearbuilt = request.args['yearbuilt']
    except KeyError as e:
        return ('Some Values are missing')
    try:
        bathrooms = float(bathrooms)
        bedrooms = float(bedrooms)
        squarefeet = float(squarefeet)
        yearbuilt = int(yearbuilt)
    except ValueError as e:
        return ('That aint a number, Cowboy.')
    else:
        dcry = pd.DataFrame({"YearBuilt": [yearbuilt],
        "LotSize": [squarefeet],"Bedrooms": [bedrooms],
        "Bathrooms": [bathrooms]})
        pipeline = load('alg.sav')
        estimate = pipeline.predict(dcry)
        return str(int(estimate))

if __name__ == '__main__':
    app.run(debug=False)
