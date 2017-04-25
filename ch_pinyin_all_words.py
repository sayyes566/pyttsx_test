from pypinyin import pinyin, lazy_pinyin
import os, sys, pypinyin

file_path = "./ch_roma.txt"
file_export = './pinyin.txt'

wf = open('./pinyin.txt','w+')

with open(file_path) as f:
    content = f.readlines()



content = [x.strip() for x in content]

for ch in content:
    ch_word = ch.split('||')[1]
    ch_pinyiin = pinyin(ch_word, style=pypinyin.BOPOMOFO).pop().pop()
    print(ch_pinyiin)
    wf.write(ch + "||" + ch_pinyiin+'\n')



wf.close()
f.close()