from PIL import Image

def flood_fill(image, sr, sc, new_color):
    """
    :type image: Image
    :type sr: int
    :type sc: int
    :type new_color: tuple
    :rtype: Image
    """
    if image.mode != 'RGBA':
        image = image.convert('RGBA')

    # Get the original color at the starting point
    original_color = image.getpixel((sr, sc))

    # Create a mask to mark pixels that have been filled
    mask = Image.new('L', (image.width, image.height), 0)
    pixels_to_fill = [(sr, sc)]

    while pixels_to_fill:
        x, y = pixels_to_fill.pop()

        # Check boundaries and pixel color
        if 0 <= x < image.width and 0 <= y < image.height and image.getpixel((x, y)) == original_color and mask.getpixel((x, y)) == 0:
            image.putpixel((x, y), new_color)
            mask.putpixel((x, y), 255)

            # Add neighboring pixels to the stack for processing
            pixels_to_fill.extend([(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)])

    return image

# Example usage:
if 1 == 1:
    # Open the PNG image
    input_image = Image.open("grid.png")

    # Starting position and new color
    sr, sc = 50, 50
    new_color = (255, 0, 0, 255)  # Red color with full opacity

    # Perform flood fill
    filled_image = flood_fill(input_image, sr, sc, new_color)

    # Save the filled image
    filled_image.save("gridfill.png")

    # Show the filled image
    filled_image.show()