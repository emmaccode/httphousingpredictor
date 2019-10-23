import flask
import json
from flask import Flask, render_template, request
from joblib import load

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
        bathrooms = int(bathrooms)
        bedrooms = int(bedrooms)
        squarefeet = int(squarefeet)
        yearbuilt = int(yearbuilt)
    except ValueError as e:
        return ('That aint a number, Cowboy.')
    else:
        dta = [bathrooms, bedrooms, squarefeet, yearbuilt]
        pipeline = load('algorithm.sav')
        estimate = pipeline.predict([dta])[0]
        return str(int(estimate))

if __name__ == '__main__':
    app.run(debug=False)
