"""
Resize an image
"""


from PIL import Image
import time
from math import floor
from resizeimage import resizeimage

def imgResize(imgName, wSize, stretch=True):
    image = Image.open(imgName)
    nameExt = imgName.split('.')
    baseName = nameExt[0]
    ext = "jpeg"
    if len(nameExt) > 1:
        ext = nameExt[-1]
        
    
    print(f"Original size : {image.size}")

    imageResized = image.resize(wSize)
    if not stretch:
        image.thumbnail(wSize)
        imageResized = image
    savedName = f"{baseName}-{floor(time.time())}.{ext}"
    imageResized.save(savedName)
    return savedName




def imgResize2(imgName, wSize, mode="crop"):
    fd_image = open(imgName, 'rb')
    image = Image.open(fd_image)
    
    nameExt = imgName.split('.')
    baseName = nameExt[0]
    
    print(f"Original size : {image.size}\nOriginal format: {image.format}")

   
    #Resize the image to fill the specified area, crop as needed
    if mode == "cover":
        image = resizeimage.resize_cover(image, wSize)

    #Crop the image with a centered rectangle of the specified size.
    elif mode == "crop":
        image = resizeimage.resize_crop(image, wSize)
    #Resize the image so that it can fit in the specified area, keeping the ratio and without crop.
    elif mode == "contain":
        image = resizeimage.resize_contain(image, wSize, bg_color=(255, 255, 255, 0))

    #Resize image while keeping the ratio trying its best to match the specified size.
    elif mode == "thumbnail":
        image = resizeimage.resize_thumbnail(image, wSize)
    else:
        raise Exception("The mode you provide is not valid")

    savedName = f"{baseName}-{floor(time.time())}.png"
    image.save(savedName)
    fd_image.close()
    return savedName


if __name__ == '__main__':
    imgResize2("test2.png", (32, 16), mode="contain")