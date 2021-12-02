_list=list(open("day02.txt").read().splitlines())

def firstpart():
    depth=0
    pos=0
    for line in _list:
        direction = line.split(' ')[0]
        X = int(line.split(' ')[1])
        if direction == 'forward':
            pos += X
        elif direction == 'up':
            depth -= X
        elif direction =='down':
            depth += X
    return depth * pos

print(firstpart())

def secondpart():
    aim=0
    depth=0
    pos=0
    for line in _list:
        direction = line.split(' ')[0]
        X = int(line.split(' ')[1])
        if direction == 'forward':
            pos += X
            depth += aim * X
        elif direction == 'up':
            aim -= X
        elif direction =='down':
            aim += X
    return depth * pos

print(secondpart())
