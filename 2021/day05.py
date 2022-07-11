_lines=list(open("day05.txt").read().splitlines())
lines=[[[int(x) for x in coords.split(",")] for coords in _line.split(" -> ")] for _line in _lines]
size=1000

def firstpart():
    diagram=[[0 for x in range(size)] for y in range(size)]
    for line in lines:
        x1,y1,x2,y2=line[0][0],line[0][1],line[1][0],line[1][1]
        if x1==x2:
            for y,_ in enumerate(diagram[x1]):
                if (y<=y1 and y>=y2) or (y>=y1 and y<=y2):
                    diagram[x1][y]+=1
        elif y1==y2:
            for x,_ in enumerate(diagram):
                if (x<=x1 and x>=x2) or (x>=x1 and x<=x2):
                    diagram[x][y1]+=1
    count=0

    for row,_ in enumerate(diagram):
        for col,_ in enumerate(diagram[row]):
            if (diagram[row][col]>=2):
                count+=1
    return count


def secondpart():
    diagram=[[0 for x in range(size)] for y in range(size)]
    for line in lines:
        x1,y1,x2,y2=line[0][0],line[0][1],line[1][0],line[1][1]
        if x1==x2:
            for y,_ in enumerate(diagram[x1]):
                if (y<=y1 and y>=y2) or (y>=y1 and y<=y2):
                    diagram[x1][y]+=1
        elif y1==y2:
            for x,_ in enumerate(diagram):
                if (x<=x1 and x>=x2) or (x>=x1 and x<=x2):
                    diagram[x][y1]+=1
        else:
            for x,_ in enumerate(diagram):
                for y,_ in enumerate(diagram[x]):
                    if abs(x-x1)==abs(y-y1) and ((x<=x1 and x>=x2) or (x>=x1 and x<=x2)) and ((y<=y1 and y>=y2) or (y>=y1 and y<=y2)):
                        diagram[x][y]+=1
        count=0
    print(diagram)

    for row,_ in enumerate(diagram):
        for col,_ in enumerate(diagram[row]):
            if (diagram[row][col]>=2):
                count+=1
    return count
                    

print(firstpart())
print(secondpart())