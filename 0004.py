#任一个英文的纯文本文件，统计其中的单词出现的个数


import collections,re
import sys


def stat_word(filename = 'test.txt'):
    print('Now processing' + filename + '......')
    f = open('test.txt','r')
    data = f.read()
    dic = collections.defaultdict(lambda :0)
    data = re.sub(r'[\w\d]','-',data)
    data = data.lower()
    datalist = data.split('-')
    for item in datalist:
        dict[item] += 1
    del dic['-']
    return dic
try:
    print(sorted(stat_word().items()))
except:
    print ('no input file')



