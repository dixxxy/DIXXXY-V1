input = '北京是个好地方'
ban_words = ['北京','程序员','公务员','领导','牛逼','牛比','你娘','你妈','love','sex']
for i in ban_words:
    input = input.replace(i,'*'*len(i))
print(input)