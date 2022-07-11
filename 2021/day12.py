_lines=list(open("day12.txt").read().splitlines())

_vertices = set([line.split('-')[0] for line in _lines]+[line.split('-')[1] for line in _lines])

def calcadj():
    adj={}
    for vertex in _vertices:
        adj[vertex]=[]
    for line in _lines:
        adj[line.split('-')[0]].append(line.split('-')[1])
        adj[line.split('-')[1]].append(line.split('-')[0])
    return adj

_adj=calcadj()

def countpaths(start,end,visited,count,part,flag):
    if start.islower():
        visited[start]+=1
    if start==end:
        count[0]+=1
    else:
        for adj in _adj[start]:
            if visited[adj]==0:
                countpaths(adj,end,visited,count,part,flag)
            elif part==2 and flag[0]==False and visited[adj]==1 and adj!="start":
                flag[0]=True
                countpaths(adj,end,visited,count,part,flag)
                flag[0]=False
    if start.islower():
        visited[start]-=1
    

def firstpart():
    visited={}
    for vertex in _vertices:
        visited[vertex]=0
    count=[0]
    flag=[False]
    countpaths("start","end",visited,count,1,flag)
    return count[0]

def secondpart():
    visited={}
    for vertex in _vertices:
        visited[vertex]=0
    count=[0]
    flag=[False]
    countpaths("start","end",visited,count,2,flag)
    return count[0]


print(firstpart())
print(secondpart())
