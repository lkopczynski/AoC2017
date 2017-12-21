

with open('input.txt', 'r') as input_file:
    instructions = input_file.read()

idx = 0
gc = 0
tc = 0
value_stack = []
garbage = False
garbage_count = 0
s = instructions.rstrip()

while idx < len(s):
    if s[idx] == '!':
        idx += 1
    elif s[idx] == '>':
        garbage = False
    elif garbage:
        garbage_count += 1
    elif s[idx] == '<':
        garbage = True
    elif s[idx] == '{':
        gc += 1
        value_stack.append(gc)
    elif s[idx] == '}' and gc > 0:
        gc -= 1
    if gc == 0:
        for v in value_stack:
            tc += v
        value_stack = []
    idx += 1

print 'Part 1: %d ' % tc
print 'Part 2: %d ' % garbage_count



