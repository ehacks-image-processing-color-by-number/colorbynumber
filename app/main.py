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
    file = open('image.jpg', 'wb')
    file.write(response.content)
    file.close()
    img = Image.open('image.jpg')
    img.show()


if __name__ == "__main__":
    app.run(debug=True)

