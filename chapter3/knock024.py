# ファイル参照の抽出

import json
import gzip
import re

def read_wiki(fname, title):
    with gzip.open(fname, 'r') as f:
        for line in f:
            data = json.loads(line)

            if data['title'] == title:
                    return data['text']

def ex_url(data):
    url_list = []
    url_pattern = "https?://[\w/:%#\$&\?\(\)~\.=\+\-]+"

    line = data.split('\n')

    for i in range(len(line)):
        if 'http' in line[i]:
            url_list.append(re.findall(url_pattern, line[i])[0])
    
    return url_list

def make_file(list_data, fname):
    data = ""

    for i in range(len(list_data)):
        list_data[i] += '\n'
        data += list_data[i]
    
    with open(fname, 'w', encoding = 'UTF-8') as f:
        f.write(data)
    
def main():
    fname = 'jawiki-country.json.gz'
    title = 'イギリス'

    data = read_wiki(fname, title)

    url_list = ex_url(data)

    make_file(url_list, 'url.txt')

    #print(url_list)

main()