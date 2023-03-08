"""
EncodingDepth: 8 bits
"""

from PIL import Image



def checksum(data):

    sum = 0
    for byte in data:
        sum += byte
    return (~sum + 1) & 0xff

def len2split(s):
    return [s[i:i+2] for i in range(0, len(s), 2)]

def buildIntHex(pixelX, pixelY, color):
    ndata = '01'
    madress = f"{(pixelY * 32 + pixelX):04x}"
    _madress = len2split(madress)
    recordType = '00'
    data = f"{color:02x}"
    
    #Conditionnal padding
    _checksum = checksum([int(ndata, 16), int(_madress[0], 16), int(_madress[1], 16), int(recordType, 16), int(data, 16)])
    if _checksum <= 15:
        _checksum = f"{_checksum:02x}"
    else:
        _checksum = f"{_checksum:x}"
    return f":{ndata}{madress}{recordType}{data}{_checksum}".upper()




def imgToHex(imgName):
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

            rstr = buildIntHex(x, y, r)
            gstr = buildIntHex(x, y, g)
            bstr = buildIntHex(x, y, b)

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
    # Mettre le chemin absolu ou relatif pointant vers le fichier
    imgToHex("test2.png")
    print("HexFiles generated")