accounting_entries = []
entry_set = set()
target_sum = 2020
with open('input.txt') as fp:
    line = fp.readline()
    while line:
        value = int(line.strip())
        accounting_entries.append(value)
        entry_set.add(value)
        line = fp.readline()
# Part 1 - 2 Sum
# Find the two entries that sum to 2020 and then multiply those two numbers together
for entry in accounting_entries:
    complement = target_sum - entry
    if complement in entry_set and not (complement == entry):
        print(f'Part 1\n{entry * complement}\n')
        break

# Part 2 - 3 Sum
# Find 3 entries that sum to 2020 and then output the product
for i in range(len(accounting_entries) - 1):
    trip_set = set()
    for j in range(i + 1, len(accounting_entries)):
        curr_sum = accounting_entries[i] + accounting_entries[j]
        complement = target_sum - curr_sum
        if complement in trip_set:
            print(
                f'\nPart 2\n{complement * accounting_entries[i] * accounting_entries[j]}')
            break
        else:
            trip_set.add(accounting_entries[j])
