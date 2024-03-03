from PIL import Image

def posterize(image, num_colors):
    """
    Posterize the given image to the specified number of colors.
    """
    # Convert the image to RGB mode
    image = image.convert('RGB')

    # Apply posterize effect
    image = image.quantize(colors=num_colors)

    return image

# Open an image file
input_image = Image.open('fruit.png')

# Specify the number of colors for posterizing
num_colors = 10

# Apply posterizing algorithm
output_image = posterize(input_image, num_colors)

# Save the output image
output_image.save('posterized_image.png')
width, height = output_image.size
pixels = output_image.load()

# Iterate through each pixel to get RGB values
for y in range(height):
    for x in range(width):
        r, g, b = output_image.getpixel((x, y))
        print(f"Pixel at ({x}, {y}): R={r}, G={g}, B={b}")

print("program success")