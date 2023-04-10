# 先頭からN行を出力

# コマンドライン引数を取り扱うモジュール
import sys

def main():
    value = sys.argv

    with open(value[1], 'r', encoding = 'UTF-8') as f:
        data = f.read()
    
    line = data.split('\n')

    for i in range(int(value[2])):
        print(line[i])

main()