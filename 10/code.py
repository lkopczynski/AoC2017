

class KnotString:
    def __init__(self, len=256):
        self.marks = [i for i in range(len)]
        self.pos = 0
        self.skip_size = 0

    def process_length(self, l):
        if l > 1:
            endpos = (self.pos + l) % len(self.marks)
            if self.pos >= endpos:
                sublist = self.marks[self.pos:] + self.marks[:endpos]
            else:
                sublist = self.marks[self.pos:endpos]
            i = 0
            for element in reversed(sublist):
                j = (self.pos + i) % len(self.marks)
                self.marks[j] = element
                i += 1
        self.pos = ( self.pos + l + self.skip_size) % len(self.marks)
        self.skip_size += 1

    def get_dense_hash(self):
        dh = []
        for i in range(16):
            cl = self.marks[i:i+16]
            print cl
            xr = eval('^'.join([str(x) for x in cl]))
            dh.append(xr)
        return dh

    def knot_hash(self):
        dh = self.get_dense_hash()
        hh = ['%0.2X' % d for d in dh]
        return ''.join(hh)


    def result(self):
        return self.marks[0] * self.marks[1]


with open('input.txt', 'r') as input_file:
    instructions = input_file.read()
instructions = '1,2,4'
byte_instructions = []
for c in instructions:
    byte_instructions.append(ord(c))
byte_instructions.extend([17, 31, 73, 47, 23])

kt = KnotString()
for i in range(64):
    for inst in byte_instructions:
        kt.process_length(int(inst))
print kt.result()
print kt.knot_hash()





