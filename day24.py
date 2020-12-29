_list=list(open("day24.txt").read().splitlines())

directions={'e':(1,0),'ne':(0,1),'nw':(-1,1),'w':(-1,0),'sw':(0,-1),'se':(1,-1)}

blacks=set()
def firstpart():
    for tile in _list:
        coords=[]
        it = enumerate(tile)
        for index,char in it:
            if char=='n' or char=='s':
                coords.append(char+tile[index+1])
                next(it)
            else:
                coords.append(char)
        destination=[0,0]
        for step in coords:
            destination[0]+=directions[step][0]
            destination[1]+=directions[step][1]
        if tuple(destination) in blacks:
            blacks.remove(tuple(destination))
        else:
            blacks.add(tuple(destination))
    return len(blacks)
print(firstpart())

def secondpart():
    for i in range(100):
        blackstoflip=set()
        whitestoflip=set()
        for tile in blacks:
            blackneighbours=0
            isflipped=False
            for neighbour in directions.values():
                neighbourcoords = (neighbour[0]+tile[0],neighbour[1]+tile[1])
                if neighbourcoords in blacks:
                    blackneighbours+=1
                    if blackneighbours>2:
                        isflipped=True
                else:
                    black2neighbours=0
                    for neighbour2 in directions.values():
                        neighbour2coords = (neighbour2[0]+neighbourcoords[0],neighbour2[1]+neighbourcoords[1])
                        if neighbour2coords==tile:
                            continue
                        if neighbour2coords in blacks:
                            black2neighbours+=1
                            if black2neighbours>1:
                                break
                    if black2neighbours==1:
                        whitestoflip.add(neighbourcoords)
            if blackneighbours==0:
                isflipped=True
            if isflipped:
                blackstoflip.add(tile)
        for tile in blackstoflip:
            blacks.remove(tile)
        for tile in whitestoflip:
            blacks.add(tile)
    return len(blacks)

print(secondpart())