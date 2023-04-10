# 暗号文

def cipher(s):
    cipherList = []
    cipherStr = ""

    for i in range(len(s)):
        if s[i].isalpha():
            cipherList.append(219-ord(s[i]))
        else:
            cipherList.append(s[i])
    
    for i in range(len(cipherList)):
        cipherStr += str(cipherList[i])

    print("cipher: ", cipherStr)

    return cipherList

def decode(l):
    decodeList = []
    decodeStr = ""

    for i in range(len(l)):
        if isinstance(l[i], int):
            decodeList.append(chr(219-l[i]))
        else:
            decodeList.append(l[i])

    for i in range(len(decodeList)):
        decodeStr += str(decodeList[i])

    print("decode: ", decodeStr)

    return decodeList

def main():
    plain = "mizuno2023"
    print("plain:  ", plain)

    plain2cipher = []
    plain2cipher = cipher(plain)

    decode(plain2cipher)

main()