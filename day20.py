_list=list(open("day20.txt").read().split('\n\n'))

translation={35: 49, 46: 48}
pieces={}
tiles={}
for piece in _list:
    id=int(piece.split(':')[0].split(' ')[1])
    edge1=int(piece.splitlines()[1].translate(translation),2)
    edge2=int(''.join([line[-1] for line in piece.splitlines()]).translate(translation)[1:],2)
    edge3=int(piece.splitlines()[-1].translate(translation)[::-1],2)
    edge4=int(''.join([line[0] for line in piece.splitlines()]).translate(translation)[:0:-1],2)
    pieces[id]=[edge1,edge2,edge3,edge4]
    tiles[id]=[[char for char in row] for row in piece.split(':')[1][1:].splitlines()]


def flip(edge):
    return int('{:010b}'.format(edge)[::-1], 2)


edges=[]
corners=[]
pairs=set()
def firstpart():
    product=1
    for key,value in pieces.items():
        uniques=0
        for code in value:
            isunique=True
            for key2,value2 in pieces.items():
                if key2==key:
                    continue
                if code in value2 or code in [flip(_) for _ in value2] or flip(code) in value2:
                    pairs.add((frozenset({key,key2})))
                    isunique=False
                    break  
            if isunique:
                uniques+=1
        if uniques>=1:
            edges.append(key)
        if uniques==2:
            corners.append(key)
            product*=key
    return product

print(firstpart())

grid = [['' for i in range(12)] for j in range(12)]

grid[0][0]=corners[0]
for i in range(1,12):
    for pair in pairs:
        first,second=pair
        if grid[0][i-1]==first and second in edges:
            grid[0][i]=second
            pairs.remove(pair)
            break
        elif grid[0][i-1]==second and first in edges:
            grid[0][i]=first
            pairs.remove(pair)
            break

for j in range(1,12):
    for i in range(12):
        for pair in pairs:
            first,second=pair
            if grid[j-1][i]==first:
                grid[j][i]=second
                pairs.remove(pair)
                if i>0:
                    pairs.remove(frozenset({grid[j][i],grid[j][i-1]}))
                break
            elif grid[j-1][i]==second:
                grid[j][i]=first
                pairs.remove(pair)
                if i>0:
                    pairs.remove(frozenset({grid[j][i],grid[j][i-1]}))
                break

def D4cycle(invert, edges):
    edge1,edge2,edge3,edge4=edges
    if invert:
        edge1,edge2,edge3,edge4=[flip(edge1),flip(edge4),flip(edge3),flip(edge2)]
    edges=[edge4,edge1,edge2,edge3]
    return edges

def transform(tile,D4index):
    if D4index==0:
        return tile
    if D4index==1:
        return [[tile[j][i] for j in range(len(tile)-1,-1,-1)] for i in range(len(tile[0]))]
    if D4index==2:
        return [[tile[i][j] for j in range(len(tile[0])-1,-1,-1)] for i in range(len(tile)-1,-1,-1)]
    if D4index==3:
        return [[tile[j][i] for j in range(len(tile))] for i in range(len(tile[0])-1,-1,-1)]
    if D4index==4:
        return [[tile[i][j] for j in range(len(tile[0]))] for i in range(len(tile)-1,-1,-1)]
    if D4index==5:
        return [[tile[j][i] for j in range(len(tile))] for i in range(len(tile[0]))]
    if D4index==6:
        return [[tile[i][j] for j in range(len(tile[0])-1,-1,-1)] for i in range(len(tile))]
    if D4index==7:
        return [[tile[j][i] for j in range(len(tile)-1,-1,-1)] for i in range(len(tile[0])-1,-1,-1)]

element=0
while pieces[grid[0][0]][1] not in pieces[grid[0][1]] + [flip(_) for _ in pieces[grid[0][1]]] or pieces[grid[0][0]][2] not in pieces[grid[1][0]] + [flip(_) for _ in pieces[grid[1][0]]]:
    invert=False
    element+=1
    if element%8==4:
        invert=True
    pieces[grid[0][0]]=D4cycle(invert,pieces[grid[0][0]])
tiles[grid[0][0]]=transform(tiles[grid[0][0]],element)

for i in range(1,12):
    element=0
    while pieces[grid[0][i]][3] != flip(pieces[grid[0][i-1]][1]):
        invert=False
        element+=1
        if element%8==4:
            invert=True
        pieces[grid[0][i]]=D4cycle(invert,pieces[grid[0][i]])
    tiles[grid[0][i]]=transform(tiles[grid[0][i]],element)

for j in range(1,12):
    for i in range(12):
        element=0
        while pieces[grid[j][i]][0] != flip(pieces[grid[j-1][i]][2]):
            invert=False
            element+=1
            if element%8==4:
                invert=not invert
            pieces[grid[j][i]]=D4cycle(invert,pieces[grid[j][i]])
        tiles[grid[j][i]]=transform(tiles[grid[j][i]],element)

image = [['' for i in range(96)] for j in range(96)]

hashcount=0
for j in range(len(image)):
    for i in range(len(image[0])):
        redi=i//8
        redj=j//8
        image[j][i]=tiles[grid[redj][redi]][1:-1][j%8][1:-1][i%8]
        if image[j][i]=='#':
            hashcount+=1

seamonster=[(0,18),(1,0),(1,5),(1,6),(1,11),(1,12),(1,17),(1,18),(1,19),(2,1),(2,4),(2,7),(2,10),(2,13),(2,16)] 
seamonstercount=0
element=0
while seamonstercount==0:
    for j in range(len(image)-3):
        for i in range(len(image[0])-20):
            isseamonster=True
            for part in seamonster:
                if image[j+part[0]][i+part[1]]!='#':
                    isseamonster=False
                    break
            if isseamonster:
                seamonstercount+=1
    element+=1
    image=transform(image,element)

print(hashcount-seamonstercount*15)

