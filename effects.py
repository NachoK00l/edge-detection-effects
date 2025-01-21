from PIL import Image
import math

def sobelEdgeDetection(image: Image.Image) -> Image.Image:
    """
    Applies the Sobel Edge Detection Algorithm to the given image. Fast but subject to noise. \n
    Returns a Greyscale ("L" Mode) image.
    """

    greyscaleImage : Image.Image
    greyscaleImage = image.convert('L')

    width, height = greyscaleImage.size

    # Used to calculate progress
    pixelCount = width * height
    pixelsDone = 0

    outputImage = Image.new('L', (width, height))
    
    # Might need to change this to be more efficient
    # O(n^2) Complexity
    for x in range(width):
        for y in range(height):
            pixelValueGrid = getPixelValueGrid(greyscaleImage, x, y, 3, 3)

            Gx = [-1, 0, 1, 
                  -2, 0, 2, 
                  -1, 0, 1]
            
            Gy = [-1, -2, -1,
                   0,  0,  0,
                   1,  2,  1]

            GxValue = 0
            GyValue = 0

            for i in range(9):
                GxValue += Gx[i] * pixelValueGrid[i]
                GyValue += Gy[i] * pixelValueGrid[i]

            value = math.sqrt(math.pow(GxValue, 2) + math.pow(GyValue, 2))

            outputImage.putpixel((x, y), int(value))

            pixelsDone += 1
            print(f"Progress: {pixelsDone}/{pixelCount} ({int(pixelsDone/pixelCount*100)}%) Pixel: ({x}, {y}) Value: {value}")

    return outputImage

def getPixelValueGrid(image: Image.Image, x: int, y: int, width: int, height: int) -> list:
    """
    Returns a list of width by height pixel values around the pixel at x, y. \n
    Width and height must be odd numbers.
    """

    imgWidth, imgHeight = image.size

    pixelValueGrid = []

    offset = int((width-1)/2)

    for pixelX in range(x-offset, x+offset+1):
        for pixelY in range(y-offset, y+offset+1):
            if pixelX < 0 or pixelX >= imgWidth or pixelY < 0 or pixelY >= imgHeight:
                pixelValueGrid.append(image.getpixel((x, y)))
            else:
                pixelValueGrid.append(image.getpixel((pixelX, pixelY)))

    return pixelValueGrid
