
fp = open('input.txt')
active = set()

for row, line in enumerate(fp):
    for col, cubeStr in enumerate(line.strip()):
        if cubeStr == '#':
            active.add((row, col, 0, 0))


def getRangeBounds() -> list:
    result = []
    for dim in range(4):
        low = min(cube[dim] for cube in active) - 1
        high = max(cube[dim] for cube in active) + 2
        result.append((low, high))
    return result


def getNeighbors(x, y, z, w) -> list:
    result = []
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dz in range(-1, 2):
                for dw in range(-1, 2):
                    if not (dx == dy == dz == dw == 0):
                        result.append((x + dx, y + dy, z + dz, w + dw))
    return result


def getLiveNeighborCount(x, y, z, w) -> int:
    count = 0
    for pos in getNeighbors(x, y, z, w):
        if pos in active:
            count += 1
    return count


def simCycle() -> set:
    newActive = set()
    ranges = getRangeBounds()
    xr, yr, zr, wr = ranges[0], ranges[1], ranges[2], ranges[3]
    for x in range(xr[0], xr[1]):
        for y in range(yr[0], yr[1]):
            for z in range(zr[0], zr[1]):
                for w in range(wr[0], wr[1]):
                    n = getLiveNeighborCount(x, y, z, w)
                    if (x, y, z, w) in active and (n == 2 or n == 3) or n == 3:
                        newActive.add((x, y, z, w))
    return newActive


for i in range(6):
    active = simCycle()

print(f'Part 2 \n{len(active)}')
