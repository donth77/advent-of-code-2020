currYesAnswers = set()
currGroupDict = {}
currGroupCount = 0

yesCountPart1, yesCountPart2 = 0, 0
with open('input.txt') as fp:
    line = fp.readline()
    while line:
        if line == '\n':
            # Add yes answer count for current group
            # Part 1
            yesCountPart1 = yesCountPart1 + len(currYesAnswers)

            # Part 2
            part2Count = 0
            for key, value in currGroupDict.items():
                if value == currGroupCount:
                    part2Count = part2Count + 1

            yesCountPart2 = yesCountPart2 + part2Count

            currYesAnswers.clear()
            currGroupDict = {}
            currGroupCount = 0
        else:
            # parse the current group
            currGroupCount = currGroupCount + 1
            for question in line.strip():
                currYesAnswers.add(question)
                if question in currGroupDict:
                    currGroupDict[question] = currGroupDict[question] + 1
                else:
                    currGroupDict[question] = 1
        line = fp.readline()

# Add yes answer count for final group
# Part 1
yesCountPart1 = yesCountPart1 + len(currYesAnswers)
# Part 2
part2Count = 0
for key, value in currGroupDict.items():
    if value == currGroupCount:
        part2Count = part2Count + 1
yesCountPart2 = yesCountPart2 + part2Count

print(f'Part 1\n{yesCountPart1}\n\nPart 2\n{yesCountPart2}')
