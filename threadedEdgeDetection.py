import threading
from PIL import Image
import math

def sobelEdgeDetection(image: Image.Image, threadCount: int) -> Image.Image:
    """
    Applies the Sobel Edge Detection Algorithm to the given image. Fast but subject to noise. \n
    Returns a Greyscale ("L" Mode) image.
    """

    #1:43 for a 13,5 MPixel image with a M1 Macbook Pro with 8 threads

    greyscaleImage : Image.Image
    greyscaleImage = image.convert('L')
    width, height = greyscaleImage.size
    outputImage = Image.new('L', (width, height), 255)
    
    # Add progress tracking
    progress_lock = threading.Lock()
    total_pixels = width * height
    progress = {'processed': 0}

    print(f"Starting Sobel Edge Detection with {threadCount} threads...")
    
    threads = []
    for threadId in range(threadCount):
        threadWidth = int(width / threadCount)
        threadX = threadWidth * threadId
        thread = threading.Thread(
            target=sobelEdgeDetectionThread, 
            args=(greyscaleImage, outputImage, threadX, threadWidth, progress, progress_lock, total_pixels),
            daemon=True
        )
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return outputImage

def sobelEdgeDetectionThread(greyscaleImage: Image.Image, outputImage: Image.Image, startX: int, width: int, progress: dict, lock: threading.Lock, total_pixels: int):
    height = greyscaleImage.size[1]

    for x in range(width):
        x += startX
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
            
            with lock:
                progress['processed'] += 1
                if progress['processed'] % (total_pixels // 100) == 0:
                    percentage = (progress['processed'] / total_pixels) * 100
                    print(f"Edge Detection progress: {int(percentage)}%")


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