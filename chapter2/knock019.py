# 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる

# コマンドライン引数を取り扱うモジュール
import sys

def main():
    value = sys.argv
    pre_list = []
    sort_pre_list= []
    pref = ""
    data2 = ""
    count_pre = []
    prefecture =   ['北海道', '青森県', '岩手県', '宮城県', '秋田県', '山形県', '福島県',
                    '茨城県', '栃木県', '群馬県', '埼玉県', '千葉県', '東京都', '神奈川県',
                    '新潟県', '富山県', '石川県', '福井県', '山梨県', '長野県', '岐阜県',
                    '静岡県', '愛知県', '三重県', '滋賀県', '京都府', '大阪府', '兵庫県',
                    '奈良県', '和歌山県','鳥取県', '島根県', '岡山県', '広島県', '山口県',
                    '徳島県', '香川県', '愛媛県', '高知県', '福岡県', '佐賀県', '長崎県',
                    '熊本県', '大分県', '宮崎県', '鹿児島県', '沖縄県']

    with open(value[1], 'r', encoding = 'UTF-8') as f1:
        data = f1.read()

    line = data.split('\n')

    for i in range(len(line)):
        for j in range(len(line[i])):
            if line[i][j] == '\t':
                pre_list.append([line[i], pref])
                pref = ""
                break
            else:
                pref += line[i][j]

    for i in range(len(prefecture)):
        count_pre.append([prefecture[i], 0])

    for i in range(len(pre_list)):
        for j in range(len(count_pre)):
            if pre_list[i][1] == count_pre[j][0]:
                count_pre[j][1] += 1
            

    count_pre.sort(reverse=True, key=lambda x:x[1])

    for i in range(len(count_pre)):
        for j in range(len(pre_list)):
            if count_pre[i][0] == pre_list[j][1]:
                sort_pre_list.append(pre_list[j][0])

    for i in range(len(sort_pre_list)):
        data2 += sort_pre_list[i]
        data2 += '\n'

    with open(value[2], 'w', encoding = 'UTF-8') as f2:
        f2.write(data2)

main()