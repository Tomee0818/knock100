# ファイルをN分割する

# コマンドライン引数を取り扱うモジュール
import sys

def split_list(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]

def main():
    value = sys.argv
    tmp =""

    with open(value[1], 'r', encoding = 'UTF-8') as f:
        data = f.read()
    
    line = data.split('\n')
    for i in range(len(line)):
        line[i] += '\n'

    nsplit_line = list(split_list(line, int(value[2])))

    for i in range(len(nsplit_line)):
        print(nsplit_line[i])

    with open('test.txt', 'w', encoding = 'UTF-8') as f2:
        for i in range(len(nsplit_line[0])):
            tmp += nsplit_line[i][0]
        
        f2.write(tmp)

main()