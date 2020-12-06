with open('input.txt') as f:
    lines = f.read().splitlines()

import math

def getSeatID(bordP):
    rows = list(range(128))
    for char in bordP[:7]:
        if char == "F":
            rows = rows[0:math.ceil(len(rows) / 2)]
        else:
            rows = rows[math.ceil(len(rows) / 2):len(rows)]
    seat = list(range(8))
    for cl in bordP[7:]:
        if cl == "L":
            seat = seat[0:math.ceil(len(seat) / 2)]
        else:
            seat = seat[math.ceil(len(seat) / 2):len(seat)]
    return (rows[0] * 8) + seat[0]

def getMaxID(lines):
    maxID = 0
    for bordP in lines:
        seatID = getSeatID(bordP)
        if seatID > maxID:
            maxID = seatID
    return maxID

print(getMaxID(lines))

import numpy as np

def getSeat(lines):
    seatIDs = []
    for bordP in lines:
        seatIDs.append(getSeatID(bordP))
    seatIDs.sort()
    v = np.diff(seatIDs)
    return seatIDs[[i for i, x in enumerate(v != 1) if x][0]] + 1

print(getSeat(lines))