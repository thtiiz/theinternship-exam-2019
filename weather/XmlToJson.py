import re
import sys
import json
#### Using Tree structure ####
def GetData(data):
    pattern = r'(\s\w+=)|(<)|(>)'
    rawData = []
    for i in data:
        if("<?" not in i):
            x = re.split(pattern, i)
            rawData.append(x)
    return rawData

def DataFilter(rawData):
    data = []
    for i in rawData:
        temp = []
        for j in i:
            if(j):
                j = re.sub(r'(=)', '', j)
                if(not re.search(r'(<)|(>)', j)):
                    if(j[-1]==' '):
                        j = j[0:len(j)-2]
                    temp.append(j)
        data.append(temp)
    return data

def CleanData(data):
    return re.sub(r'"|(\s\/)|(^\s)|(\s$)', '', data)

def GetAtt(data,i):
    att = {}
    keyi = 1
    while(keyi<len(data[i[0]])):
        att[CleanData(data[i[0]][keyi])] = CleanData(data[i[0]][keyi+1])
        keyi += 2
    return att

def createNode(node, data, i=[0], att=0): #use array i because pass by reference
    newNode = {}
    while(i[0]<len(data)):
        thisnode = data[i[0]][0]
        if(not '/' in data[i[0]][-1]): #new Node
            att = GetAtt(data, i)
            i[0]+=1
            newNode[thisnode] = createNode(thisnode, data, i)
            if(att):
                mergeAtt = {**att, **newNode[thisnode]} # merge
                newNode[thisnode] = mergeAtt
                att = 0
        elif('/' in data[i[0]][-1] and i[0]<len(data) and len(data[i[0]])>1):
            if(len(data[i[0]]) == 3 and data[i[0]][-1][-1] != '/'): # 1att or 1 value
                newNode[thisnode] = data[i[0]][1]
            else:
                att = GetAtt(data, i)
                newNode[thisnode] = att
        else:
            return newNode
        i[0]+=1
    return newNode

inFile = sys.argv[1]
with open(inFile, 'r') as f:  
    data = [x.strip() for x in f.readlines()]
rawData = GetData(data)
data = DataFilter(rawData)
tree = createNode(data[0][0], data)
with open(re.sub('.xml', '.json', inFile), 'w') as f: #write dict to json
    json.dump(tree, f, indent = 4)