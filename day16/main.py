mode = 0

rules = dict()
ranges = []
nearby = []
myTicket = []

with open('input.txt') as fp:
  line = fp.readline()
  while line:
    tokens = line.split()
    if len(tokens):
      if mode == 0:
        tokens = line.strip().split(':')
        ruleTokens = tokens[1].strip().split(' or ')
        ticketRanges = []
        for token in ruleTokens:
          rangeTokens = token.split('-')
          ticketRange = (int(rangeTokens[0]), int(rangeTokens[1]))
          ticketRanges.append(ticketRange)
          ranges.append(ticketRange)
        rules[tokens[0]] = ticketRanges
      elif mode == 1 and tokens[0] != 'your':
        yourTokens = tokens[0].split(',')
        myTicket = [int(n) for n in yourTokens]
      elif mode == 2 and tokens[0] != 'nearby':
        nearbyTokens = tokens[0].split(',')
        nearby.append([int(n) for n in nearbyTokens])

    if line == '\n':
      mode += 1
    line = fp.readline()

# Part 1
errorRate = 0
nearbyValues = [num for ticket in nearby for num in ticket]
validTickets = []

for index, ticket in enumerate(nearby):
  ticketValid = True
  for num in ticket:
    valid = False
    for rule in ranges:
      if (num in range(rule[0], rule[1]+1)):
        valid = True
        break
    if not valid:
      ticketValid = False
      errorRate += num
  if ticketValid:
    validTickets.append(ticket)

print(f'Part 1\n{errorRate}')

# Part 2
fieldToIndexes = {}
for field, ranges in rules.items():
  for i in range(len(myTicket)):
    if all(any(t[i] in range(r[0], r[1]+1) for r in ranges) for t in validTickets):
      if field in fieldToIndexes:
        fieldToIndexes[field].append(i)
      else:
        fieldToIndexes[field] = [i]     


fieldToIndexes = {k: v for k, v in sorted(fieldToIndexes.items(), key=lambda item: len(item[1]))}

assigned = set()
for field, indexes in fieldToIndexes.items():
    for i in indexes:
        if i in assigned: 
          continue
        fieldToIndexes[field] = i
        assigned.add(i)

part2Result = 1
for field, i in fieldToIndexes.items():
    if 'departure' in field:
        part2Result *= myTicket[i]

print(f'\nPart 2\n{part2Result}')
			
			