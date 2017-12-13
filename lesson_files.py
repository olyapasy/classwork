# file_path = r'C:\Users\User\Desktop\test.txt' #r отключает специальные символы
# f = open(file_path,'w+')
# for i in range(100):
#     f.write('Hello world %d\n' % i)
# f.close()
#
#
import pprint
import  string

def word_counter(file_path,file_path_stop_words, num_limit = 20):
    f = open(file_path)
    content = f.read()
    lst_words = content.split()
    f.close()

    f2 = open(file_path_stop_words)
    content_stop_words = f2.read()
    lst_stop_words = content_stop_words.split()
    f2.close()


    print(len(lst_words))
    print(len(lst_stop_words))
    word_stats = {}
    for word in lst_words:

        if word not in lst_stop_words:
            word = word.strip(string.punctuation)
            if word:
                if word in word_stats:
                    word_stats[word] += 1
                else:
                    word_stats[word] = 1

    for key in sorted(word_stats.keys(), key=lambda key: word_stats[key],reverse=True) [:num_limit]:
        print('%s:\t%d' %(key,word_stats[key]))
    #pprint.pprint(word_stats)
word_counter('hhgttg.txt','stop_words.txt')
