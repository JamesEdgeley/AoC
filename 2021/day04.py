_guesses=list(map(int,open("day04.txt").read().splitlines()[0].split(',')))
_boards = list(open("day04.txt").read().split("\n\n")[1:])
boards=[[[int(cell) for cell in line.split()] for line in board.splitlines()] for board in _boards]


def checkoff(guess,marks):
    for i,board in enumerate(boards):
        for line in board:
            if guess in line:
                marks[i].append((board.index(line),line.index(guess)))


def checkcomplete(mark):
    for num in range(5):
        for dim in range(2):
            count=0
            for coords in mark:
                if coords[dim]==num:
                    count+=1
                    if count==5:
                        return True
                
def sumunchecked(board,mark):
    sum=0
    for line in board:
        for guess in line:
            if (board.index(line),line.index(guess)) not in mark:
                sum +=guess
    return sum


def firstpart():
    marks=[[] for board in boards]
    for guess in _guesses:
        checkoff(guess,marks)
        for i,mark in enumerate(marks):
            if checkcomplete(mark):
                return guess*sumunchecked(boards[i],mark)

def secondpart():
    marks=[[] for board in boards]
    winners=[]
    for guess in _guesses:
        checkoff(guess,marks)
        for i,mark in enumerate(marks):
            if i in winners:
                continue
            if checkcomplete(mark):
                lastscore=guess*sumunchecked(boards[i],mark)
                winners.append(i)
    return lastscore

print(firstpart())
print(secondpart())