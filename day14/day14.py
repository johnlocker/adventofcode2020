with open('input.txt') as f:
	lines = f.read().splitlines()

import re
import itertools
    
def memSum(lines):
    def applyMask(val, bitChange):
        valBit = f'{val:036b}'
        for bc in bitChange:
            index = 35 - bc[1]
            valBit = valBit[:index] + bc[0] + valBit[index + 1:]
        return int(valBit, 2)
    mem = {}
    for line in lines:
        if "mask" in line:
            bitmask = line.split(" = ")[1]
            bitChange = [(bitmask[::-1][i], i) for i in range(len(bitmask)) if bitmask[::-1][i] != "X"]
        else:
            lineSplit = line.split(" = ")
            val = int(lineSplit[1])
            pos = int(re.search('\[(.*)\]', lineSplit[0]).group(1))
            newVal = applyMask(val, bitChange)
            mem[pos] = newVal
            
    return sum([mVal for mVal in mem.values()])
    
print(memSum(lines))

def memSum2(lines):
    def getAddresses(pos, bitmask):
        posBit = f'{pos:036b}'
        for i in range(len(bitmask)):
            index = 35 - i
            if bitmask[::-1][i] != "0":
                posBit = posBit[:index] + bitmask[::-1][i] + posBit[index + 1:]
        lst = list(map(list, itertools.product([0, 1], repeat=posBit.count("X"))))
        memAddresses = []
        for comb in lst:
            repBit = posBit
            for c in comb:
                repBit = repBit.replace("X", str(c), 1)
            memAddresses.append(int(repBit, 2))  
        return memAddresses
    mem = {}
    for line in lines:
        if "mask" in line:
            bitmask = line.split(" = ")[1]
        else:
            lineSplit = line.split(" = ")
            val = int(lineSplit[1])
            pos = int(re.search('\[(.*)\]', lineSplit[0]).group(1))
            memPos = getAddresses(pos, bitmask)
            for mPos in memPos:
                mem[mPos] = val

    return sum([mVal for mVal in mem.values()])
    
print(memSum2(lines))