_list=list(open("day14.txt").read().splitlines())

def firstpart():
    memory={}
    for line in _list:
        splitline=line.split(' = ')
        if splitline[0] =='mask':
            mask = splitline[1]
        else:
            address=int(splitline[0].split('[')[1][:-1])
            value=int(splitline[1])
            value=f'{value:036b}'
            result=''
            for i in range(36):
                if mask[i]=='X':
                    result+=value[i]
                else:
                    result+=mask[i]
            memory[address]=int(result,2)
            
    return sum(memory.values())
        
print(firstpart())

def secondpart():
    memory={}
    for line in _list:
        splitline=line.split(' = ')
        if splitline[0] =='mask':
            mask = splitline[1]
        else:
            rawaddress=int(splitline[0].split('[')[1][:-1])
            rawaddress=f'{rawaddress:036b}'
            addresses=['']
            for i in range(36):
                if mask[i]=='1':
                    for j in range(len(addresses)):
                        addresses[j]+='1'
                    continue
                if mask[i]=='0':
                    for j in range(len(addresses)):
                        addresses[j]+=rawaddress[i]
                    continue
                else:
                     for j in range(len(addresses)):
                         base=addresses[j]
                         addresses.append(base+'1')
                         addresses[j]+='0'
            value=int(splitline[1])
            for address in addresses:
                memory[address]=value
    return sum(memory.values())

print(secondpart())