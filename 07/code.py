import itertools


class Program:
    def __init__(self, name, weight, children=[]):
        self.name = name
        self.weight = int(weight)
        self.children = children

    def x_is_child(self, x):
        if x in self.children:
            return True
        return False

    def add_child(self, c):
        self.children.append(c)

    def add_children(self, cl):
        for c in cl:
            self.add_child(c)

    def weight_with_children(self):
        weight = self.weight
        to_count = self.children
        while len(to_count) > 0:
            print
            print to_count
            for p in to_count:
                weight += p.weight
                if len(p.children) > 0:
                    to_count.extend(p.children)
                to_count.remove(p)

        return weight


class Tower:
    def __init__(self):
        self.programs = {}

    def add_program(self, p):
        self.programs[p.name] = p

    def get_bottom_program(self):
        for name, program in self.programs.iteritems():
            if not any(self.programs[p].x_is_child(name) for p in self.programs):
                return program

    @property
    def weight(self):
        weight = 0
        for p in self.programs:
            weight += self.programs[p].weight
        return weight

    def subtower_weight(self, bottom_program):
        weight = bottom_program.weight
        to_count = bottom_program.children
        while len(to_count) > 0:
            for p in to_count:
                weight += self.programs[p].weight
                to_count.extend(self.programs[p].children)
                to_count.remove(p)
        return weight

    def check_balance(self):
        for name, program in self.programs.iteritems():
            weights = [self.subtower_weight(self.programs[c]) for c in program.children]
            if len(weights) > 0:
                print weights
                for x, y in itertools.combinations(weights, 2):
                    if x != y:
                        print x, y



def find(f, l):
    for item in l:
        if f(item):
            return item


with open('input.txt', 'r') as input_file:
    instructions = input_file.readlines()

programs = {}
t = Tower()

for i in instructions:
    i = i.rstrip().replace(' ', '')
    name = i[:i.index('(')]
    weight = i[i.index('(')+1:i.index(')')]
    children = []
    if '->' in i:
        children = i[i.index('>')+1:].split(',')
    p = Program(name, weight, children)
    programs[name] = p
    t.add_program(p)

bottom = t.get_bottom_program()
print t.weight
print t.subtower_weight(programs['vtgfsqt'])
print t.check_balance()






