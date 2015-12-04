import pprint


def move(curr_loc, direction):

    x, y = curr_loc[0], curr_loc[1]
    if direction == '>':
        x += 1
    elif direction == '<':
        x -= 1
    elif direction == '^':
        y += 1
    elif direction == 'v':
        y -= 1
    return (x, y)


def main():

    grid = {(0, 0): 1}
    loc = (0, 0)

    with open('input.txt') as input:

        for p in ''.join(input.readlines()):

            loc = move(loc, p)
            if loc in grid.keys():
                grid[loc] += 1
            else:
                grid[loc] = 1

        pprint.pprint(grid)
        print(len(grid))

if __name__ == '__main__':

    main()
