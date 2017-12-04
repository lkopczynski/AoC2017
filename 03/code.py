
class spiral:
    velocities = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0), 4: (1, 1), 5: (-1, 1), 6: (-1, -1), 7:(1, -1)}

    def __init__(self):
        self.locations = {}

    def calc_locations(self, target):
        location = (0, 0)
        d = 1
        changes = 0
        change_d_after = 1
        i = 0
        while True:
            i += 1
            r = self.get_adj_sum(location)
            if r == 0:
                r = i
            self.locations[location] = r
            location = (location[0] + self.velocities[d][0], location[1] + self.velocities[d][1])
            if i % change_d_after == 0:
                changes += 1
                d = (d + 1) % 4
                if changes % 2 == 0:
                    change_d_after += 1

            if r > target:
                return r

    def get_adj_sum(self, location):
        s = 0
        for i in range(0, 8):
            adj_cell = (location[0] + self.velocities[i][0], location[1] + self.velocities[i][1])
            if adj_cell in self.locations:
                s += self.locations[(adj_cell)]
        return s

    def get_distance(self, target):
        x, y = self.locations.keys()[self.locations.values().index(target)]
        return abs(x) + abs(y)

    def print_grid(self, size=20):
        min_coord = size / 2 - size
        max_coord = size / 2

        for y in range(min_coord, max_coord):
            line = ''
            for x in range(min_coord, max_coord):
                line += ' ' + str(self.locations[(x, y)])
            print line


target = 312051
s = spiral()
print s.calc_locations(target)
s.print_grid()
