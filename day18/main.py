class Op:
    ADD = '+'
    MULT = '*'


def precedence(op: Op, part1=False) -> int:
    if op == Op.ADD:
        return 1 if part1 else 2
    elif op == Op.MULT:
        return 1
    return 0


def applyOp(term1: int, term2: int, op: Op) -> int:
    if op == Op.ADD:
        return term1 + term2
    elif op == Op.MULT:
        return term1 * term2


def calculate(line: str, part1=False) -> int:
    terms, ops = [], []

    def combineTerms():
        term1, term2 = terms.pop(), terms.pop()
        op = ops.pop()
        terms.append(applyOp(term1, term2, op))

    for ch in "".join(line.strip().split()):
        if ch.isdigit():
            terms.append(int(ch))
        elif ch == '(':
            ops.append(ch)
        elif ch == ')':
            while len(ops) and ops[-1] != '(':
                combineTerms()
            ops.pop()
        elif ch in {Op.ADD, Op.MULT}:
            while len(ops) and precedence(ops[-1], part1) >= precedence(ch, part1):
                combineTerms()
            ops.append(ch)

    while len(ops):
        combineTerms()

    return terms[-1]


lines = open('input.txt').read().splitlines()

# Part 1
resultSum = 0
for line in lines:
    resultSum += calculate(line, True)

print(f'Part 1\n{resultSum}')

# Part 2
resultSum = 0
for line in lines:
    resultSum += calculate(line, False)

print(f'\nPart 2\n{resultSum}')
