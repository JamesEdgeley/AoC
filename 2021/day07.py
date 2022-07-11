_list = list(map(int,open("day07.txt").read().split(",")))

from statistics import median
def firstpart():
    centre = round(median(_list))
    fuel=0
    for pos in _list:
        fuel+=abs(pos-centre)
    return fuel

def secondpart():
    minfuel=2**32
    for pos in _list:
        fuel=0
        for pos2 in _list:
            fuel+=abs(pos2-pos)*(abs(pos2-pos)+1)/2
        if fuel<minfuel:
            minfuel=fuel
    return round(minfuel)

print(firstpart())
print(secondpart())