with open('input.txt') as f:
	lines = f.read().splitlines()
import pyparsing

def calcStr(cStr, part2):
    cSp = cStr.split(" ")
    if not part2:
        res = int(cSp[0])
        plus = True
        for c in cSp[1:]:
            if c == "+":
                plus = True
            elif c == "*":
                plus = False
            else:
                if plus:
                    res += int(c)
                else:
                    res *= int(c)
    else:
        count = 0
        while "+" in cSp:
            curA = cSp[count]
            if curA == "+":
                sumRes = int(cSp[count - 1]) + int(cSp[count + 1])
                cSp[count] = sumRes
                for index in sorted([count - 1, count + 1], reverse = True):
                    del cSp[index]
                count = 0
            count += 1
            if count >= len(cSp):
                break
        if len(cSp) == 1:
            return cSp[0]
        res = 1
        for a in cSp:
            if a != "*":
                res *= int(a)
    return res

def findInner(lineList, part2):
    for l in lineList:
        if isinstance(l, list):
            return findInner(l, part2)
    elStr = " ".join(lineList)
    num = str(calcStr(elStr, part2))
    return (num, "(" + elStr + ")")

def calcLine(line, part2 = False):
    thecontent = pyparsing.Word(pyparsing.alphanums) | '+' | '*'
    parens     = pyparsing.nestedExpr( '(', ')', content = thecontent)
    while "(" in line:
        lineList = parens.parseString("(" + line + ")").asList()[0]
        res = findInner(lineList, part2)
        line = line.replace(res[1], res[0])
    final = calcStr(line, part2)
    return final

print("Part1: ", sum([calcLine(line) for line in lines]))
print("Part2: ", sum([calcLine(line, part2 = True) for line in lines]))