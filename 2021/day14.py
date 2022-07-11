_rules=list(open("day14.txt").read().split("\n\n")[1].splitlines())
_base=list(open("day14.txt").read().split("\n\n")[0])


_ruledict={}
_pairsdict={}
for rule in _rules:
    _pairsdict[rule.split(" -> ")[0]]=[rule.split(" -> ")[0][0]+rule.split(" -> ")[1],rule.split(" -> ")[1]+rule.split(" -> ")[0][1]]
    _ruledict[rule.split(" -> ")[0]]=rule.split(" -> ")[1]

def firstpart():
    countdict={}
    countdictcopy={}
    charcount={}
    pairs=[_base[i]+_base[i+1] for i in range(len(_base)-1)]

    for pair in pairs+[value[0] for value in list(_pairsdict.values())]+[value[1] for value in list(_pairsdict.values())]:
        countdict[pair]=0
        countdictcopy[pair]=0
        charcount[pair[0]]=0
    for pair in pairs:
        countdict[pair]+=1
        countdictcopy[pair]+=1

    for step in range(10):
        for k,v in countdict.items():
            if v>0:
                countdictcopy[k]-=v
                countdictcopy[_pairsdict[k][0]]+=v
                countdictcopy[_pairsdict[k][1]]+=v
        for k,v in countdictcopy.items():
            countdict[k]=v
    
    for k,v in countdict.items():
        charcount[k[0]]+=v
    charcount[_base[-1]]+=1

    ranking=sorted(list(charcount.values()))
    return ranking[-1]-ranking[0]

def secondpart():
    countdict={}
    countdictcopy={}
    charcount={}
    pairs=[_base[i]+_base[i+1] for i in range(len(_base)-1)]

    for pair in pairs+[value[0] for value in list(_pairsdict.values())]+[value[1] for value in list(_pairsdict.values())]:
        countdict[pair]=0
        countdictcopy[pair]=0
        charcount[pair[0]]=0
    for pair in pairs:
        countdict[pair]+=1
        countdictcopy[pair]+=1
    for step in range(40):
        for k,v in countdict.items():
            if v>0:
                countdictcopy[k]-=v
                countdictcopy[_pairsdict[k][0]]+=v
                countdictcopy[_pairsdict[k][1]]+=v
        for k,v in countdictcopy.items():
            countdict[k]=v
    
    for k,v in countdict.items():
        charcount[k[0]]+=v
    charcount[_base[-1]]+=1

    ranking=sorted(list(charcount.values()))
    return ranking[-1]-ranking[0]

print(firstpart())
print(secondpart())