_list=list(open("day13.txt").read().splitlines())

timestamp=int(_list[0])
line=_list[1].split(',')
IDs=[]
for i in range(len(line)):
    if line[i].isdigit():
        IDs.append((int(line[i]),i))

def modInverse(a, m): 
    m0 = m 
    y = 0
    x = 1
    if (m == 1): 
        return 0
    while (a > 1): 
        q = a // m 
        t = m 
        m = a % m 
        a = t 
        t = y 
        y = x - q * y 
        x = t 
    if (x < 0): 
        x = x + m0 
    return x 

def firstpart():
    waitmax=IDs[0][0]-timestamp%IDs[0][0]
    for id in IDs:
        if id[0]-timestamp%id[0]<waitmax:
            waitmax=id[0]-timestamp%id[0]
            IDmax=id[0]
    return IDmax*waitmax

print(firstpart())

def secondpart():
    prod=1
    stride=1
    start=0
    for id in IDs:
        inverse=modInverse(prod,id[0]) 
        offset=start+id[1]
        stride=id[0]-inverse*offset%id[0] 
        start+=stride*prod
        prod*=id[0]
    return start

print(secondpart())