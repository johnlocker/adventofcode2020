nums = [8,11,0,19,1,2]

def getNum(nums, stopNum = 2020):
    lastNumDict = {}
    turn = 1
    for num in nums[:-1]:
        lastNumDict[num] = turn
        turn += 1
    lastNum = nums[-1]
    for i in range(stopNum - len(nums)):
        if lastNum not in lastNumDict.keys():
            numSpoken = 0
        else:
            numSpoken = turn - lastNumDict[lastNum]
        lastNumDict[lastNum] = turn
        lastNum = numSpoken
        turn += 1
        if i % 10 ** 6 == 0:
            print("Progress: ", round(i / stopNum * 100, 1), "%")

    return lastNum
    
print("This is the last number: ", getNum(nums, stopNum = 2020))

print("This is the last number: ", getNum(nums, stopNum = 30000000))