with open('input.txt') as f:
    lines = f.read().splitlines()

def checkPasspord(lines):
    pList = []
    pDict = {} 
    for line in lines:
        if line != '':
            for sLine in line.split(" "):
                pDict[sLine.split(":")[0]] = sLine.split(":")[1]
        else:
            pList.append(pDict)
            pDict =  {}
    pList.append(pDict)
    check = [dic.keys() >= {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"} for dic in pList]
    return sum(check)

print(checkPasspord(lines))

def checkPasspord2(lines):
    pList = []
    pDict = {} 
    for line in lines:
        if line != '':
            for sLine in line.split(" "):
                pDict[sLine.split(":")[0]] = sLine.split(":")[1]
        else:
            pList.append(pDict)
            pDict =  {}
    pList.append(pDict)
    count = 0
    for dic in pList:
        if dic.keys() >= {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}:
            valid = True
            for key, val in dic.items():
                if key == "byr":
                    if int(val) < 1920 or int(val) > 2002:
                        valid = False
                if key == "iyr":
                    if int(val) < 2010 or int(val) > 2020:
                        valid = False
                if key == "eyr":
                    if int(val) < 2020 or int(val) > 2030:
                        valid = False
                if key == "hgt":
                    if val[-2:] == "cm":
                        if int(val[:-2]) < 150 or int(val[:-2]) > 193:
                            valid = False
                    elif val[-2:] == "in":
                        if int(val[:-2]) < 59 or int(val[:-2]) > 76:
                            valid = False
                    else:
                        valid = False
                if key == "hcl":
                    if val[0] != "#" or len(val[1:]) != 6:
                        valid = False
                if key == "ecl":
                    if val not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                        valid = False
                if key == "pid":
                    if len(val) != 9:
                        valid = False
            count += valid
    return count

print(checkPasspord2(lines))