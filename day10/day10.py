with open('input.txt') as f:
    lines = f.read().splitlines()
    nums = [int(num) for num in lines]

import numpy as np
from itertools import combinations
def getJoltDiff(nums):
    nums.sort()
    nums = [0] + nums + [max(nums) + 3]
    numsDiff = np.diff(nums)
    return sum(numsDiff == 1) * sum(numsDiff == 3)

print(getJoltDiff(nums))

def getCombinations(nums):
    nums.sort()
    nums = [0] + nums + [max(nums) + 3]
    def checkArrange(checkNums):
        return all([val > 0 and val <= 3 for val in np.diff(checkNums)])

    checkNumsDiff = np.diff(nums)

    splits = [i for i in range(len(checkNumsDiff)) if checkNumsDiff[i] == 3]
    splits = [-1] + splits + [len(checkNums)]

    def getValidCombs(numSet):
        if len(numSet) == 1:
            return [numSet]
        numSets = []
        first = [numSet[0]]
        last = [numSet[len(numSet) - 1]]
        inner = np.array(numSet[1:-1])
        if checkArrange(first + last):
            numSets += [first + last]
        for cN in range(1, len(inner) + 1):
            combs = list(combinations(inner, cN))
            for c in combs:
                innerL = [n for n in c]
                cSet = first + innerL + last
                if checkArrange(cSet):
                    numSets.append(cSet)
        return numSets

    outputSets = []
    for i in range(1, len(splits)):
        curSplit = splits[i - 1:i+1]
        numSet = nums[curSplit[0]+1:curSplit[1] + 1]
        outputSets.append(getValidCombs(numSet))

    lens = [len(s) for s in outputSets]
    result = 1
    for x in lens:
        result *= x
    return result

print(getCombinations(nums))
