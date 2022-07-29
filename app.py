from flask import Flask, render_template, request
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import numpy as np

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        data = pd.read_csv("./data/predict_data.csv")
        x = data.iloc[:, :1]
        y = data.iloc[:, -1:]
        regressor = RandomForestRegressor(n_estimators=100, random_state=2)
        regressor.fit(x, y.values.ravel())
        square_footage = request.form["sqft"]
        pred = regressor.predict(np.array([square_footage]).reshape(1, 1))
        prediction = pred[0] * 100
        return render_template("result.html", prediction=prediction)
    else:
        return render_template("index.html")


@app.route("/result")
def result():
    return render_template("result.html")


@app.route("/graphs")
def graphs():
    return render_template("graphs.html")


if __name__ == "__app__":
    app.run()
