from collections import Counter
from copy import deepcopy

EMPTY = 'L'
OCCUPIED = '#'

seats = []
with open('input.txt') as fp:
    line = fp.readline()
    while line:
        seats.append(list(line.strip()))
        line = fp.readline()


def printSeats(seats):
    for rowStr in seats:
        print(''.join(rowStr))


def getAdjacentNeighbors(grid, x, y):
    neighbors = []
    rows, cols = len(grid[0]), len(grid)
    if x > 0:
        neighbors.append(grid[x-1][y])
        if y > 0:
            neighbors.append(grid[x-1][y-1])
        if y < rows - 1:
            neighbors.append(grid[x-1][y+1])
    if x < cols-1:
        neighbors.append(grid[x+1][y])
        if y > 0:
            neighbors.append(grid[x+1][y-1])
        if y < rows - 1:
            neighbors.append(grid[x+1][y+1])
    if y > 0:
        neighbors.append(grid[x][y-1])
    if y < rows - 1:
        neighbors.append(grid[x][y+1])
    return Counter(neighbors)


def getVisibleOccupied(seats, x, y):
    count = 0
    dirs = [
        (-1, -1), (-1, 0), (-1, 1),
        (0,  -1),          (0,  1),
        (1,  -1), (1,  0), (1, 1)
    ]
    for (dx, dy) in dirs:
        nx, ny = (x+dx, y+dy)
        while ((0 <= nx <= len(seats)-1) and
               (0 <= ny <= len(seats[0])-1)):
            if seats[nx][ny] == EMPTY:
                break
            if seats[nx][ny] == OCCUPIED:
                count += 1
                break
            nx, ny = (nx+dx, ny+dy)
    return count


def applyStep(seats, isPart1):
    newSeats = deepcopy(seats)
    didChange = False
    for row in range(len(seats)):
        for col in range(len(seats[row])):
            seat = seats[row][col]

            numOccupied = getAdjacentNeighbors(seats, row, col)[
                OCCUPIED] if isPart1 else getVisibleOccupied(seats, row, col)

            if seat == EMPTY and numOccupied == 0:
                newSeats[row][col] = OCCUPIED
                didChange = True
            elif seat == OCCUPIED and (isPart1 and numOccupied >= 4 or (not isPart1 and numOccupied >= 5)):
                newSeats[row][col] = EMPTY
                didChange = True
    return (newSeats, didChange)


def getNumOccupied(seats):
    count = 0
    for row in range(len(seats)):
        for col in range(len(seats[row])):
            if seats[row][col] == OCCUPIED:
                count += 1
    return count


isPart1 = False
step = 0
currSeats = deepcopy(seats)

while step < 100:
    currSeats, didChange = applyStep(currSeats, isPart1)
    if didChange == False:
        if isPart1:
            print('Part 1')
        else:
            print('Part 2')
        print(getNumOccupied(currSeats))
        break
    step += 1
