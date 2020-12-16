with open('input.txt') as f:
	lines = f.read().splitlines()

def calcErrorRate(lines):
    data = "rules"
    rules = []
    nearTicket = []
    for line in lines:
        if line == "":
            continue
        if line == "your ticket:":
            data = "ticket"
            continue
        if line == "nearby tickets:":
            data = "nearTicket"
            continue
        if data == "rules":
            rules.append(line)
        if data == "ticket":
            ticket = line
        if data == "nearTicket":
            nearTicket.append(line)

    rulesList = []
    fields = {}
    def getNums(ruleSeg): 
        minMax = [int(r) for r in ruleSeg.split("-")]
        return list(range(minMax[0], minMax[1] + 1))
    for rule in rules:
        ruleSplit = rule.split(": ")[1].split(" or ")
        nums1 = getNums(ruleSplit[0])
        nums2 = getNums(ruleSplit[1])
        rulesList += nums1 + nums2
        fields[rule.split(": ")[0]] = nums1 + nums2

    adding = []
    validTickets = []
    for nearT in nearTicket:
        validTicket = True
        for num in nearT.split(","):
            if int(num) not in rulesList:
                adding.append(int(num))
                validTicket = False
        if validTicket:
            validTickets.append(nearT)

    print("Error Rate:", sum(adding))
    return fields, validTickets, ticket

fields, validTickets, ticket = calcErrorRate(lines)

def calcMultiplication(fields, validTickets, ticket):
    ticketsLong = []
    for i in range(len(validTickets[0].split(","))):
        ticketCol = []
        for j in range(len(validTickets)):
            ticketCol.append(int(validTickets[j].split(",")[i]))
        ticketsLong.append(ticketCol)

    fieldSeq = {}
    for key, value in fields.items():
        for i, tCol in enumerate(ticketsLong):
            check =  all(num in value for num in tCol)
            if check:
                if key not in fieldSeq.keys():
                    fieldSeq[key] = [i]
                else:
                    fieldSeq[key].append(i)

    fieldList = [""] * len(fieldSeq)

    def getFieldList(fieldSeq, fieldList):
        for key, value in fieldSeq.items():
            if len(value) == 1:
                targetValue = value[0]
                fieldList[targetValue] = key
                break
        for val in fieldSeq.values():
            if targetValue in val:
                val.remove(targetValue)
        if any(len(v) > 0 for v in fieldSeq.values()):
            return getFieldList(fieldSeq, fieldList)
        else:
            return fieldList

    fieldList = getFieldList(fieldSeq, fieldList)
    depIdx = [i for i, field in enumerate(fieldList) if "departure" in field]
    finalNums = [int(tick) for i, tick in enumerate(ticket.split(",")) if i in depIdx]
    res = 1
    for num in finalNums:
        res *= num
    print("Multiplication departure fields:", res)
    return res

res = calcMultiplication(fields, validTickets, ticket)