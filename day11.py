from time import perf_counter
_list=list(open("day11.txt").read().splitlines())

grid1=[]
grid2=[]
for line in _list:
    grid1.append([char for char in line])
    grid2.append([char for char in line])
    
def neighbours(grid,i,j,sight):
    neighbours=[]

    for l in range(-1,2):
        for k in range(-1,2):
            if k==0 and l==0:
                continue
            x=i+k
            y=j+l
            if sight:
                while(x>=0 and x<len(grid[0])) and (y>=0 and y<len(grid)):
                    if grid[y][x]!='.':
                        neighbours.append((x,y))
                        break 
                    x+=k
                    y+=l
            else:
                if(x>=0 and x<len(grid[0])) and (y>=0 and y<len(grid)):
                    neighbours.append((x,y))
                    
    return neighbours

def step(grid,fussiness,sight):
    seatstofill=[]
    seatstoempty=[]
    for i in range(len(grid[0])):
        for j in range(len(grid)):
            if grid[j][i]=='L':
                tobefilled=True
                for neighbour in neighbours(grid,i,j,sight):
                    if grid[neighbour[1]][neighbour[0]]=='#':
                        tobefilled=False
                        break
                if tobefilled:
                    seatstofill.append((i,j))
            if grid[j][i]=='#':
                tobeemptied=False
                occupationcount=0
                for neighbour in neighbours(grid,i,j,sight):
                    if grid[neighbour[1]][neighbour[0]]=='#':
                        occupationcount+=1
                        if occupationcount>=fussiness:
                            tobeemptied=True
                            break
                if tobeemptied:
                    seatstoempty.append((i,j))
    return seatstofill,seatstoempty

def firstpart(grid):
    seatstofill,seatstoempty=step(grid,4,False)
    while seatstofill or seatstoempty:
        for seats in seatstofill:
            grid[seats[1]][seats[0]]='#'
        for seats in seatstoempty:
            grid[seats[1]][seats[0]]='L'
        seatstofill,seatstoempty=step(grid,4,False)

    return sum(x.count('#') for x in grid)
 
print(firstpart(grid1))

def secondpart(grid):
    seatstofill,seatstoempty=step(grid,5,True)
    while seatstofill or seatstoempty:
        for seats in seatstofill:
            grid[seats[1]][seats[0]]='#'
        for seats in seatstoempty:
            grid[seats[1]][seats[0]]='L'
        seatstofill,seatstoempty=step(grid,5,True)

    return sum(x.count('#') for x in grid)

print(secondpart(grid2))