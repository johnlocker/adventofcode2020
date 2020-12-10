with open('input.txt') as f:
    lines = f.read().splitlines()
    nums = [int(num) for num in lines]

import itertools

def makeSums(pre):
    preComb = list(itertools.combinations(pre, 2))
    preSum = [su[0] + su[1] for su in preComb]
    return preSum

def xmasWeak(nums):
    preambleLen = 25
    for i in range(preambleLen, len(nums)):
        pre = nums[(i - preambleLen):i]
        if nums[i] not in makeSums(pre):
            print("This is the number:", nums[i])
            return nums[i]
    
target = xmasWeak(nums)

def encWeak(nums, target):
    for sumLen in range(2, len(nums)):
        for i in range(sumLen, len(nums)):
            if sum(nums[(i - sumLen):i]) == target:
                print("min: ", min(nums[(i - sumLen):i]))
                print("max: ", max(nums[(i - sumLen):i]))
                print("sum: ", min(nums[(i - sumLen):i])
                             + max(nums[(i - sumLen):i]))
                return (min(nums[(i - sumLen):i]) 
                      + max(nums[(i - sumLen):i]))

print(encWeak(nums, target))