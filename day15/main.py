import collections
nums = [6, 19, 0, 5, 7, 13, 1]


def speakSequence(finalTurn):
    numDict = {}
    for i, num in enumerate(nums):
        numDict[num] = collections.deque([i], maxlen=2)

    last = nums[-1]
    for i in range(len(nums), finalTurn):
        turnsDeque = numDict[last]

        if len(turnsDeque) == 1:
            spoken = 0
        else:
            spoken = turnsDeque[1]-turnsDeque[0]
        if spoken in numDict:
            numDict[spoken].append(i)
        else:
            numDict[spoken] = collections.deque([i], maxlen=2)
        last = spoken
    return spoken


print(f'Part 1\n{speakSequence(2020)}')
print(f'\nPart 2\n{speakSequence(30000000)}')
