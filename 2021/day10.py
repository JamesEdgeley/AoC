_lines=list(open("day10.txt").read().splitlines())

_dict={"(":")","[":"]","{":"}","<":">"}
_scores={")":3,"]":57,"}":1197,">":25137}   
_scores2={")":1,"]":2,"}":3,">":4}

def firstpart():
    lines = [line for line in _lines]
    score=0
    for line in lines:
        stack=[]
        for char in line:
            if char not in [")","]","}",">"]:
                stack.append(char)
            elif char==_dict[stack[-1]]:
                stack.pop()
            else:
                score+=_scores[char]
                break
    return score

def secondpart():
    lines = [line for line in _lines]
    incomplete=[]
    scores=[]
    for line in lines:
        score=0
        stack=[]
        corrupted=False
        for char in line:
            if char not in [")","]","}",">"]:
                stack.append(char)
            elif char==_dict[stack[-1]]:
                stack.pop()
            else:
                corrupted=True
                break
        if not corrupted:
            for close in [_dict[open] for open in stack[::-1]]:
                score=score*5+_scores2[close]
            scores.append(score)
    medianscore=sorted(scores)[len(scores)//2]
    return medianscore

print(firstpart())
print(secondpart())