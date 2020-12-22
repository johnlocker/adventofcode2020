with open('input.txt') as f:
	lines = f.read().splitlines()

def getPlayerDic(lines):
    playerDic = {}
    playerName = ""
    for line in lines:
        if "Player" in line:
            playerName = line.split(" ")[1].split(":")[0]
            playerNums = []
            continue
        if playerName != "" and line != "":
            playerNums.append(int(line))
        if line == "":
            playerDic[playerName] = playerNums
            playerName = ""
    playerDic[playerName] = playerNums
    return playerDic

def playGame(playerDic):
    while all([len(v) > 0 for v in playerDic.values() ]):
        p1 = playerDic["1"].pop(0)
        p2 = playerDic["2"].pop(0)
        if p1 > p2:
            playerDic["1"].append(p1)
            playerDic["1"].append(p2)
        else:
            playerDic["2"].append(p2)
            playerDic["2"].append(p1)

    key = [k for k, v in playerDic.items() if len(v) > 0][0]
    mulList = list(range(len(playerDic[key]), 0, -1))
    print(sum([playerDic[key][i] *  mulList[i] for i in range(len(playerDic[key]))]))

print(playGame(getPlayerDic(lines)))

playerDic = getPlayerDic(lines)
playerList = [playerDic["1"], playerDic["2"]]

def playRecCombat(playerList):
    config = []
    while all([len(v) > 0 for v in playerList]):
        curConfig = tuple(playerList[0]) + (0,) + tuple(playerList[1])
        if curConfig in config:
            return True, playerList[0]
        config.append(curConfig)

        p1 = playerList[0].pop(0)
        p2 = playerList[1].pop(0)

        if len(playerList[0]) >= p1 and len(playerList[1]) >= p2:
            copyPlayerList = playerList.copy()
            copyPlayerList = [copyPlayerList[0][:p1], copyPlayerList[1][:p2]]
            p1winner, _ = playRecCombat(copyPlayerList)
        else:
            p1winner = p1 > p2

        if p1winner:
            playerList[0] += [p1, p2]
        else:
            playerList[1] += [p2, p1]
    p1winner = len(playerList[0]) > len(playerList[1])
    return p1winner, playerList[1 - p1winner]

p1winner, winnerList = playRecCombat(playerList)

def score(winnerList):
    mulList = list(range(len(winnerList), 0, -1))
    print(sum([winnerList[i] *  mulList[i] for i in range(len(winnerList))]))

print(score(winnerList))