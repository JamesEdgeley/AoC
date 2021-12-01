import re
_list=list(open("day04.txt").read().split('\n\n'))

def firstpart():
    count=0
    for line in _list:
        if line.count(':') == 8 or line.count(':') == 7 and line.count('cid') != 1:
           count+=1
    return count

print(firstpart())

def secondpart():
    count=0
    for line in _list:
        if line.count(':') == 8 or line.count(':') == 7 and line.count('cid') != 1:
            attributes=line.split()
            attributes.sort()
            if len(attributes)==8:  
                attributes.pop(1)

            byr=attributes[0].split(':')[1]
            ecl=attributes[1].split(':')[1]
            eyr=attributes[2].split(':')[1]
            hcl=attributes[3].split(':')[1]
            hgt=attributes[4].split(':')[1]
            iyr=attributes[5].split(':')[1]
            pid=attributes[6].split(':')[1]

            if (ecl in('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth') and
            re.search(r'^#(?:[0-9a-f]{3}){1,2}$', hcl) and
            re.search(r'^[0-9]{9}$',pid) and
            re.search(r'^(59|6[0-9]|7[0-6])in|1([5-8][0-9]|9[0-3])cm$',hgt) and
            re.search(r'^(19[2-9][0-9])|200[0-2]',byr) and
            re.search(r'^(201[0-9])|2020',iyr) and
            re.search(r'^(202[0-9])|2030',eyr)):
                count+=1
    return count

print(secondpart())