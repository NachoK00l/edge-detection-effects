from PIL import Image, ImageChops, ImageEnhance, ImageOps
import edgeDetection
import threadedEdgeDetection
import effects
import time

image = Image.open("image.png")

startTime = time.time()

#edge = edgeDetection.sobelEdgeDetection(image)
edge = threadedEdgeDetection.sobelEdgeDetection(image, 12)

sobelStopTime = time.time()
print(f"Sobel Edge Detection Time: {sobelStopTime - startTime}s")

edge.show()

newImage = effects.melt(image, edge, Length=15, Threshold=180)

meltStopTime = time.time()
print(f"Melt Time: {meltStopTime - sobelStopTime}s")

print(f"Total Time: {meltStopTime - startTime}s")

newImage.save('output.png')