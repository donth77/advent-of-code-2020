instructions = []
with open('input.txt') as fp:
    line = fp.readline()
    while line:
        tokens = line.strip().split()
        instructions.append((tokens[0], int(tokens[1])))
        line = fp.readline()


def execute(instrs):
    hasLoop = False
    visited = set()
    ptr = acc = 0
    while ptr < len(instrs):
        op, value = instrs[ptr]
        if ptr in visited:
            hasLoop = True
            break
        visited.add(ptr)
        if op == 'jmp':
            ptr = ptr + value
            continue
        elif op == 'acc':
            acc = acc + value
        ptr = ptr + 1
    return (acc, hasLoop)


print(f'Part 1\n{execute(instructions)[0]}\n')

swapDict = {'nop': 'jmp', 'jmp': 'nop'}
for i, (op, value) in enumerate(instructions):
    if op == 'nop' or op == 'jmp':
        swappedOp = [(swapDict[op], value)]
        newInstructions = instructions[:i] + swappedOp + instructions[i+1:]
        accValue, hasLoop = execute(newInstructions)
        if not hasLoop:
            print(f'\nPart 2\n{accValue}')
