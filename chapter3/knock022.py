# カテゴリ名の抽出

import json
import gzip

def read_wiki(fname, title):
    with gzip.open(fname, 'r') as f:
        for line in f:
            data = json.loads(line)

            if data['title'] == title:
                    return data['text']

def main():
    fname = 'jawiki-country.json.gz'
    category_list = []
    tmp = ""

    data = read_wiki(fname, 'イギリス')

    line = data.split('\n')

    for i in range(len(line)):
        if 'Category' in line[i]:
            for j in range(11, len(line[i])):
                if line[i][j] == ']':
                    category_list.append(tmp)
                    tmp = ""
                    break
                else:
                    tmp += line[i][j]

    print(category_list)

main()