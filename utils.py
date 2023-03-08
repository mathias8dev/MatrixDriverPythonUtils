from zipPixels import zipPixels
from pixelsToImg import pixelsToImg2, pixelsToImg
from pixelsCpFromHex import pixelsCpFromHex

print("Reading red ...")
redPixels = pixelsCpFromHex("redROM.hex", 32, 16, 4)
# print(redPixels)
#print("Reading Green")
greenPixels = pixelsCpFromHex("greenROM.hex", 32, 16, 4)
print("Reading Blue ...")
bluePixels = pixelsCpFromHex("blueROM.hex", 32, 16, 4)
print("Zipping pixels ...")
imgPixels = zipPixels(redPixels, greenPixels, bluePixels)
print("Generating image ...")
pixelsToImg(imgPixels)
print("Image generated")
