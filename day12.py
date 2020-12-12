_list=list(open("day12.txt").read().splitlines())

def firstpart():
    longitude=0
    latitude=0
    directions=((1,0),(0,1),(-1,0),(0,-1))
    direction=0
    for line in _list:
        action=line[0]
        integer=int(line[1:])
        if action=='N':
            latitude+=integer
        if action=='S':
            latitude-=integer
        if action=='E':
            longitude+=integer
        if action=='W':
            longitude-=integer
        if action=='L':
            direction+=integer//90
            direction=direction%4
        if action=='R':
            direction-=integer//90
            direction=direction%4
        if action=='F':
            longitude+=directions[direction][0]*integer
            latitude+=directions[direction][1]*integer
    return abs(latitude) + abs(longitude)

print(firstpart())

def secondpart():
    wplongitude=10
    wplatitude=1
    longitude=0
    latitude=0
    for line in _list:
        action=line[0]
        integer=int(line[1:])
        if action=='N':
            wplatitude+=integer
        if action=='S':
            wplatitude-=integer
        if action=='E':
            wplongitude+=integer
        if action=='W':
            wplongitude-=integer
        if action=='L':
            wpdirections=((wplongitude,wplatitude),(-wplatitude,wplongitude),(-wplongitude,-wplatitude),(wplatitude,-wplongitude))
            direction=(integer//90)%4
            wplongitude=wpdirections[direction][0]
            wplatitude=wpdirections[direction][1]
        if action=='R':
            wpdirections=((wplongitude,wplatitude),(wplatitude,-wplongitude),(-wplongitude,-wplatitude),(-wplatitude,wplongitude))
            direction=(integer//90)%4
            wplongitude=wpdirections[direction][0]
            wplatitude=wpdirections[direction][1]
        if action=='F':
            longitude+=wplongitude*integer
            latitude+=wplatitude*integer
    return abs(latitude) + abs(longitude)

print(secondpart())