# テンプレートによる文生成

def temperature(x, y, z):
    s = str(x) + "時の" + str(y) + "は" + str(z)

    return s

def main():
    text = temperature(12, "気温", 22.4)

    print(text)

main()