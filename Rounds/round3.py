def slope(list_lines, right, down):
    positionX = 0
    positionY = 0
    count = 0

    while positionY < len(list_lines):
        if list_lines[positionY][positionX] == "#":
            count += 1
        if positionX + right >= 31:
            positionX = positionX + right - 31
        else:
            positionX += right
        positionY += down
    return count


aFile = open("../inputs/map.txt", "r")
lines = aFile.readlines()
totalCount = 1
totalCount *= slope(lines, 1, 1)
totalCount *= slope(lines, 3, 1)
totalCount *= slope(lines, 5, 1)
totalCount *= slope(lines, 7, 1)
totalCount *= slope(lines, 1, 2)

print(totalCount)
