with open('input.txt') as f:
    lines = f.read().splitlines()

def getYesSum(lines):
    answers = ""
    answerCount = 0
    for line in lines:
        if line != "":
            answers += line
        else:
            answerCount += len(set(answers))
            answers = ""
    answerCount += len(set(answers))
    return answerCount
print(getYesSum(lines))

def getYesSum2(lines):
    answerList = []
    groupList = []
    for line in lines:
        if line != "":
            answerList.append(line)
        else:
            groupList.append(answerList)
            answerList = []
    groupList.append(answerList)
    def groupCount(group):
        answerCount = 0
        letters = list(map(chr, range(97, 123))) 
        for let in letters:
            count = 0
            for g in group:
                if let in g:
                    count += 1
            if count == len(group):
                answerCount += 1
        return answerCount
    return sum([groupCount(l) for l in groupList])
print(getYesSum2(lines))