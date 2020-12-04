with open('input.txt') as f:
    lines = f.read().splitlines()

import re

def validPasswords(lines):
    pwCount = 0
    for pw in lines:
        res = re.split(': | |-', pw)
        resCount = res[3].count(res[2])
        if resCount >= int(res[0]) and resCount <= int(res[1]):
            pwCount += 1
    return pwCount

print(validPasswords(lines))

def validPasswords2(lines):
    pwCount = 0
    for pw in lines:
        res = re.split(': | |-', pw)
        firstCheck = res[3][int(res[0]) - 1] == res[2]
        secondCheck = res[3][int(res[1]) - 1] == res[2]
        if int(firstCheck) + int(secondCheck) == 1:
            pwCount += 1
    return pwCount

print(validPasswords2(lines))