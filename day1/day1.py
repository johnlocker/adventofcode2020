with open('input.txt') as f:
    lines = f.read().splitlines()
    nums = [int(x) for x in lines]

def day1a(nums):
    if len(nums) == 0:
        return -1
    tarNum = nums.pop(0)
    for num in nums:
        if tarNum + num == 2020:
            return num * tarNum
    return day1a(nums)

print(day1a(nums))

with open('input.txt') as f:
    lines = f.read().splitlines()
    nums = [int(x) for x in lines]

from itertools import combinations

def day1b(nums):
    for i in combinations(nums, 3):
        if i[0] + i[1] + i[2] == 2020:
            return i[0] * i[1] * i[2]
print(day1b(nums))
