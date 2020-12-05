_dict=open("day5.txt").read()

def firstpart():
    code='FBLR'
    binary='0101'
    translation=_dict.maketrans(code,binary)
    lines=list(_dict.translate(translation).splitlines())
    lines.sort(reverse=True)
    return int(lines[0],2)

print(firstpart())

def secondpart():
    code='FBLR'
    binary='0101'
    translation=_dict.maketrans(code,binary)
    lines=list(_dict.translate(translation).splitlines())
    lines.sort(reverse=True)
    for i in range(0,len(lines)):
        if lines[i][-1]==lines[i+1][-1]:
            return int(lines[i],2)-1

print(secondpart())
