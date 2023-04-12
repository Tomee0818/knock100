# カテゴリ名を含む行を抽出

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

    data = read_wiki(fname, 'イギリス')

    line = data.split('\n')

    for i in range(len(line)):
         if 'Category' in line[i]:
              print(line[i])

main()