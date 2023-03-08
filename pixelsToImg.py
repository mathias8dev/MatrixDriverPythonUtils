from PIL import Image
import numpy as np


def pixelsToImg(pixels, outputName="createdImg.png"):
    npArray = np.array(pixels, dtype=np.uint8)
    createdImage = Image.fromarray(npArray)
    createdImage.save(outputName)
    return outputName

def pixelsToImg2(pixels, outputName="createdImg2.png"):
    npArray = (np.array(pixels) * 255).astype('uint8')
    createdImage = Image.fromarray(npArray)
    createdImage.save(outputName)
    return outputName