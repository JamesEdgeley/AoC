_list=list(map(int,open("day01.txt").read().splitlines()))

def firstpart():
    count=0
    for i in range(len(_list)-1):
        if _list[i+1]>_list[i]:
            count+=1
    return count
print(firstpart())

def secondpart():
    count=0
    for i in range(len(_list)-3):
        if _list[i+3]>_list[i]:
            count+=1
    return count
print(secondpart())