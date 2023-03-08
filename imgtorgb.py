"""
Convert an image to it's three color components
"""

from PIL import Image


def imgToRGB(imgName):
    image = Image.open(imgName)


    image = image.convert("RGBA")

    outImgR = Image.new('RGB', image.size, color='white')
    outImgG = Image.new('RGB', image.size, color='white')
    outImgB = Image.new('RGB', image.size, color='white')

    for y in range(image.size[1]):
        for x in range(image.size[0]):
            pixel = image.getpixel((x,y))
            print(pixel)
            r, g, b, a = image.getpixel((x,y))
            pixelR  = (r, 0, 0, 255)
            pixelG = (0, g, 0, 255)
            pixelB = (0, 0, b, 255)
            outImgR.putpixel((x,y), pixelR)
            outImgG.putpixel((x,y), pixelG)
            outImgB.putpixel((x,y), pixelB)

    outImgR.save(imgName + 'R.png')
    outImgG.save(imgName + 'G.png')
    outImgB.save(imgName + 'B.png')

if __name__ == '__main__':
    imgToRGB("rect4518.png")
