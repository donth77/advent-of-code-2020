bag = [0]
with open('input.txt') as fp:
    line = fp.readline()
    while line:
        bag.append(int(line.strip()))
        line = fp.readline()

bag.sort()
bag.append(bag[-1:][0]+3)

countDict = {}
for i in range(1, len(bag)):
    diff = bag[i] - bag[i - 1]
    if diff in countDict:
        countDict[diff] += 1
    else:
        countDict[diff] = 1

# Part 2
# Calculate Tribonacci sequence, each number is the sum of the three preceding
# T(n) = T(n-1) + T(n-2) + T(n- 3)
# Dynammic Programming solution
arrange = [1]+[0]*bag[-1]
for i in bag[1:]:
    arrange[i] = arrange[i-3] + arrange[i-2] + arrange[i-1]


print(f'Part 1\n{countDict[1] * countDict[3]}\n\nPart 2\n{arrange[-1]}')
