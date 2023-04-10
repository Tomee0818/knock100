# 集合

def c_bigram(char):

    c_set = set()

    for i in range(len(char)-1):
        c_set.add(char[i:i+2])

    return c_set

def main():
    s1 = "paraparaparadise"
    s2 = "paragraph"

    X = c_bigram(s1)
    Y = c_bigram(s2)

    union = X | Y
    inter = X & Y
    diff1 = X - Y
    diff2 = Y - X

    print("X: ", X)
    print("Y: ", Y)
    print("X and Y: ", union)
    print("X or Y: ", inter)
    print("X - Y: ", diff1)
    print("Y - X: ", diff2)

    if "se" in X:
        print('"se" is in X')
    else:
        print('"se" is not in X')
    if "se" in Y:
        print('"se" is in Y')
    else:
        print('"se" is not in Y')

main()