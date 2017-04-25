import os

# 要唸得句子
file_news = 'news'
# 查表
file_pinin = 'ch_roma_pinin.txt'

with open(file_news) as f:
    content = f.readlines()
list_content = [x.strip() for x in content]
    
with open(file_pinin) as f:
    con_pinin = f.readlines()
list_pinin = [x.strip() for x in con_pinin]

'''
make distinary
like :'鎳': ['nie', 'ㄋㄧㄝˋ']}
'''
dist_word = {}
for ele_pinin_set in list_pinin:
    list_pinin_set = ele_pinin_set.split("||")
    dist_word [list_pinin_set[1]] = [list_pinin_set[2],list_pinin_set[3]]
   

roma_sentence = ''
enter_word = ''
for sentence in list_content:
    for word in sentence:
            if( word in dist_word):
                roma = dist_word[word][0]
                pinin = dist_word[word][1]
                #print (word, roma, pinin)
                roma_sentence += roma + ' '
            else:
                roma = 'space'
                pinin = word
        

print (list_content)
#print (roma_sentence)
#combine all wavs sound, then play output a wav
print ('sudo python3 ../slice_combine.1.py %s' % roma_sentence)
os.system('sudo python3 ../slice_combine.1.py '+ roma_sentence)

