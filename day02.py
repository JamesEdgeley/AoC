_list=list(open("day02.txt").read().splitlines())

def firstpart():
    validcount=0
    for line in _list:
        password=line.split(': ')[1]
        criterion=line.split(': ')[0]
        letter=criterion.split(' ')[1]
        number=criterion.split(' ')[0]
        lower=int(number.split('-')[0])
        upper=int(number.split('-')[1])
        count=password.count(letter)
        if count<=upper and count>=lower:
            validcount+=1
    return validcount

print(firstpart())

def secondpart():
    validcount=0
    for line in _list:
        password=line.split(': ')[1]
        criterion=line.split(': ')[0]
        letter=criterion.split(' ')[1]
        number=criterion.split(' ')[0]
        lower=int(number.split('-')[0])
        upper=int(number.split('-')[1])
        if len(password)>=upper:
            if (password[lower-1] == letter) ^ (password[upper-1] == letter):
                validcount+=1
    return validcount

print(secondpart())