with open('input.txt', 'r') as input_file:
    instructions = input_file.read()

instructions = instructions.rstrip()


def sum_part_1(sequence):
    sum = 0
    for i in range(len(sequence)):
        if sequence[i] == sequence[i-1]:
            sum += int(sequence[i])
    return sum


def sum_part_2(sequence):
    sum = 0
    for i in range(len(sequence)):
        if sequence[i] == sequence[(i + int(len(sequence) / 2)) % len(sequence)]:
            sum += int(sequence[i])
    return sum

print 'Part 1: %d' % sum_part_1(instructions)
print 'Part 2: %d' % sum_part_2(instructions)