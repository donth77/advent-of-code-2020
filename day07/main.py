import re

colorGraph = {}
with open('input.txt') as fp:
    line = fp.readline()
    while line:
        tokens = line.strip().split(',')
        sourceTokens = tokens[0].split('contain')
        sourceColor = sourceTokens[0].split('bags')[0].strip()

        colorGraph[sourceColor] = []
        targetLst = sourceTokens[1:] + tokens[1:]

        for targetStr in targetLst:
            targetStrTokens = re.split('bags?', targetStr.strip())
            targetCountStrLst = re.findall(r'\d+', targetStr)
            if len(targetCountStrLst) > 0:
                targetCountStr = targetCountStrLst[0]
                targetColor = targetStrTokens[0].split(targetCountStr)[
                    1].strip()
                colorGraph[sourceColor].append(
                    (targetColor, int(targetCountStr))
                )

        line = fp.readline()

visitedPart1 = set()


def traversePart1(visited, graph, targetNode):
    if targetNode not in visited:
        visited.add(targetNode)
        for source in graph:
            for child in graph[source]:
                if child[0] == targetNode:
                    traversePart1(visited, graph, source)


part2Count = 0


def traversePart2(graph, sourceNode, srcCount):
    for child in graph[sourceNode]:
        childKey, count = child
        countToAdd = count * srcCount
        global part2Count
        part2Count = part2Count + countToAdd
        traversePart2(graph, childKey, countToAdd)
    pass


traversePart1(visitedPart1, colorGraph, 'shiny gold')

traversePart2(colorGraph, 'shiny gold', 1)

print(f'Part 1\n{len(visitedPart1) - 1}\n\nPart 2\n{part2Count}')
