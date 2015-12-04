import pprint
import day_3


grid = {(0, 0): 2}
loc = (0, 0)

with open('input.txt') as input:

    path = ''.join(input.readlines())
    santa = [p for i, p in enumerate(path) if i % 2 == 0]
    robo_santa = [p for i, p in enumerate(path) if i % 2 == 1]

    for s in santa:

        loc = day_3.move(loc, s)
        if loc in grid.keys():
            grid[loc] += 1
        else:
            grid[loc] = 1

    loc = (0, 0)
    for r in robo_santa:

        loc = day_3.move(loc, r)
        if loc in grid.keys():
            grid[loc] += 1
        else:
            grid[loc] = 1

pprint.pprint(grid)
print(len(grid))
