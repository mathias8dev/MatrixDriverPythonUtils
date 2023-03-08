from PIL import Image
from imresize import imgResize


resized = imgResize("test2.jpg", (32, 16))
image = Image.open(resized)


# image = image.convert("RGB")


for y in range(image.size[1]):
    for x in range(image.size[0]):
        pixel = image.getpixel((x,y))
        print(pixel)
        # r, g, b, a = image.getpixel((x,y))