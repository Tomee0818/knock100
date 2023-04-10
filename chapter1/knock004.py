# 元素記号

def main():
    s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. \
        New Nations Might Also Sign Peace Security Clause. Arthur King Can."

    word = s.split()

    d = {}
    list1 = [1,5,6,7,8,9,15,16,19]
    for i in range(1, len(word)+1):
        if i in list1:
            d[word[i-1][0]] = i
        else:
            d[word[i-1][0:2]] = i

    print(d)

main()