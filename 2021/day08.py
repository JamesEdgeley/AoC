_lines=list(open("day08.txt").read().splitlines())
_outputs=[line.split(" | ")[1] for line in _lines]
_inputs=[line.split(" | ")[0] for line in _lines]

def firstpart():
    count = 0
    for output in _outputs:
        digits = output.split(" ")
        for digit in digits:
            if len(digit) in [2,3,4,7]:
                count+=1
    return count

def decode(input):
    digitdict={}
    input=input.split(' ')
    for digit in input:
        if len(digit)==2:
            digitdict[1]=digit
        if len(digit)==3:
            digitdict[7]=digit
        if len(digit)==4:
            digitdict[4]=digit
        if len(digit)==7:
            digitdict[8]=digit
    for digit in input:
        if len(digit)==6 and any(char not in digit for char in digitdict[1]):
            digitdict[6]=digit
            break

    for digit in input:
        if len(digit)==6 and any(char not in digit for char in digitdict[4]) and digit not in digitdict.values():
            digitdict[0]=digit
            break

    for digit in input:
        if len(digit)==6 and digit not in digitdict.values():
            digitdict[9]=digit
            break

    for digit in input:
        if len(digit)==5 and all(char in digitdict[6] for char in digit):
            digitdict[5]=digit
            break

    for digit in input:
        if len(digit)==5 and all(char in digitdict[9] for char in digit) and digit not in digitdict.values():
            digitdict[3]=digit
            break

    for digit in input:
        if len(digit)==5 and digit not in digitdict.values():
            digitdict[2]=digit
            break
    return digitdict



def secondpart():
    sum=0
    for i,input in enumerate(_inputs):
        digitdict=decode(input)
        codedict={}
        for k,v in digitdict.items():
            codedict["".join(sorted(v))]=k
        
        sortedoutput=["".join(sorted(output)) for output in _outputs[i].split(" ")]
        number=[codedict[word] for word in sortedoutput]
        sum+=int("".join(map(str,number)))
            
    return sum

print(firstpart())

print(secondpart())