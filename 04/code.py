with open('input.txt', 'r') as input_file:
    instructions = input_file.readlines()

def is_anagram(w1, w2):
    if len(w1) != len(w2):
        return False
    for c in w1:
        if c not in w2:
            return False
    return True
        

def is_valid_passphrase(p):
    p = p.split()
    while len(p) > 0:
        w = p.pop()
        for w2 in p:
            if is_anagram(w, w2):
                return False
    return True

s = 0
for i in instructions:
    i = i.rstrip()
    if is_valid_passphrase(i):
        s += 1

print s
