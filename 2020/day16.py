_list=list(open("day16.txt").read().split('\n\n'))

lines=_list[0].splitlines()
yourticket=_list[1].splitlines()[1].split(',')
nearbytickets=_list[2].splitlines()[1:]
validtickets=[]
lowest=1000
highest=0
ranges={}
for line in lines:
    splitline=line.split(': ')
    field=splitline[0]
    range1,range2 =splitline[1].split(' or ')
    lower1,upper1=range1.split('-')
    lower2,upper2=range2.split('-')
    ranges[field]=[int(lower1),int(upper1),int(lower2),int(upper2)]
    if int(lower1)<lowest:
        lowest=int(lower1)
    if int(upper2)>highest:
        highest=int(upper2)

def firstpart():
    global validtickets
    invalid=0
    for ticket in nearbytickets:
        values=ticket.split(',')
        isvalid=True
        for value in values:
            if int(value)<lowest or int(value)>highest:
                invalid+=int(value)
                isvalid=False
                break
        if isvalid:
            validtickets.append(ticket)
    return invalid

print(firstpart())

def secondpart():
    validindex={}
    for key in ranges.keys():
        validindex[key]=[*range(len(ranges))]
        for ticket in validtickets:
            for index in validindex[key]:
                value=int(ticket.split(',')[index])
                if value<ranges[key][0] or (value>ranges[key][1] and value<ranges[key][2]) or value>ranges[key][3]:
                    validindex[key].remove(index)
    product=1
    while sum(len(validindex[x]) for x in validindex)!= 0:
        for keyi in validindex.keys():
            if len(validindex[keyi])==1:
                index=validindex[keyi][0]
                if keyi.startswith('departure'):
                    product*=int(yourticket[index])
                for keyj in validindex.keys():
                    if index in validindex[keyj]:
                        validindex[keyj].remove(index)
    return product

print(secondpart())

         



    





#firstpart()