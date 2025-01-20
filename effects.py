from PIL import Image
import math

def melt(image: Image.Image, edge: Image.Image, Threshold : int = 128, Length: int = 10) -> Image.Image:
    """
    Melts the image.\n
    Image is the original image.\n
    Edge is the output of an edge detection algorithm.\n
    Threshold is how bright the edge needs to be to be considered an edge (Max 255).\n
    Length is how long the melt should be (px).
    """
    width, height = image.size

    newImage = image.copy()

    # Used as a counter to determine when to stop melting
    count = 0

    prevPixel = None

    for x in range(width):
        for y in range(height):
            if edge.getpixel((x, y)) > Threshold:
                count = Length
                prevPixel = newImage.getpixel((x, y))
            else:
                if count > 0:
                    newImage.putpixel((x, y), prevPixel)
                    count -= 1
                else:
                    continue
        
        count = 0
        prevPixel = None

    return newImage

def hmelt(image: Image.Image, edge: Image.Image, Threshold : int = 128, Length: int = 10) -> Image.Image:
    """
    Melts the image but horizontally.\n
    Image is the original image.\n
    Edge is the output of an edge detection algorithm.\n
    Threshold is how bright the edge needs to be to be considered an edge (Max 255).\n
    Length is how long the melt should be (px).
    """
    width, height = image.size

    newImage = image.copy()

    # Used as a counter to determine when to stop melting
    count = 0

    prevPixel = None

    for y in range(height):
        for x in range(width):
            if edge.getpixel((x, y)) > Threshold:
                count = Length
                prevPixel = newImage.getpixel((x, y))
            else:
                if count > 0:
                    newImage.putpixel((x, y), prevPixel)
                    count -= 1
                else:
                    continue
        
        count = 0
        prevPixel = None

    return newImage