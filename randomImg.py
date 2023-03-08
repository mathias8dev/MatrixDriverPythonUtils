from random import random
from math import floor
from zipPixels import zipPixels
from pixelsToImg import pixelsToImg

def randomArray(size):
    return [floor(random()*255) for it in range(size)]

def randomImage(width, height):
    red = [randomArray(width) for it in range(height)]
    green = [randomArray(width) for it in range(height)]
    blue = [randomArray(width) for it in range(height)]
    
    
    pixels = zipPixels(red, green, blue)
    pixelsToImg(pixels, "randomImage.png")