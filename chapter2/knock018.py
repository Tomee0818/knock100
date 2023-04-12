# 各行を3コラム目の数値の降順にソート

# コマンドライン引数を取り扱うモジュール
import sys

def main():
    value = sys.argv
    pre_list = []
    sort_pre_list= []
    temp = ""
    data2 = ""
    count_tab = 0

    with open(value[1], 'r', encoding = 'UTF-8') as f1:
        data = f1.read()

    line = data.split('\n')

    for i in range(len(line)):
        for j in range(len(line[i])):
            if count_tab == 2:
                if line[i][j] == '\t':
                    count_tab += 1
                else:
                    temp += line[i][j]
            elif count_tab == 3:
                pre_list.append([line[i], float(temp)])
                temp = ""
                count_tab = 0
                break
            else:
                if line[i][j] == '\t':
                    count_tab += 1
            
    pre_list.sort(reverse=False, key=lambda x:x[1])

    for i in range(len(pre_list)):
        sort_pre_list.append(pre_list[i][0])
    
    for i in range(len(sort_pre_list)):
        data2 += sort_pre_list[i]
        data2 += '\n'

    with open(value[2], 'w', encoding = 'UTF-8') as f2:
        f2.write(data2)

main()