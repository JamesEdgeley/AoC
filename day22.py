_list=list(open("day22.txt").read().split('\n\n'))

hand1=[int(card) for card in _list[0].splitlines()[1:]]
hand2=[int(card) for card in _list[1].splitlines()[1:]]

def firstpart():
    deck1=hand1.copy()
    deck2=hand2.copy()
    while len(deck1)!=0 and len(deck2)!=0:
        if deck1[0]>deck2[0]:
            deck1.append(deck1.pop(0))
            deck1.append(deck2.pop(0))
        else:
            deck2.append(deck2.pop(0))
            deck2.append(deck1.pop(0))
    score=0
    for i in range(0,len(deck1)):
        score+=(i+1)*deck1[::-1][i]
    return(score)

print(firstpart())

def combat(deck1,deck2,toplevel=True):
    previous=set()
    winner=None
    while winner==None:
        if (tuple(deck1),tuple(deck2)) in previous:
            winner=1
            break
        previous.add((tuple(deck1),tuple(deck2)))
        if len(deck1)==0:
            winner=2
            break
        if len(deck2)==0:
            winner=1
            break

        if len(deck1)>deck1[0] and len(deck2)>deck2[0]:
            rwinner=combat(deck1[1:deck1[0]+1],deck2[1:deck2[0]+1],False)
        elif deck1[0]>deck2[0]:
            rwinner=1
        else:
            rwinner=2

        if rwinner==1:
            deck1.append(deck1.pop(0))
            deck1.append(deck2.pop(0))
        else:
            deck2.append(deck2.pop(0))
            deck2.append(deck1.pop(0))

    if toplevel:
        score=0
        for i in range(0,len(deck1)):
            score+=(i+1)*deck1[::-1][i]
        for i in range(0,len(deck2)):
            score+=(i+1)*deck2[::-1][i]
        return score
    else:
        return winner

def secondpart():
    deck1=hand1.copy()
    deck2=hand2.copy()
    return combat(deck1,deck2)

print(secondpart())
