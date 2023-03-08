from checksum import checksum
from len2split import len2split

def isValidIntHex(hexString):
    # print(f"The hexstring is {hexString}")
    if len(hexString) == 0:
        return False
    splited = [int(it, 16) for it in len2split(hexString[1:len(hexString)])]
    if (checksum(splited[:-1]) != splited[-1]):
        return False
    return True