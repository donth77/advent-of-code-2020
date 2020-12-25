from lark import Lark, LarkError


def processRules(rules, isPart1=False):
    if not isPart1:
        rules = rules.replace('8: 42', '8: 42 | 42 8').replace(
            '11: 42 31', '11: 42 31 | 42 11 31')

    numsStr = '0123456789'
    lettersStr = 'cdefghijlm'
    rules = rules.translate(str.maketrans(numsStr, lettersStr))

    parser = Lark(
        f'''{rules}\n%import common.WS\n%ignore WS''', start=lettersStr[0])

    total = 0
    for line in lines.splitlines():
        try:
            parser.parse(line)
            total += 1
        except LarkError:
            pass
    return total


rules, lines = open('input.txt').read().split('\n\n')

print(f'Part 1\n{processRules(rules, True)}')
print(f'\nPart 2\n{processRules(rules, False)}')
