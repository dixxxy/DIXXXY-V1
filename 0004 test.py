import re,collections
text = "JGood is a handsome boy, he is cool, clever, and so on..."
dic = collections.defaultdict(lambda :0)
data = re.sub(r'[\w\d]', '-', text)
data = data.lower()
datalist = data.split('-')
for item in datalist:
    dict[item] += 1
del dic['-']
print(dic)