# 末尾のN行を出力

# コマンドライン引数を取り扱うモジュール
import sys

def main():
    value = sys.argv

    with open(value[1], 'r', encoding = 'UTF-8') as f:
        data = f.read()
    
    line = data.split('\n')

    e_top = len(line) - int(value[2]) - 1
    e_end = len(line) - 1

    for i in range(e_top, e_end):
        print(line[i])

main()