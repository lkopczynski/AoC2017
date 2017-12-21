class Grid:
    velocities = {
        'n': [0, 1],
        'ne': [1, 1],
        'se': [1, -1],
        's': [0, -1],
        'sw': [-1, -1],
        'nw': [-1, 1]
    }

    def __init__(self):
        self.pos_x = 0
        self.pos_y = 0

    def move(self,d):
        self.pos_x += self.velocities[d][0]
        self.pos_y += self.velocities[d][1]

    def move_to_zero(self,x,y):
        steps = 0
        while True:
            if x == 0 and y < 0:
                dir = 'n'
            elif x < 0 and y < 0:
                dir = 'ne'
            elif x < 0 and y > 0:
                dir = 'se'
            elif x == 0 and y > 0:
                dir = 's'
            elif x > 0 and y > 0:
                dir = 'sw'
            elif x > 0 and y < 0:
                dir = 'nw'
            elif x > 0 and y == 0:
                dir = 'sw'
            elif x < 0 and y == 0:
                dir = 'ne'
            elif x == 0 and y == 0:
                return steps

            x += self.velocities[dir][0]
            y += self.velocities[dir][1]

            print x,y

            steps += 1



with open('input.txt', 'r') as input_file:
    instructions = input_file.read()

g = Grid()
max_steps = 0
for i in instructions.split(','):
    g.move(i)
    curr_steps = g.move_to_zero(g.pos_x, g.pos_y)
    if curr_steps > max_steps:
        max_steps = curr_steps


print 'Part 1: %d' % g.move_to_zero(g.pos_x, g.pos_y)
print 'Part 2: %d' % max_steps
