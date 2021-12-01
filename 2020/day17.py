import itertools
_list=list(open("day17.txt").read().splitlines())

def init(_list,dim):
    alive=[]
    for i in range(len(_list)):
        for j in range (len(_list[0])):
            if _list[i][j]=='#':
                coord=[i,j]
                for d in range(dim-2):
                    coord.append(0)
                alive.append(coord)
    return alive


def isneighbour(cell1,cell2,dim):
    isneighbour=True
    for d in range(dim):
        if cell2[d]==cell1[d] or cell2[d]==cell1[d]+1 or cell2[d]==cell1[d]-1:
            continue
        else:
            isneighbour=False
    return isneighbour

def epsilon(dim):
    epsilon=list(itertools.product([-1,0,1],repeat=dim))
    return epsilon

def step(life,dim,epsilon):
    vanoflife=[]
    vanofdeath=[]
    for cell1 in life:
        adjacentlife=0
        stayingalive=True
        for cell2 in life:
            if adjacentlife>3:
                stayingalive=False
                break
            if cell2==cell1:
                continue

            if isneighbour(cell1,cell2,dim):
                adjacentlife+=1

        for eps in epsilon:
            candidate=[]        
            for d in range(dim):
                candidate.append(cell1[d]+eps[d])
            if candidate in vanoflife or candidate in life:
                continue
            adjacentlife2=0
            for cell2 in life:
                if adjacentlife2>2:
                    break
                if cell2==cell1:
                    continue
                if isneighbour(cell2,candidate,dim):
                    adjacentlife2+=1

            if adjacentlife2==2:
                vanoflife.append(candidate)
        

        if adjacentlife<2 or adjacentlife>3:
            stayingalive=False
        if not stayingalive:
            vanofdeath.append(cell1)

    for cell in vanoflife:
        life.append(cell)

    for cell in vanofdeath:
        life.remove(cell)


def firstpart():
    dim=3
    life=init(_list,dim)
    t=0
    eps=epsilon(dim)
    while t<6:
        step(life,dim,eps)
        t+=1
    return(len(life))

print(firstpart())

def secondpart():
    dim=4
    life=init(_list,dim)
    t=0
    eps=epsilon(dim)
    while t<6:
        step(life,dim,eps)
        t+=1
    return(len(life))

print(secondpart())