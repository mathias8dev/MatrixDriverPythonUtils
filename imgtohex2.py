"""
Version pour une profondeur d'encodage de 1 bit.
"""

from PIL import Image
from checksum import checksum
from len2split import len2split





def buildIntHex2(pixelX, pixelY, color):
    ndata = '01'
    madress = f"{(pixelY * 32 + pixelX):04x}"
    _madress = len2split(madress)
    
    recordType = '00'
    data = '00'
    if (color) > 0:
        data = '01'
    
    _checksum = checksum([int(ndata, 16), int(_madress[0], 16), int(_madress[1], 16), int(recordType, 16), int(data, 16)])
    if _checksum <= 15:
        _checksum = f"{_checksum:02x}"
    else:
        _checksum = f"{_checksum:x}"
    
    return f":{ndata}{madress}{recordType}{data}{_checksum}".upper()




def imgToHex2(imgName):
    image = Image.open(imgName)


    image = image.convert("RGBA")

    outFileR = open('redROM.hex', 'w')
    outFileG = open('greenROM.hex', 'w')
    outFileB = open('blueROM.hex', 'w')

    for y in range(image.size[1]):
        for x in range(image.size[0]):
            #pixel = image.getpixel((x,y))
            #print(pixel)
            r, g, b, a = image.getpixel((x,y))
            print(f"({r}, {g}, {b})")

            rstr = buildIntHex2(x, y, r)
            gstr = buildIntHex2(x, y, g)
            bstr = buildIntHex2(x, y, b)

            outFileR.write(f"{rstr}\n")
            outFileG.write(f"{gstr}\n")
            outFileB.write(f"{bstr}\n")

    outFileR.write(":00000001FF\n")
    outFileG.write(":00000001FF\n")
    outFileB.write(":00000001FF\n")

    outFileR.close()
    outFileB.close()
    outFileG.close()

if __name__ == '__main__':
    imgToHex2("test2-1678190021.png")