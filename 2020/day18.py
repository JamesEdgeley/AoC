_list=list(open("day18.txt").read().splitlines())

def calc1(expr):
    e=expr.split(' ')
    first=int(e[0])
    for i in range(len(e[1:-1])):
        if e[1:][i] == '+':
            first+=int(e[1:][i+1])
        elif e[1:][i] == '*':
            first*=int(e[1:][i+1])
    return first

def calc2(expr):
    e=expr.split(' * ')
    first=calc1(e[0])
    for p in e[1:]:
        first*=calc1(p)
    return first

def split(line,calc):
    if '(' not in line:
        s=calc(line)
        return s,True
    inbracket=False
    for i in range(len(line)):
        if line[i] == '(':
            expr=""
            inbracket=True
        elif line[i] == ')':
            newline=line.replace('('+expr+')',str(calc(expr)))
            inbracket=False
        elif inbracket:
            expr+=line[i]
        else:
            continue
    return newline,False
    

def firstpart():
    sum=0
    for line in _list:
        while split(line,calc1)[1]==False:
            line=split(line,calc1)[0]
        sum+=split(line,calc1)[0]
    return sum

print(firstpart())

def secondpart():
    sum=0
    for line in _list:
        while split(line,calc2)[1]==False:
            line=split(line,calc2)[0]
        sum+=split(line,calc2)[0]
    return sum

print(secondpart())
    