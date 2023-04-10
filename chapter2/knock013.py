# col1.txtとcol2.txtをマージ

def main():
    with open('col1.txt', 'r', encoding = 'UTF-8') as f1:
        data1 = f1.read()
    with open('col2.txt', 'r', encoding = 'UTF-8') as f2:
        data2 = f2.read()     

    data = data1 + '\t' + data2

    with open('merge.txt', 'w', encoding = 'UTF-8') as f3:
        f3.write(data)     

main()