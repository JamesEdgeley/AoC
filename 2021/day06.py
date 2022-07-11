_list = list(map(int,open("day06.txt").read().split(",")))

def firstpart():
    period=80
    fishlist=[fish for fish in _list]
    for day in range(period):
        newfish=0
        for i,fish in enumerate(fishlist): 
            if fish==0:
                fishlist[i]=6
                newfish+=1
            else:
                fishlist[i]=fish-1
        for i in range(newfish):
            fishlist.append(8)

    return len(fishlist)

def secondpart():
    period=256
    fishlist=[fish for fish in _list]
    fishdict={}
    for age in range(9):
        fishdict[age]=fishlist.count(age)
    for day in range(period):
        newfish=fishdict[0] 
        for age in range(1,9):  
                fishdict[age-1]=fishdict[age]
        fishdict[6]+=newfish
        fishdict[8]=newfish
        
    sum=0
    for age in range(9):
        sum+=fishdict[age]
    return sum


print(firstpart())
print(secondpart())

