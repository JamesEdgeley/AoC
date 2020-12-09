_list=list(open("day9.txt").read().splitlines())
data=[int(i) for i in _list]

def firstpart():
    for i in range(25,len(data)):
        combinations=[]
        for j in range(1,26):
            for k in range(1,j):
                combinations.append(data[i-j]+data[i-k])
        if data[i] not in combinations:
            return data[i]

print(firstpart())

def secondpart():
    target=firstpart()
    for i in range(0,len(data)):
        for j in range(i+1,len(data)):
            if sum(data[i:j+1])==target:
                return max(data[i:j+1])+min(data[i:j+1])
            if sum(data[i:j+1])>target:
                break

print(secondpart())