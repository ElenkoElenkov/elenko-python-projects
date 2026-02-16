from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        city = request.form.get("city")

        url = "https://api.openbrewerydb.org/v1/breweries"
        params = {"by_city": city}

        response = requests.get(url, params=params)

        if response.status_code == 200:
            breweries = response.json()
            return render_template("results.html", breweries=breweries, city=city)
        else:
            return f"API error: {response.status_code}"

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)