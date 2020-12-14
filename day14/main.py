def setBit(value: int, bit: int):  # set to 1
    return value | (1 << bit)


def clearBit(value: int, bit: int):  # set to 0
    return value & ~(1 << bit)


def applyMask(maskStr: str, value: int) -> int:
    result = value
    for i, bitValue in enumerate(maskStr):
        bitIndex = len(maskStr)-1-i

        if bitValue == '0':
            result = clearBit(result, bitIndex)
        elif bitValue == '1':
            result = setBit(result, bitIndex)
    return result


def getDecodedAddrs(maskStr: str, value: int, memAddr: int) -> set:
    initialAddr = memAddr

    for i in range(len(maskStr)):
        if maskStr[len(maskStr)-1-i] == '1':
            initialAddr = setBit(initialAddr, i)

    currAddrs = set([initialAddr])
    for i in range(len(maskStr)):
        if maskStr[len(maskStr)-1-i] == 'X':
            newAddrs = set()
            for addr in currAddrs:
                newAddrs.add(setBit(addr, i))
                newAddrs.add(clearBit(addr, i))
            currAddrs = currAddrs.union(newAddrs)
    return currAddrs


isPart1 = False
maskStr = ''
memDict = {}
with open('input.txt') as fp:
    line = fp.readline()
    while line:
        tokens = line.strip().split()
        if line.startswith('mask'):
            maskStr = tokens[2]
        else:
            memAddr, value = int(tokens[0][4:-1]), int(tokens[2])
            if isPart1:
                memDict[memAddr] = applyMask(maskStr, value)
            else:
                for addr in getDecodedAddrs(maskStr, value, memAddr):
                    memDict[addr] = value
        line = fp.readline()

resultSum = sum(memDict.values())

if isPart1:
    print(f'Part 1\n{resultSum}')
else:
    print(f'Part 2\n{resultSum}')
