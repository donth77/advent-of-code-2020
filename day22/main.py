from collections import deque

tokens = open('input.txt').read().split('\n\n')
p1Tokens, p2Tokens = tokens

player1Start = [int(n) for n in p1Tokens.splitlines()[1:]]
player2Start = [int(n) for n in p2Tokens.splitlines()[1:]]


def part1():
    player1, player2 = deque(player1Start), deque(player2Start)
    while player1 and player2:
        p1Card = player1.popleft()
        p2Card = player2.popleft()

        if p2Card > p1Card:
            player2.extend([p2Card, p1Card])
        else:
            player1.extend([p1Card, p2Card])

    winning = player1 + player2
    print(
        f'Part 1\n{sum([n * (len(winning) - i) for i, n in enumerate(winning)])}')


def playRecursiveCombat(p1: list, p2: list) -> tuple:
    seen = set()
    while p1 and p2:
        cards = (tuple(p1), tuple(p2))
        if cards in seen:
            return (True, p1)

        p1Card, p2Card = p1.pop(0), p2.pop(0)

        didP1WinRecurse = None
        if len(p1) >= p1Card and len(p2) >= p2Card:
            didP1WinRecurse = playRecursiveCombat(p1[:p1Card], p2[:p2Card])[0]

        if (didP1WinRecurse != False) and (didP1WinRecurse or p1Card >= p2Card):
            p1.extend([p1Card, p2Card])
        else:
            p2.extend([p2Card, p1Card])

        seen.add(cards)

    winner = p1 + p2
    return (len(p1) > len(p2), winner)


def part2():
    winning = playRecursiveCombat(player1Start, player2Start)[1]
    print(
        f'\nPart 2\n{sum([n * (len(winning) - i) for i, n in enumerate(winning)])}')


part1()
part2()
