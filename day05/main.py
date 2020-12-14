def binarySearchPart1(data: str, leftChar: str, rightChar: str, start: int, end: int) -> int:
    mid = (start + end) // 2
    for letter in data:
        if letter == rightChar:
            start = mid + 1
        elif letter == leftChar:
            end = mid
        mid = (start + end) // 2
    return mid


def binarySearchPart2(sortedLst: list) -> int:
    left = 0
    right = len(sortedLst) - 1
    mid = 0
    while right > left + 1:
        mid = (left + right) // 2
        if (sortedLst[left] - left) != (sortedLst[mid] - mid):
            right = mid
        elif (sortedLst[right] - right) != (sortedLst[mid] - mid):
            left = mid
    return sortedLst[mid] + 1


def calculateSeatID(bPassStr: str):
    strList = list(bPassStr)
    for index, c in enumerate(bPassStr):
        if c == 'B':
            strList[index] = '1'
        elif c == 'F':
            strList[index] = '0'
        elif c == 'R':
            strList[index] = '1'
        elif c == 'L':
            strList[index] = '0'

    return int(''.join(strList), 2)


maxSeatID = -1
seatIDs = []
with open('input.txt') as fp:
    line = fp.readline()
    while line:
        # Binary Search Method
        rowNum = binarySearchPart1(line[:7], 'F', 'B', 0, 127)
        colNum = binarySearchPart1(line[7:], 'L', 'R', 0, 7)
        seatID = rowNum * 8 + colNum

        # Binary String Method
        seatID = calculateSeatID(line)

        seatIDs.append(seatID)
        maxSeatID = max(maxSeatID, seatID)
        line = fp.readline()

seatIDs.sort()
missingID = binarySearchPart2(seatIDs)
print(f'Part 1\n{maxSeatID}\n\nPart 2\n{missingID}')
