import re
import sys

def GetData(rawData):
    data = []
    stack = []
    for i in rawData:
        temp = []
        for j in i:
            if(j):
                j = re.sub(r'(=)', '', j)
                if(not re.search(r'(<)|(>)', j)):
                    if(j[-1]==' '):
                        j = j[0:len(j)-2]
                    temp.append(j)
        if(temp[0]!='/'):
            stack.append(temp[0])
        else:
            stack.append(temp[1])
        data.append(temp)
    return (data,stack)

def WriteData(key, value, tab, f):
    f.write("\t" * tab + key + ': ' + value)

def Case1(i, f, tab):
    if(i[0]!='/'):
        WriteData('"'+ i[0] +'"', '{\n', tab, f)
    tab+=1
    for j in range (1, len(i)-1, 2):
        i[j] = re.sub(r' ', '', i[j])
        i[j+1] = re.sub(r'"', '', i[j+1])
        WriteData('"'+ i[j] +'"', '"'+ i[j+1] +'"', tab, f)
        if(j!=len(i)-3): 
            f.write(',')
        f.write("\n")
    tab -=1
def match(stack):
    if(stack[len(stack)-1] in stack[0:len(stack)-2]):
        stack.pop()
        return True
    else:
        return False
def WriteFile(i, tab, data, node, f, stack):
    if(i>=len(data)): #out of range
        return 0
    ################### Append
    if(node):
        if(node[0] == '/'):
            node.pop(0)
        stack.append(node[0])
        node.pop(0)
        # print(stack)
    ##################
    if(match(stack)):
        tab-=1
        f.write("\t"*tab + '}')
        if(i<len(data)-1):
            f.write(',\n')
        else:
            f.write('\n')
        tab-=1
        
    if(data[i][-1] == '/'):
        Case1(data[i][0:len(data)-1], f, tab)
        f.write("\t"*tab + '}')
        if(not node):
            end = 1
        elif(node[0] in stack):
            end = 1
        else:
            end = 0
        if(i < len(data)-1 and not end):
            f.write(',\n')
        else:
            f.write('\n')
    elif(len(data[i])==4):
        WriteData('"'+ data[i][0] +'"', '"'+ data[i][1] + '",\n', tab, f)
    else:
        Case1(data[i][0:len(data)-1], f, tab)
        tab+=1
    WriteFile(i+1, tab, data, node, f, stack)

inFile = sys.argv[1]
with open(inFile, 'r') as f:  
    data = [x.strip() for x in f.readlines()]
pattern = r'(\s\w+=)|(<)|(>)|(\/)'
rawData = []
for i in data:
    if("<?" not in i):
        x = re.split(pattern, i)
        rawData.append(x)
(data, stack) = GetData(rawData)
print(data)
stack.pop(0)
stack.pop(len(stack)-1)
f = open("o.json", 'w+')
f.write('{\n')
WriteFile(1, 1, data, stack, f, [])
f.write('}')