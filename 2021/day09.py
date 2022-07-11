_lines=list(open("day09.txt").read().splitlines())
array = [[int(x) for x in line] for line in _lines]

def adjacents(i,j):
    adjacents = []
    if i < len(array[0])-1:
        adjacents.append(array[j][i+1])
    if i > 0:
        adjacents.append(array[j][i-1])
    if j < len(array)-1:
        adjacents.append(array[j+1][i])
    if j > 0:
        adjacents.append(array[j-1][i])
    return adjacents

def measurebasin(i,j,size):
    if array[j][i]==9 or array[j][i]==-1 or i >= len(array[0])-1 or i <= 0 or j >= len(array)-1 or j <= 0:
        return 0
    array[j][i]=-1
    size[-1]+=1
    measurebasin(i,j+1,size)
    measurebasin(i,j-1,size)
    measurebasin(i-1,j,size)
    measurebasin(i+1,j,size)
    return size



def firstpart():
    total = 0
    for j,y in enumerate(array):
        for i,_ in enumerate(y):
            if array[j][i] < min(adjacents(i, j)):
                total += 1 + array[j][i]
    return total

def secondpart():
    basins=[]
    for j,y in enumerate(array):
        for i,_ in enumerate(y):
            basins.append(0)
            measurebasin(i,j,basins)
    top3=sorted(basins)[-3:]
    return top3[0]*top3[1]*top3[2]
            
print(firstpart())
print(secondpart())