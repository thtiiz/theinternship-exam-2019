import re

with open("data.xml", 'r') as f:  
    data = [x.strip() for x in f.readlines()]
# print(data)
parent = '</?(\w+)[>\s]'
att = '(\w+="(.+)")'
stack = []
pattern = "<\w+"
for i in data:
    regex = re.compile(parent)
    ans = regex.findall(i)
    if(ans):
        # print(ans)
        stack.append(ans)
    x = re.split(r'\s(\w+)=', i)
    print(x)
    # print(ans)
print(stack)
