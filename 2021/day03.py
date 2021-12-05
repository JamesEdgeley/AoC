_list=list(open("day03.txt").read().splitlines())

def firstpart():
    sum = [0]*len(_list[0])
    for line in _list:
        for i,char in enumerate(line):
            sum[i]+=int(char)
    sum=[1 if val>len(_list)/2 else 0 for val in sum]
    gamma=int("".join(str(val) for val in sum),2)
    epsilon=2**len(sum)-gamma-1
    return gamma * epsilon

print(firstpart())

def filter(list,j,mostorleast):
    if len(list)==1:
        return int(list[0],2)
    else:
        sum=0
        for line in list:
            sum+=int(line[j])
        mostcommon=1 if sum>=len(list)/2 else 0
        leastcommon=1 if sum<len(list)/2 else 0
        common=mostcommon if mostorleast else leastcommon
        newlist=[]
        for line in list:
            if int(line[j])==common:
                newlist.append(line)
        return filter(newlist,j+1,mostorleast)

        

def secondpart():
    o2=filter(_list,0,True)
    co2=filter(_list,0,False)
    return o2*co2

print(secondpart())