# 「パトカー」+「タクシー」=「パタトクカシーー」

def main():
    s1 = "パトカー"
    s2 = "タクシー"
    new_s = ""

    len_s = len(s1)

    for i in range(len_s):
        new_s += s1[i]
        new_s += s2[i]

    print(new_s)

main()