# JSONデータの読み込み

import json
import gzip

with gzip.open('jawiki-country.json.gz', 'r') as f:
        for line in f:
            data = json.loads(line)

print(data['text'])