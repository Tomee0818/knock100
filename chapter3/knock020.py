# JSONデータの読み込み

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
    print(read_wiki(fname, 'イギリス'))

main()