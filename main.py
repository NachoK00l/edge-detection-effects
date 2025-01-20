from PIL import Image, ImageChops, ImageEnhance, ImageOps
import edgeDetection
import effects

image = Image.open("C:/Users/Ohioman/Pictures/image.png")

edge = edgeDetection.sobelEdgeDetection(image)

edge.show()

melt = effects.melt(image, edge, Length=30)
newImage = effects.hmelt(melt, edge, Length=30)
newImage.show()
newImage.save('output.png')