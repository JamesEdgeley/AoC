_list=[int(char) for char in open("day23.txt").read()]
input=_list.copy()
def firstpart():
    for i in range(100):
        pickedup=input[1:4]
        input=[x for x in input if x not in pickedup]
        destination=input[0]-1
        if destination==0:
                destination=9
        while destination in pickedup:
            destination-=1
            if destination==0:
                destination=9
        index=input.index(destination)+1
        input[index:index]=pickedup
        input=input[1:]+input[:1]

    index=input.index(1)
    print(input[index:]+input[:index])

def secondpart():
    input=_list.copy()
    _dict={}
    number=1000000
    for cup in range(1,number+1):
        if cup==number:
            _dict[cup]=input[0]
        elif cup<len(input):
            _dict[input[cup-1]]=input[cup]
        elif cup==len(input):
            _dict[input[cup-1]]=cup+1
        else:
            _dict[cup]=cup+1

    start=input[0]
    for i in range(10000000):
        picked1=_dict[start]
        picked2=_dict[picked1]
        picked3=_dict[picked2]

        destination=start
        while True:
            destination-=1
            if destination==0:
                destination=number
            if destination not in [picked1,picked2,picked3]:
                break

        _dict[start]=_dict[picked3]
        _dict[picked3]=_dict[destination]
        _dict[destination]=picked1
        start=_dict[start]

    return _dict[1]*_dict[_dict[1]]

print(secondpart())

