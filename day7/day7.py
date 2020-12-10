with open('input.txt') as f:
    lines = f.read().splitlines()

def makeBagDict(lines):
    bagDict = {}
    for bag in lines:
        sBags = bag.split("contain")
        content = sBags[1].split(", ")
        cBags = ()
        for cBag in content:
            name = " ".join(cBag.strip().split(" ")[1:-1])
            if cBag.strip().split(" ")[0] != "no":
                num = int(cBag.strip().split(" ")[0])
                cBags = cBags + ((num, name),)
        bagDict[" ".join(sBags[0].strip().split(" ")[:-1])] = cBags
    return bagDict


bagDict = makeBagDict(lines)

def getBags(bagName):
    outKeys = []
    for key, value in bagDict.items():
        for bag in value:
            if bag[1] == bagName:
                outKeys.append(key)
    return outKeys

def getNumBags(bagDict):
    bags = []
    bagsToDo = ["shiny gold"]
    while len(bagsToDo) > 0:
        curBag = bagsToDo.pop(0)
        outputBags = getBags(curBag)
        bags = bags + outputBags
        bagsToDo = bagsToDo + outputBags
    return len(set(bags))

print(getNumBags(bagDict))

def countBags(bagName):
    return sum(num * (1 + countBags(childBag)) for num, childBag in bagDict[bagName])

print(countBags("shiny gold"))