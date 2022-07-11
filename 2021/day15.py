_lines=list(open("day15.txt").read().splitlines())
array = [[int(x) for x in line] for line in _lines]
bigarray=[[(i+j+num-1)%9+1 for i in range(0,5) for num in line] for j in range(0,5) for line in array]

def adjacents(i,j,x,y):
    adjacents = []
    if i < x-1:
        adjacents.append((i+1,j))
    if i > 0:
        adjacents.append((i-1,j))
    if j < y-1:
        adjacents.append((i,j+1))
    if j > 0:
        adjacents.append((i,j-1))
    return adjacents

def firstpart():
    unvisited={}
    visited=set()
    for i,row in enumerate(array):
        for j,col in enumerate(row):
            unvisited[(i,j)]=float("inf")
    
    unvisited[(0,0)]=0
    
    while unvisited:
        u=min(unvisited,key=unvisited.get)
        if u==(len(array)-1,len(array[-1])-1):
            return(unvisited[u])
        
        for neighbour in adjacents(u[0],u[1],len(array),len(array[0])):
            if neighbour not in visited:
                distance=unvisited[u]+array[neighbour[0]][neighbour[1]]
                if distance<unvisited[neighbour]:
                    unvisited[neighbour]=distance
        visited.add(u)
        unvisited.pop(u)

import heapq
def secondpart():
    visitqueue=[(0,(0,0))]

    visited=set()
    distances={}
    for i,row in enumerate(bigarray):
        for j,col in enumerate(row):
            distances[(i,j)]=float("inf")
    distances[(0,0)] = 0
    
    
    while visitqueue:
        
        olddist,u=heapq.heappop(visitqueue)
        if u==(len(bigarray)-1,len(bigarray[-1])-1):
            return(olddist)
        
        for neighbour in adjacents(u[0],u[1],len(bigarray),len(bigarray[0])):
            if neighbour not in visited:
                newdist=olddist+bigarray[neighbour[0]][neighbour[1]]
                if newdist<distances[neighbour]:
                    distances[neighbour]=newdist
                    heapq.heappush(visitqueue,(newdist,neighbour))
                    visited.add(u)




print(firstpart())
print(secondpart())