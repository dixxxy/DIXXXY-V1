# 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights

input = 'sex'
ban_words = ['北京','程序员','公务员','领导','牛逼','牛比','你娘','你妈','love','sex']
if input in ban_words:
    input = input.replace(input,'Freedom')
else:
    input = input.replace(input,'Human Rights')

print(input)
