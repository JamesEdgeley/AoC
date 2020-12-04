_sum=2020
_list=list(map(int,open("day1.txt").read().splitlines()))

def firstpart(sum):
    for number in _list:
        if sum - number in _list:
         return(number * (sum - number))
         break

print(firstpart(_sum))

def secondpart(sum):
    for number1 in _list:
        subsum = sum - number1
        for number2 in _list:
            if subsum - number2 in _list:
                return number1 * number2 * (subsum-number2)
                break

print(secondpart(_sum))

        