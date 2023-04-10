# n-gram

def word_ngram(s, n):
    wList = []

    word = s.split()
    
    for i in range(len(word)-n+1):
        wList.append(word[i:i+n])

    print(wList)

def char_ngram(s, n):
    tmp = ""
    cList = []

    for i in range(len(s)):
        if s[i].isspace() == False:
            tmp += s[i]
    
    for i in range(len(tmp)-n+1):
        cList.append(tmp[i:i+n])  

    print(cList)  

def main():
    text = "I am an NLPer"
    word_ngram(text, 2)
    char_ngram(text, 2)

main()