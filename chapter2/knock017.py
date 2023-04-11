# １列目の文字列の異なり

# コマンドライン引数を取り扱うモジュール
import sys

def main():
    value = sys.argv
    col1_set = set()

    with open(value[1], 'r', encoding = 'UTF-8') as f:
        data = f.read()

    line = data.split('\n')
    pre_s = ""

    for i in range(len(line)):
        for j in range(len(line[i])):
            if line[i][j] == '\t':
                col1_set.add(pre_s)
                pre_s = ""
                break
            else:
                pre_s += line[i][j]
        
    print(col1_set)

main()