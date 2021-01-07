from copy import deepcopy

rules = dict()
messages = []

with open('input.txt') as fp:
  line = fp.readline()
  while line:
    tokens = line.strip().split(': ')

    if len(tokens) > 1:
      ruleId, matches = tokens[0], tokens[1]
      if '"' in matches:
        rule = matches.strip('\"')
      else:
        rule = []
        for option in matches.split('|'):
          rule.append(tuple(map(str, option.split())))
      rules[ruleId] = rule
    elif len(tokens) and tokens[0]:
      messages.append(line.strip())
    line = fp.readline()


def match(rules, msg, rule='0', index=0):
	if index == len(msg):
		return []

	rule = rules[rule]
	if type(rule) is str:
		if msg[index] == rule:
			return [index + 1]
		return []
  
	matches = []
	for option in rule:
		subMatches = [index]

		for subRule in option:
			newMatches = []
			for i in subMatches:
				newMatches += match(rules, msg, subRule, i)
			subMatches = newMatches

		matches += subMatches

	return matches

# Part 1
part1Count = 0
for msg in messages:
  if len(msg) in match(rules, msg):
    part1Count += 1

print(f'Part 1\n{part1Count}')

# Part 2
part2Rules = deepcopy(rules)
part2Rules['8']  = [('42',), ('42', '8')]
part2Rules['11'] = [('42', '31'), ('42', '11', '31')]

part2Count = 0
for msg in messages:
  if len(msg) in match(part2Rules, msg):
    part2Count += 1

print(f'\nPart 2\n{part2Count}')