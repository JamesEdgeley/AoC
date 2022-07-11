_lines=list(open("day13.txt").read().split("\n\n")[0].splitlines())
points=set([(int(line.split(",")[0]),int(line.split(",")[1])) for line in _lines])
_folds=list(open("day13.txt").read().split("\n\n")[1].splitlines())
folds=[[fold.split("=")[0][-1],int(fold.split("=")[1])] for fold in _folds]
_map={'x':0,'y':1}

def firstpart():
    direction=_map[folds[0][0]]
    axis=folds[0][1]
    for point in list(points):
        if point[direction]>axis:
            copy=list(point)
            points.remove(point)
            copy[direction]=2*axis-point[direction]
            points.add(tuple(copy))
     

    return len(points)

def secondpart():
    for fold in folds[1:]:
        direction=_map[fold[0]]
        axis=fold[1]
        for point in list(points):
            if point[direction]>axis:
                copy=list(point)
                points.remove(point)
                copy[direction]=2*axis-point[direction]
                points.add(tuple(copy))

    for y in range(max([point[1] for point in points])+1):
        for x in range(max([point[0] for point in points])+1):
            if (x,y) in points:
                print("#",end='')
            else:
                print(" ",end='')
        print("")

    

print(firstpart())
secondpart()