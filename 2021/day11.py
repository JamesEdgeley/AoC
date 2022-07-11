_lines=list(open("day11.txt").read().splitlines())
array = [[int(x) for x in line] for line in _lines]


def adjacents(i,j):
    adjacents = []
    if i < len(array[0])-1:
        adjacents.append((i+1,j))
        if j < len(array)-1:
            adjacents.append((i+1,j+1))
        if j > 0:
            adjacents.append((i+1,j-1))
    if i > 0:
        adjacents.append((i-1,j))
        if j < len(array)-1:
            adjacents.append((i-1,j+1))
        if j > 0:
            adjacents.append((i-1,j-1))
    if j < len(array)-1:
        adjacents.append((i,j+1))
    if j > 0:
        adjacents.append((i,j-1))
    return adjacents

def flash(i,j,flashed):
    flashed.append((i,j))
    for a,b in adjacents(i,j):
        if (a,b) not in flashed:
            array[b][a]+=1
            if array[b][a]>=10:
                flash(a,b,flashed)
                
    return flashed


def firstpart():
    flashes=0
    for t in range(100):
        flashed=[]  
        for j,row in enumerate(array):
            for i,_ in enumerate(row):
                array[j][i]+=1
                if array[j][i]>9 and (i,j) not in flashed:
                    flash(i,j,flashed)
            
        for i,j in flashed:
            array[j][i]=0
        flashes+=len(flashed)
    return flashes

def secondpart():
    t=0
    while True:
        t+=1
        flashed=[]  
        for j,row in enumerate(array):
            for i,_ in enumerate(row):
                array[j][i]+=1
                if array[j][i]>9 and (i,j) not in flashed:
                    flash(i,j,flashed)
            
        for i,j in flashed:
            array[j][i]=0
        if len(flashed)==100:
            return t

print(firstpart())
array = [[int(x) for x in line] for line in _lines]
print(secondpart())
