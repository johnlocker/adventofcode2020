with open('input.txt') as f:
	lines = f.read().splitlines()
instructions = [(line[0], int(line[1:])) for line in lines]


def updateState(curState, direct, value):
    if direct == "E":
        curState["WE"] -= value
    if direct == "W":
        curState["WE"] += value
    if direct == "S":
        curState["NS"] -= value
    if direct == "N":
        curState["NS"] += value
    return curState
    
def changeFace(curState, ins):
    curFace = curState["face"]
    steps = int(ins[1] / 90)
    dirs = ["N", "E", "S", "W"]
    turnDirs = dirs + dirs + dirs
    curIndex = dirs.index(curFace) + 4
    if ins[0] == "R":
        curIndex += steps
        return turnDirs[curIndex]
    else:
        curIndex -= steps
        return turnDirs[curIndex]

def calcDistance(curState, instructions):
    for ins in instructions:
        if ins[0] == "F":
            curState = updateState(curState, curState["face"], ins[1])
        if ins[0] in ["N", "S", "E", "W"]:
            curState = updateState(curState, ins[0], ins[1])
        if ins[0] in ["L", "R"]:
            curState["face"] = changeFace(curState, ins)
            
    print("Distance: ", abs(curState["NS"]) + abs(curState["WE"]))
    return abs(curState["NS"]) + abs(curState["WE"])
    
curState = {"NS": 0, "WE": 0, "face": "E"}
print(calcDistance(curState, instructions))

def updateFace(wayState, ins):
    steps = int(ins[1] / 90)
    NS = wayState["NS"]
    WE = wayState["WE"]
    if steps == 1:
        if ins[0] == "R":
            wayState["WE"] = NS * -1
            wayState["NS"] = WE
        else:
            wayState["WE"] = NS
            wayState["NS"] = WE * -1
    if steps == 2:
        wayState["WE"] = WE * -1
        wayState["NS"] = NS * -1
    if steps == 3:
        if ins[0] == "R":
            wayState["WE"] = NS
            wayState["NS"] = WE * -1
        else:
            wayState["WE"] = NS * -1
            wayState["NS"] = WE
    return wayState

def calcDistance2(wayState, shipState, instructions):
    for ins in instructions:
        if ins[0] in ["N", "S", "E", "W"]:
            wayState = updateState(wayState, ins[0], ins[1])
        if ins[0] in ["L", "R"]:
            wayState = updateFace(wayState, ins)
        if ins[0] == "F":
            for fDir in ["NS", "WE"]:
                shipState[fDir] += wayState[fDir] * ins[1]
    print("Distance: ", abs(shipState["NS"]) + abs(shipState["WE"]))
    return abs(shipState["NS"]) + abs(shipState["WE"])

wayState = {"NS": 1, "WE": -10}
shipState = {"NS": 0, "WE": 0}
print(calcDistance2(wayState, shipState, instructions))