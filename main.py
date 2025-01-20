from PIL import Image, ImageChops, ImageEnhance, ImageOps
import edgeDetection
import effects

image = Image.open("image.png")

edge = edgeDetection.sobelEdgeDetection(image)

edge.show()

newImage = effects.melt(image, edge, Length=30)
newImage.show()
newImage.save('output.png')