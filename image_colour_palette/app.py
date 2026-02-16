from flask import Flask, render_template, request
from PIL import Image
import numpy as np
from collections import Counter
import os

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(*rgb)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        file = request.files["image"]

        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)

        image = Image.open(filepath)
        image = image.resize((200, 200))  # speed up processing

        pixels = np.array(image).reshape(-1, 3)

        most_common = Counter(map(tuple, pixels)).most_common(10)

        hex_colors = [rgb_to_hex(color) for color, count in most_common]

        return render_template("result.html",
                               image=filepath,
                               colors=hex_colors)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)