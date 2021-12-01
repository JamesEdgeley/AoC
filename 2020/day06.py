_list=list(open("day06.txt").read().split('\n\n'))

def firstpart():
    count=0
    for group in _list:
        questions=[]
        for char in group:
            questions.append(char)
        uniques=set(questions)
        uniques.discard('\n')
        count+=len(uniques)
    return count

print(firstpart())

def secondpart():
    count=0
    for group in _list:
        individuals=group.splitlines()
        for char in individuals[0]:
            if group.count(char)==len(individuals):
                count+=1
    return count

print(secondpart())