from flask import Flask, render_template
import pandas as pd

app = Flask("__name__")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<station>/<data>")
def about(station, date):
    df = pd.read_csv("")
    temperature = df.station(date)
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)