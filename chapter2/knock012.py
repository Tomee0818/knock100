# 1列目をcol1.txtに，2列目をcol2.txtに保存

def main():
    with open('hightemp.txt', 'r', encoding='UTF-8') as f1:
        data = f1.read()
    
    line = data.split('\n')

    with open('col1.txt', 'w', encoding='UTF-8') as f2:
        f2.write(line[0])
    with open('col2.txt', 'w', encoding='UTF-8') as f3:
        f3.write(line[1])

main()