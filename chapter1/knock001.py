# 「パタトクカシーー」

def main():
    s = "パタトクカシーー"
    new_s = ""
    s_len = len(s)

    for i in range(s_len):
        if i%2 == 0:
            new_s += s[i]

    print(new_s)

main()