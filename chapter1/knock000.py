#文字列の逆順

def main():
    s = "streesed"
    new_s = ""
    s_len = len(s)

    for i in range(s_len):
        new_s += s[(s_len-1) - i]

    print(new_s)

main()