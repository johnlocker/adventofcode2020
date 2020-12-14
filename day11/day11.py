import numpy as np

with open('input.txt') as f:
	lines = f.read().splitlines()
	layout = np.full((len(lines), len(lines[0])), ".")
	for i in range(len(lines)):
		layout[i,] = [char for char in lines[i]]

def getOccupiedSeats(layout):
	def changeSeat(x, y, layout):
		layoutShape = layout.shape
		if layout[x, y] == ".":
			return "."
		xPos = [x + 1, x, x - 1]
		yPos = [y + 1, y, y - 1]
		pos = []
		for xP in xPos:
			for yP in yPos:
				pos.append((xP, yP))
		def checkPos(pos, x, y, layoutShape):
			output = []
			for p in pos:
				if p[0] == x and p[1] == y:
					continue
				if p[0] < 0 or p[0] >= layoutShape[0]:
					continue
				if p[1] < 0 or p[1] >= layoutShape[1]:
					continue
				output.append(p)
			return output
		checkedPos = checkPos(pos, x, y, layoutShape)
		adjSeats = [layout[cPos[0], cPos[1]]  for cPos in checkedPos]
		if layout[x, y] == "L":
			if "#" not in adjSeats:
				return "#"
			else:
				return "L"
		if layout[x, y] == "#":
			if adjSeats.count("#") >= 4:
				return "L"
			else:
				return "#"

	newLayout = np.full((layout.shape[0], layout.shape[1]), ".")
	oldLayout = layout.copy()
	while True:
		for index, x in np.ndenumerate(oldLayout):
			newLayout[index] = changeSeat(index[0], index[1], oldLayout)
		if (oldLayout == newLayout).all():
			print("occupied seats: ", sum(sum(newLayout == "#")))
			break
		else:
			oldLayout = newLayout.copy()
	return sum(sum(newLayout == "#"))
print(getOccupiedSeats(layout))


def getOccupiedSeats2(layout):
	def changeSeat2(x, y, layout):
		if layout[x, y] == ".":
			return "."
		def getAdjSeats(x, y, layout):
			l = [-1, 0, 1]
			inCrements = []
			for lx in l:
				for ly in l:
					inCrements.append((lx, ly))
			inCrements.remove((0, 0))
			adjOut = []
			for inc in inCrements:
				curPos = [x, y]
				while True:
					curPos[0] += inc[0]
					curPos[1] += inc[1]
					if (curPos[0] < 0 or curPos[0] >= layout.shape[0]
						or curPos[1] < 0 or curPos[1] >= layout.shape[1]):
						adjOut.append(".")
						break
					seat = layout[curPos[0], curPos[1]]
					if seat == "L" or seat == "#":
						adjOut.append(seat)
						break
			return adjOut
		adjSeats = getAdjSeats(x, y, layout)
		if layout[x, y] == "L":
			if "#" not in adjSeats:
				return "#"
			else:
				return "L"
		if layout[x, y] == "#":
			if adjSeats.count("#") >= 5:
				return "L"
			else:
				return "#"
	newLayout = np.full((layout.shape[0], layout.shape[1]), ".")
	oldLayout = layout.copy()
	while True:
		for index, x in np.ndenumerate(oldLayout):
			newLayout[index] = changeSeat2(index[0], index[1], oldLayout)
		if (oldLayout == newLayout).all():
			print("occupied seats: ", sum(sum(newLayout == "#")))
			break
		else:
			oldLayout = newLayout.copy()
	return sum(sum(newLayout == "#"))
	
print(getOccupiedSeats2(layout))