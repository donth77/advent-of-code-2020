earliestTimePart1 = None
serviceIDs = []
serviceIDsPart2 = []
maxID = -1

with open('input.txt') as fp:
    line = fp.readline()
    lineNum = 0
    while line:
        if lineNum == 0:
            earliestTimePart1 = int(line.strip())
        elif lineNum == 1:
            tokens = line.strip().split(',')
            for token in tokens:
                if not token == 'x':
                    id = int(token)
                    serviceIDs.append(id)
                    maxID = max(maxID, id)
                else:
                    serviceIDs.append(token)
        line = fp.readline()
        lineNum += 1

for i in range(earliestTimePart1, earliestTimePart1 + maxID):
    found = False
    for id in serviceIDs:
        if id == 'x':
            continue

        if (i % id == 0) == True:
            found = True
            print(f'Part 1\n{id * (i - earliestTimePart1)}')
            break
    if found:
        break

earliestTime = 0  # earliest timestamp all bus IDs depart at offsets matching list indices
runningProduct = 1

# t + index % id === 0 for each element
#
# [7, 13, 'x', 'x', 59, 'x', 31, 19]
# index: 0, id: 7   -- 0 + 0 % 7 == 0
# index: 1, id: 13  -- 77 + 1 % 13 == 0
# index: 4, id: 59  -- 350 + 4 % 59 == 0
# index: 6, id: 31  -- 70147 + 6 % 31  == 0
# index: 7, id: 19  -- 1068781 + 7 % 19 == 0
#
# result is 1068781

for (index, id) in enumerate(serviceIDs):
    if id == 'x':
        continue
    while((earliestTime + index) % id != 0):
        earliestTime += runningProduct
    runningProduct *= id
print(f'\nPart 2\n{earliestTime}')
