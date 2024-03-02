import cv2
import numpy as np

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

    # Save the result
    cv2.imwrite(output_path, contour_image)
    

if __name__ == "__main__":
    input_image_path = "Stewie.jpg"
    output_contour_path = "output_contour.jpg"

    trace_image(input_image_path, output_contour_path, line_thickness=5)