_list=list(open("day7.txt").read().splitlines())

def findparents(parents,colour):
    for line in _list:
        splitline=line.split(' bags contain ')
        if colour in splitline[1]:
            parent=splitline[0]
            parents.add(parent)
            findparents(parents,parent)
    return parents

def findchildren(colour):
    count=0
    for line in _list:
        splitline=line.split(' bags contain ')
        if colour==splitline[0]:
            if splitline[1]=='no other bags.':
                return count
            else:
                children=splitline[1].split(', ')
                for child in children:
                    count+=int(child[0])
                    childcolour=child.split(' ')[1]+' '+child.split(' ')[2]
                    count+=int(child[0])*findchildren(childcolour)
            return count


def firstpart():
    outers=set()
    findparents(outers,'shiny gold')
    return len(outers)

print(firstpart())

def secondpart():
    return findchildren('shiny gold')
    
print(secondpart())