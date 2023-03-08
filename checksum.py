
def checksum(data):

    sum = 0
    for byte in data:
        sum += byte
    return (~sum + 1) & 0xff

    
if __name__ == '__main__':
    data = [0x01, 0x00, 0xf5, 0x00, 0x01]
    checksum = checksum(data)
    #checksum = checksum([int('01', 16), int('00', 16), int('A4', 16), int('00', 16), 0x01])

    print(f"{10:02x}")
    print("Checksum:", hex(10))

