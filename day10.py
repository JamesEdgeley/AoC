from time import perf_counter
_list=list(map(int,open("day10.txt").read().splitlines()))
_list.sort()
_list.insert(0,0)
_list.append(_list[-1]+3)

def firstpart():
    onecount=0
    threecount=0
    for i in range(0,len(_list)-1):
        if _list[i+1]-_list[i]==1:
            onecount+=1
        elif _list[i+1]-_list[i]==3:
            threecount+=1
    return onecount*threecount

print(firstpart())

def calculateperms(gap):
    if gap==1:
        return 1
    if gap==2:
        return 2
    if gap==3:
        return 4
    else:
        return 2*calculateperms(gap-1)-1

def secondpart():
    unremovables=[0]
    for i in range(0,len(_list)-1):
        if _list[i+1]-_list[i-1]>3:
            unremovables.append(i)
    unremovables.append(len(_list)-1)
    arrangements=1
    for i in range(1, len(unremovables)):
        arrangements*=calculateperms(unremovables[i]-unremovables[i-1])
    return arrangements

print(secondpart())
