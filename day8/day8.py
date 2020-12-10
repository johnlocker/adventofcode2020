with open('input.txt') as f:
    lines = f.read().splitlines()

def calcAccumulator(lines):
    pointer = 0
    visited = []
    accum = 0
    while pointer not in visited:
        visited.append(pointer)
        ins = lines[pointer]
        insSp = ins.split(" ")
        if insSp[0] == "acc":
            accum += int(insSp[1])
            pointer += 1
        elif insSp[0] == "jmp":
            pointer += int(insSp[1])
        elif insSp[0] == "nop":
            pointer += 1
    return accum
print(calcAccumulator(lines))

def calcAccumulatorFixed(lines):
    switchIdx = [i for i in range(len(lines)) if "jmp" in lines[i] or "nop" in lines[i]]
    for sIdx in switchIdx:
        testLines = lines.copy()
        if "nop" in testLines[sIdx]:
            testLines[sIdx] = testLines[sIdx].replace("nop", "jmp")
        else:
            testLines[sIdx] = testLines[sIdx].replace("jmp", "nop")
        pointer = 0
        visited = []
        accum = 0
        while pointer not in visited and pointer != len(testLines):
            visited.append(pointer)
            ins = testLines[pointer]
            insSp = ins.split(" ")
            if insSp[0] == "acc":
                accum += int(insSp[1])
                pointer += 1
            elif insSp[0] == "jmp":
                pointer += int(insSp[1])
            elif insSp[0] == "nop":
                pointer += 1
        if pointer == len(testLines):
            print("found instruction!")
            print("switch instruction: " + str(sIdx))
            print(accum)
            break
print(calcAccumulatorFixed(lines))
