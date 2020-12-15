_list=list(open("day15.txt").read().split(','))

lastturn={}
for i in range(len(_list)-1):
    lastturn[int(_list[i])]=i+1
lastone=int(_list[-1])

def firstpart(end):
    global lastone
    turn=len(_list)+1
    while turn<=end:
        if lastone in lastturn:
            result=turn-1-lastturn[lastone]
        else:
            result=0
        lastturn[lastone]=turn-1
        lastone=result
        turn+=1
    return lastone

print(firstpart(2020))

lastturn={}
for i in range(len(_list)-1):
    lastturn[int(_list[i])]=i+1
lastone=int(_list[-1])

print(firstpart(30000000))



