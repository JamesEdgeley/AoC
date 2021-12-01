_list=list(open("day08.txt").read().splitlines())
def firstpart():
    acc=0
    i=0
    instructions=[]
    for line in _list:
        op=line.split(' ')[0]
        arg=line.split(' ')[1]
        instructions.append([op,arg])
    
    checked=[]
    while i not in checked:
        checked.append(i)
        if instructions[i][0]=='nop':
            i+=1

        if instructions[i][0]=='acc':
            acc+=int(instructions[i][1])
            i+=1
            
        if instructions[i][0]=='jmp':
            i+=int(instructions[i][1])

    return acc

print(firstpart())

def secondpart():
    
    instructions=[]
    for line in _list:
        op=line.split(' ')[0]
        arg=line.split(' ')[1]
        instructions.append([op,arg,False])

    for i in range(0,len(instructions)):
        j=i
        checked=[]
        while j not in checked:
            checked.append(j)
            if instructions[j][0]=='jmp':
                j+=int(instructions[j][1])
            else:
                j+=1

            if j>=len(instructions) or instructions[j][2]==True:
                instructions[i][2]=True
                break
        
    acc=0
    i=0
    madeedit=False
    while i<len(instructions):
        j=i
        if instructions[j][0]=='nop':
            if madeedit==False and instructions[i+int(instructions[i][1])][2]==True:
                madeedit=True
                i+=int(instructions[j][1])
            else:
                i+=1
            
        if instructions[j][0]=='jmp':
            if madeedit==False and instructions[j+1][2]==True:
                madeedit=True
                i+=1
            else:
                i+=int(instructions[j][1])
    
        if instructions[j][0]=='acc':
            acc+=int(instructions[j][1])
            i+=1

    return acc
    
print(secondpart())