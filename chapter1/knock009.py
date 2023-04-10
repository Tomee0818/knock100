# Typoglycemia

import random

def char_shuffle(word):
    sList = []
    sList2 = []
    sWord = ""

    if len(word) > 4:
        for i in range(len(word)):
            sList.append(word[i])

        sList2 = sList[1:len(sList)-1]

        random.shuffle(sList2)

        sList[1:len(sList)-1] = sList2

        for i in range(len(sList)):
            sWord += sList[i]
    else:
        return word

    return sWord

def str_shuffle(s):
    word = ""
    sStr = ""

    for i in range(len(s)):
        if s[i].isspace():
            sStr += char_shuffle(word)
            word = ""
            sStr += s[i]
        else:
            word += s[i]
    sStr += char_shuffle(word)
        
    return sStr

def main():
    text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    print("before: ", text)

    new_s = str_shuffle(text)

    print("after:  ", new_s)

main()