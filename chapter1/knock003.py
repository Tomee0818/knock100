# 円周率

def main():
    s = "Now I need a drink, alcoholic of course, after the heavy \
        lectures involving quantum mechanics."

    word = s.split()

    word_len = []
    for i in range(len(word)):
        word_len.append(len(word[i]))

    print(word_len)

main()