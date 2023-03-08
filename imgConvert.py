from PIL import Image

def imgConvert(imgName):
    savedName = "".join(imgName.split('.')[:-1]) + '.jpeg'
    toSaved = Image.open(imgName)
    toSaved.convert('RGB').save(savedName)



if __name__ == '__main__':
    imgConvert("image.png")
    print("Image converted to jpg")