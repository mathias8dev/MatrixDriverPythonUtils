def zipPixels(redPixels, greenPixels, bluePixels):
    pixels = []
    if (len(redPixels) != len(greenPixels) != len(bluePixels)):
        raise Exception("The different components should be of the same size")
    for lineIndex in range(len(redPixels)):
        if len(redPixels[lineIndex]) != len(greenPixels[lineIndex]) != len(bluePixels[lineIndex]):
            raise Exception("Lines should be of the same size")
        pixels.append(
            list(zip(redPixels[lineIndex], greenPixels[lineIndex], bluePixels[lineIndex])))
    return pixels
