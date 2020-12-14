tree_map = []

with open('input.txt') as fp:
    line = fp.readline()
    map_row = []
    while line:
        tree_map.append(line[:-1])
        line = fp.readline()


def traverse(dx, dy):
    x, y, tree_count = 0, 0, 0
    while y < len(tree_map):
        if tree_map[y][x % len(tree_map[0])] == '#':
            tree_count = tree_count + 1
        x = x + dx
        y = y + dy
    return tree_count


print(f'Part 1\n{traverse(3, 1)}\n\nPart 2\n{traverse(1, 1) * traverse(3, 1) * traverse(5, 1) * traverse(7, 1) * traverse(1, 2)}')
