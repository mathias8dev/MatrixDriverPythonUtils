from isValidIntHex import isValidIntHex


def pixelsCpFromHex(filePath, width, height, addressSize=4, dataSize=2):
    pixels = []
    start = 2 + addressSize + 2 + 1
    readRow = 0
    readCol = 0
    with open(filePath, "r") as file:

        while readCol < height:
            # print("Read column is ", readCol)
            
            # print("\n\nThe line is \n\n", line)
            array = []
            readRow = 0
            while readRow < width:
                line = file.readline()
                
                striped = line.strip()
                if not isValidIntHex(striped):
                    print(readCol, readRow)
                    raise Exception(f"Line not valid {line}")

                color = striped[start:start+dataSize]
                # print("The color is ", color)
                array.append(int(color, 16))
                readRow = readRow + 1
            # print("Read row is ", readRow)
            # print("The colum is ", readCol)
            readCol = readCol + 1
            pixels.append(array)
            
    return pixels