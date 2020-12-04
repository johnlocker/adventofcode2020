with open('input.txt') as f:
    lines = f.read().splitlines()

def countTrees(lines, xChange, yChange):
    count, curX, curY = 0, 0, 0
    notBottom = True
    bottomLen = len(lines)
    rowLen = len(lines[0])
    while notBottom:
        field = lines[curY][curX]
        if field == "#":
            count += 1
        curX += xChange
        curY += yChange
        if curY >= bottomLen:
            notBottom = False
        if curX >= rowLen:
            curX = curX % rowLen
    return count

print(countTrees(lines, 3, 1))

multiTrees = (countTrees(lines, 1, 1)
    * countTrees(lines, 3, 1)
    * countTrees(lines, 5, 1)
    * countTrees(lines, 7, 1)
    * countTrees(lines, 1, 2))
print(multiTrees)
    
