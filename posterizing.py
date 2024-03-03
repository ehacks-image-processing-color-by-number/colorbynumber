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
input_image = Image.open('colorimage.png')

# Specify the number of colors for posterizing
num_colors = 8

# Apply posterizing algorithm
output_image = posterize(input_image, num_colors)

# Save the output image
output_image.save('posterized_image.png')

print("program success")