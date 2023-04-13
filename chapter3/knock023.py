# セクション構造

import json
import gzip

def read_wiki(fname, title):
    with gzip.open(fname, 'r') as f:
        for line in f:
            data = json.loads(line)

            if data['title'] == title:
                    return data['text']

def ex_section(data):
    rank = -1
    ex_comp = 0
    section_name = ""
    section_list = []

    line = data.split('\n')

    for i in range(len(line)):
        if '==' in line[i]:
            for j in range(len(line[i])):
                if line[i][j] == '=' and ex_comp == 0:
                    rank += 1
                elif line[i][j] == '=' and ex_comp == 1:
                    section_list.append([section_name, rank])
                    rank = -1
                    ex_comp = 0
                    section_name = ""
                    break
                else:
                    section_name += line[i][j]
                    ex_comp = 1

    return section_list

         




def main():
    fname = 'jawiki-country.json.gz'
    title = 'イギリス'

    data = read_wiki(fname, title)

    section = ex_section(data)

    print(section)

main()