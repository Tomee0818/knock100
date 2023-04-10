# タブをスペースに置換

def tab2space(s):
    new_s = s.replace('\t', ' ')     

    return new_s

def main():
    with open('hightemp.txt', 'r', encoding='UTF-8') as f1:
        data = f1.read()

    tmp = tab2space(data)

    with open('hightemp2.txt', 'w', encoding='UTF-8') as f2:
        f2.write(tmp)

main()