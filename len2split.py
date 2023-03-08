def len2split(s):
    return [s[i:i+2] for i in range(0, len(s), 2)]


if __name__ == '__main__':
    s = "FF00AA55"
    chunks = len2split(s)
    print(chunks)