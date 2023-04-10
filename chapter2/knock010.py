# 行数のカウント

def count_lines(s):
    count = s.count('\n')

    print(count)

def main():
    with open('hightemp.txt', 'r', encoding='UTF-8') as f:
        data = f.read()

    count_lines(data)

    f.close()

main()