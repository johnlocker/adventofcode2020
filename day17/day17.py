with open('input.txt') as f:
	lines = f.read().splitlines()

import numpy as np

def sim3dPocket(lines):
    pocket = np.full((len(lines), len(lines[0])), ".")
    for i, line in enumerate(lines):
        pocket[i, ] = list(line)
    pocket = np.expand_dims(pocket, axis = 0)

    def getNeighbours(z, x, y, pocket):
        nList = [-1, 0, 1]
        combs = list(((ll, il, l) for ll in nList for il in nList for l in nList))
        combs.remove((0, 0, 0))
        validCombs = []
        for comb in combs:
            if not (z + comb[0] < 0 or z + comb[0] > pocket.shape[0] - 1 or 
            x + comb[1] < 0 or x + comb[1] > pocket.shape[1] - 1 or
            y + comb[2] < 0 or y + comb[2] > pocket.shape[2] - 1):
                validCombs.append((z + comb[0], x + comb[1], y + comb[2]))
        neighbors = [pocket[nComb[0], nComb[1], nComb[2]] for nComb in validCombs]
        return neighbors


    nCycles = 6
    for cycle in range(nCycles):
        pocketExt = np.full((pocket.shape[0] + 2, pocket.shape[1] + 2, pocket.shape[2] + 2), ".")
        pocketExt[1:pocket.shape[0] + 1, 1:pocket.shape[1] + 1, 1:pocket.shape[2] + 1] = pocket
        pocket = pocketExt.copy()
        newPocket = pocket.copy()
        for iZ in range(pocket.shape[0]):
            for iX in range(pocket.shape[1]):
                for iY in range(pocket.shape[2]):
                    active = pocket[iZ, iX, iY] == "#"
                    neighbors = getNeighbours(iZ, iX, iY, pocket)
                    if active:
                        if neighbors.count("#") not in [2, 3]:
                            newPocket[iZ, iX, iY] = "."
                    else:
                        if neighbors.count("#") == 3:
                            newPocket[iZ, iX, iY] = "#"
        pocket = newPocket.copy()


    print("active state:", sum(sum(sum(pocket == "#"))))

print(sim3dPocket(lines))

def sim4dPocket(lines):
    def getNeighbours2(w, z, x, y, pocket):
        nList = [-1, 0, 1]
        combs = list(((ll, il, l, wl) for ll in nList for il in nList for l in nList for wl in nList))
        combs.remove((0, 0, 0, 0))
        validCombs = []
        for comb in combs:
            if not (w + comb[0] < 0 or w + comb[0] > pocket.shape[0] - 1 or 
            z + comb[1] < 0 or z + comb[1] > pocket.shape[1] - 1 or
            x + comb[2] < 0 or x + comb[2] > pocket.shape[2] - 1 or
            y + comb[3] < 0 or y + comb[3] > pocket.shape[3] - 1):
                validCombs.append((w + comb[0], z + comb[1], x + comb[2], y + comb[3]))
        neighbors = [pocket[nComb[0], nComb[1], nComb[2], nComb[3]] for nComb in validCombs]
        return neighbors

    nCycles = 6
    pocket = np.full((len(lines), len(lines[0])), ".")
    for i, line in enumerate(lines):
        pocket[i, ] = list(line)
    pocket = np.expand_dims(pocket, axis = 0)
    pocket = np.expand_dims(pocket, axis = 0)

    for cycle in range(nCycles):
        pocketExt = np.full((pocket.shape[0] + 2, pocket.shape[1] + 2,
                        pocket.shape[2] + 2, pocket.shape[3] + 2), ".")
        pocketExt[1:pocket.shape[0] + 1, 1:pocket.shape[1] + 1, 1:pocket.shape[2] + 1, 1:pocket.shape[3] + 1] = pocket
        pocket = pocketExt.copy()
        newPocket = pocket.copy()
        for iZ in range(pocket.shape[0]):
            for iW in range(pocket.shape[1]):
                for iX in range(pocket.shape[2]):
                    for iY in range(pocket.shape[3]):
                        active = pocket[iZ, iW, iX, iY] == "#"
                        neighbors = getNeighbours2(iZ, iW, iX, iY, pocket)
                        if active:
                            if neighbors.count("#") not in [2, 3]:
                                newPocket[iZ, iW, iX, iY] = "."
                        else:
                            if neighbors.count("#") == 3:
                                newPocket[iZ, iW, iX, iY] = "#"
        pocket = newPocket.copy()

    print("active state:", sum(sum(sum(sum(pocket == "#")))))

print(sim4dPocket(lines))