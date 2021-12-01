_list=list(open("day25.txt").read().splitlines())
key1=int(_list[0])
key2=int(_list[1])

def modInverse(a, m): 
    m0 = m 
    y = 0
    x = 1
    if (m == 1): 
        return 0
    while (a > 1): 
        q = a // m 
        t = m 
        m = a % m 
        a = t 
        t = y 
        y = x - q * y 
        x = t 
    if (x < 0): 
        x = x + m0 
    return x

def transform(subjectnumber,loopnumber):
    value=1
    for i in range(loopnumber):
        value=(value*subjectnumber)%20201227
    return value

def firstpart():
    x=key1
    u=modInverse(7,20201227)
    loop=1
    while x!=7:
        x=(x*u)%20201227
        loop+=1
    y=key2
    return transform(y,loop)
print(firstpart())