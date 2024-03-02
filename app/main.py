import base64
from django.http import JsonResponse
from flask import Flask, render_template
import random
import requests
from PIL import Image
import io



app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def hello_world():
    return render_template('index.html')

@app.post("/image")
def image():
    txt = '/1920x1080'
    response = requests.get("https://source.unsplash.com/random{0}".format(txt))
    return base64.b64encode(response.content)


if __name__ == "__main__":
    app.run(debug=True)

