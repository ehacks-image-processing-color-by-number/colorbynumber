import base64
from email.encoders import encode_base64
from flask import Flask, render_template, request
import random
import requests
import cv2
import numpy as np

# change port to 8080 flask run --port 8080

app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def hello_world():
    return render_template('index.html')

@app.post("/image")
def image():
    txt = '/1920x1080'
    response = requests.get("https://source.unsplash.com/random{0}".format(txt))
    # get post data 
    post_data = request.json
    data_url = post_data['image']
    prefix, base64_data = data_url.split(',')

    image_data = base64.b64decode(base64_data)
    
    with open('./image.png', 'wb') as f:
        f.write(image_data)
    return trace_image('./image.png', 'out.png', line_thickness=5)

def trace_image(input_path, output_path, line_thickness=2):
    # Load the image using OpenCV
    image = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)

    # Apply Mean (Box) Filter to reduce noise
    blurred_image = cv2.boxFilter(image, -1, (5, 5), normalize=True)  # Adjust the kernel size (third parameter) as needed

    # Perform edge detection (using Canny)
    edges = cv2.Canny(blurred_image, 30, 100)

    # Apply morphological operations to further clean up the edges
    kernel = np.ones((3, 3), np.uint8)
    edges = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

    # Convert edges to a binary image
    _, binary = cv2.threshold(edges, 128, 255, cv2.THRESH_BINARY)

    # Find contours in the binary image
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Create an empty image with a white background
    contour_image = np.ones_like(image) * 255

    # Draw contours on the image with black color and increased thickness
    cv2.drawContours(contour_image, contours, -1, 0, thickness=line_thickness)
    # convert contours to a binary image
    _, binary = cv2.threshold(contour_image, 128, 255, cv2.THRESH_BINARY)

    # Save the result
    cv2.imwrite(output_path, contour_image)
    with open(output_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    return encoded_string

    

if __name__ == "__main__":
    app.run(debug=True)
    # input_image_path = "Stewie.jpg"
    # output_contour_path = "output_contour.jpg"

    # trace_image(input_image_path, output_contour_path, line_thickness=5)

