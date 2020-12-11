def getRow(seq):
    low = 0
    high = 127
    for i in range(0, len(seq)):
        aCode = seq[i]
        if high - low != 1:
            if aCode == 'F':
                high = (high + low) // 2
            elif aCode == 'B':
                low = ((high + low) // 2) + 1
        else:
            if aCode == 'F':
                return low
            elif aCode == 'B':
                return high


def getCol(seq):
    low = 0
    high = 7
    for i in range(0, len(seq)):
        aCode = seq[i]
        if high - low != 1:
            if aCode == 'L':
                high = (high + low) // 2
            elif aCode == 'R':
                low = ((high + low) // 2) + 1
        else:
            if aCode == 'L':
                return low
            elif aCode == 'R':
                return high


def getSeatID(row, col):
    return (row * 8) + col


aFile = open("../inputs/seats.txt")
lines = aFile.readlines()
count = 0
finalID = 0
# part1
for aLine in lines:
    aRow = getRow(aLine[:7])
    aCol = getCol(aLine[-4:])
    anID = getSeatID(aRow, aCol)
    if finalID < anID:
        finalID = anID
print(finalID)

# part2
aMap = {}
for aLine in lines:
    aRow = getRow(aLine[:7])
    aCol = getCol(aLine[-4:])
    anID = getSeatID(aRow, aCol)
    aMap[anID] = anID
for anID in aMap.keys():
    if not((anID + 1) in aMap) and (anID + 2) in aMap:
        print(anID + 1)