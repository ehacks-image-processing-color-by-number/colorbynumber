import base64
from flask import Flask, render_template
import random
import requests



app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def hello_world():
    return render_template('index.html')

@app.route("/upload")
def uploadImage():
    return render_template('upload.html')

@app.route("/randomizedImage")
def randomizedImage():
    return render_template('randomizedImage.html')

@app.post("/image")
def image():
    txt = '/1920x1080'
    response = requests.get("https://source.unsplash.com/random{0}".format(txt))
    return base64.b64encode(response.content)


if __name__ == "__main__":
    app.run(debug=True)

