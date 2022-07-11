hex=open("day16.txt").read()
binary=""
for x in hex:
    binary+=bin(int(x,16))[2:].zfill(4)


def packetextract(i=0,versionsum=0):

    version=int(binary[i:i+3],2)
    versionsum+=version
    i+=3
    typeid=int(binary[i:i+3],2)
    i+=3
    if typeid==4:
        leadingbit=int(binary[i],2)
        literal=""
        while leadingbit!=0:
            literal+=binary[i+1:i+5]
            i+=5
            leadingbit=int(binary[i],2)
        literal+=binary[i+1:i+5]
        i+=5    
        result=int(literal,2)
        
    else:
        
        lengthid=int(binary[i],2)
        i+=1
        values=[]
        if lengthid==0:
            
            bitlength=int(binary[i:i+15],2)
            i+=15
            current=i
            while i-current<bitlength:
                i,versionsum,result=packetextract(i,versionsum)
                values.append(result)

        elif lengthid==1:
            
            numsubpackets=int(binary[i:i+11],2)
            i+=11
            subpacketindex=0
            while subpacketindex<numsubpackets:
                i,versionsum,result=packetextract(i,versionsum)
                values.append(result)
                subpacketindex+=1

        if typeid==0:
            result=sum(values)
        elif typeid==1:
            result=1
            for value in values:
                result*=value
        elif typeid==2:
            result=min(values)
        elif typeid==3:
            result=max(values)
        elif typeid==5:
            result=values[0]>values[1]
        elif typeid==6:
            result=values[0]<values[1]
        else:
            result=values[0]==values[1]

    return i,versionsum,result


def firstpart():
    return packetextract()[1]

print(firstpart())

def secondpart():
    return packetextract()[2]

print(secondpart())


