with open('input.txt', 'r') as input_file:
    instructions = input_file.readlines()

jumps = [int(i.rstrip()) for i in instructions]


def jumps_1(l):
    pos = 0
    jumps_done = 0
    while True:
        new_pos = pos + l[pos]
        l[pos] += 1
        jumps_done += 1
        if new_pos < 0 or new_pos > len(l) - 1:
            return jumps_done
        else:
            pos = new_pos


def jumps_2(l):
    pos = 0
    jumps_done = 0
    while True:
        new_pos = pos + l[pos]
        if l[pos] > 2:
            l[pos] -= 1
        else:
            l[pos] += 1
        jumps_done += 1
        if new_pos < 0 or new_pos > len(l) - 1:
            return jumps_done
        else:
            pos = new_pos

#print 'Part1 : %d ' % jumps_1(jumps)
print 'Part2 : %d ' % jumps_2(jumps)
