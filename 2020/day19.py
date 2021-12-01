_list=list(open("day19.txt").read().split('\n\n'))

rules=_list[0].splitlines()
messages=_list[1].splitlines()


R={}
for rule in rules:
    lhs=rule.split(': ')[0]
    rhs=rule.split(': ')[1].replace('"','')
    rhs=rhs.split(' | ')
    options=[]
    for branch in rhs:
        options.append([number for number in branch.split(' ')])

    R[lhs]=options
invalidMessageDict = {}

def matchesRuleList(message, ruleList):
        if len(message) < len(ruleList):
                return False
        if len(message) == 0 and len(ruleList) == 0:
                return True
        if len(ruleList) == 0:
                return False
        for i in range(1, len(message) + 1):
                prefix = message[:i]
                firstRule = ruleList[0]
                if matchesRule(prefix, firstRule):
                        if matchesRuleList(message[i:], ruleList[1:]):
                                return True
        return False
 
def matchesRule(message, ruleName):
        if message in invalidMessageDict:
                if ruleName in invalidMessageDict[message]:
                        return False # If we already checked/saved this resut, return early
        options = R[ruleName]
        for option in options:
                if message in option:
                        return True
                if option[0] in ["a","b"]:
                        if message in invalidMessageDict:
                                invalidMessageDict[message].append(ruleName)
                        else:
                                invalidMessageDict[message] = []
                        return False
                if matchesRuleList(message, option):
                        return True
 
        if message in invalidMessageDict:
                invalidMessageDict[message].append(ruleName)
        else:
                invalidMessageDict[message] = []
        return False

R['8']=[['42'],['42','8']]
R['11']=[['42','31'],['42','11','31']]

count=0
for message in messages:
    if matchesRule(message,'0'):
        count+=1

print(count)






