import json

ar = []

with open('C:\\Users\\dimam\\tg_bot\\word.txt', encoding='utf-8') as r:
    for i in r:
        n = i.lower().split('/n')[0]
        if n != '':
            ar.append(n)


with open('C:\\Users\\dimam\\tg_bot\\words.json', 'w', encoding='utf-8') as e:
    json.dump(ar, e)