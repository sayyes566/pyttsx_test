import os
import time
file_news = 'news'
file_pinin = 'ch_roma_pinin.txt'

'''
with open(file_news) as f:
    content = f.readlines()
list_content = [x.strip() for x in content]
    '''
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
enter_no = 'n'

print("pleace input sentence")
sentence = input()
start_time = time.time()

print (sentence)
print("pleace enter to start")
if (enter_word == input()):
    for word in sentence:
        
        speak_time = int(time.time() - start_time)
        satisfy = False
        if( word in dist_word):
            roma = dist_word[word][0]
            pinin = dist_word[word][1]
            roma_sentence += roma + ' '
            while(satisfy == False):
                print ("===============")
                print (sentence)
                print ("===============")
                print (word, roma, pinin)
                time.sleep(1)
                #print("pleace enter to start")
                #if (enter_word == input()):
                
                #print("1-sec")
                os.system('sudo python3 record_enter.py ' + roma)
                os.system('sudo python ../play_wave.py wav '+ roma)
                print ("are you satisfy? enter=yes, input n = no")
                if ( enter_no == input()):
                    satisfy = False
                else:
                    satisfy = True
            
            #print("pleace enter")
            #if (enter_word == input()):
            #    os.system('sudo python ../detect_audio.py ' + roma)
        else:
            roma = 'space'
            pinin = word
                    

print (sentence)
print (roma_sentence)
os.system('sudo python ../play_wave.py wav '+ roma_sentence)
os.system('sudo python3 ../slice_combine.1.py '+ roma_sentence)

