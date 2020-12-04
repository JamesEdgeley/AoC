_list=list(open("day3.txt").read().splitlines())

def firstpart(right, down):
    treecount=0
    column=0
    newlist=_list[::down]
    for line in newlist:
        if line[column%len(line)]=='#':
            treecount+=1
        column+=right
    return treecount

print(firstpart(3,1))

paths=[(1,1),(3,1),(5,1),(7,1),(1,2)]

def secondpart():
    product=1
    for path in paths:
        product*=firstpart(*path)
    return product

print(secondpart())