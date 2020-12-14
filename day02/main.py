valid_count_part1, valid_count_part2 = 0, 0
with open('input.txt') as fp:
    line = fp.readline()
    while line:
        tokens = line.split()
        policy, letter, password = tokens[0], tokens[1][:-1], tokens[2]
        policy_tokens = policy.split('-')
        first_value, second_value = int(
            policy_tokens[0]), int(policy_tokens[1])

        # Part 1 - Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid.
        num_occurences = password.count(letter)
        if (first_value <= num_occurences <= second_value):
            valid_count_part1 = valid_count_part1 + 1

        # Part 2 - Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.
        num_positions = 0
        if(password[first_value - 1] == letter):
            num_positions = num_positions + 1
        if(password[second_value - 1] == letter):
            num_positions = num_positions + 1

        if(num_positions == 1):
            valid_count_part2 = valid_count_part2 + 1

        line = fp.readline()

print(f'Part 1\n{valid_count_part1}\n\nPart 2\n{valid_count_part2}')
