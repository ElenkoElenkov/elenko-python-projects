from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)


def get_db():
    conn = sqlite3.connect("cafes.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def home():
    db = get_db()
    cafes = db.execute("SELECT * FROM cafe").fetchall()
    return render_template("index.html", cafes=cafes)


@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    if request.method == "POST":
        name = request.form["name"]
        location = request.form["location"]
        wifi = request.form["wifi"]
        power = request.form["power"]
        map_url = request.form["map_url"]
        img_url = request.form["img_url"]
        seats = request.form["seats"]
        coffee_price = request.form["coffee_price"]

        db = get_db()
        db.execute("""
        INSERT INTO cafe
        (name, map_url, img_url, location, seats,
         has_toilet, has_wifi, has_sockets, can_take_calls, coffee_price)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            name, map_url, img_url, location, seats,
            "Yes", wifi, power, "Yes", coffee_price
        ))
        db.commit()
        return redirect("/")

    return render_template("add.html")


@app.route("/delete/<int:cafe_id>")
def delete_cafe(cafe_id):
    db = get_db()
    db.execute("DELETE FROM cafe WHERE id = ?", (cafe_id,))
    db.commit()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)