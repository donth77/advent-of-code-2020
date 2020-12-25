key1, key2 = map(int, open("input.txt").readlines())

value = 1
loops = 0
subjectNum = 1

while (value != key1 and value != key2):
    value *= 7
    value %= 20201227
    if value == key1:
        subjectNum = key2
    elif value == key2:
        subjectNum = key1
    loops += 1

value = 1
for _ in range(loops):
    value *= subjectNum
    value %= 20201227

print(f'Part 1\n{value}')