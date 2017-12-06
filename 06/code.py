
class Memory:
    def __init__(self, blocks):
        self.banks = [int(b) for b in blocks]
        print self.banks

    def reallocate(self, state=None):
        steps = 0
        configs = []
        while True:
            config_str = '-'.join([str(b) for b in self.banks])
            configs.append(config_str)
            cb = 0
            for b in range(len(self.banks)):
                if self.banks[b] > self.banks[cb]:
                    cb = b
            blocks = self.banks[cb]
            self.banks[cb] = 0
            pos = cb
            for i in range(blocks):
                pos += 1
                pos = pos % len(self.banks)
                self.banks[pos] += 1
            steps += 1
            config_str = '-'.join([str(b) for b in self.banks])
            if state is not None:
                if config_str == state:
                    return steps
            elif config_str in configs:
                return steps, config_str










with open('input.txt', 'r') as input_file:
    instructions = input_file.read()

m = Memory(instructions.split())
steps, state = m.reallocate()
print 'part 1: %d' % steps
steps = m.reallocate(state)
print 'part 2: %d' % steps


