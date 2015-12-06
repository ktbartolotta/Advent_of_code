
def apply_action_in_range(house, start, stop, action):

    for y in xrange(start[1], stop[1] + 1):
        for x in xrange(start[0], stop[0] + 1):
            house[x][y] = action(house[x][y])
    return house


def toggle(light):

    return not light


def turn_on(light):

    return True


def turn_off(light):

    return False


def get_action(action_str):

    if action_str == 'on':
        return turn_on
    elif action_str == 'off':
        return turn_off
    else:
        return toggle


def initialize_house(house, grid_size):

    new_house = list(house)
    for y in xrange(grid_size):
        new_house.append([])
        for x in xrange(grid_size):
            new_house[y].append(False)
    return new_house


def get_start(start_str):

    return tuple([int(k) for k in start_str.split(',')])


def get_stop(stop_str):

    return tuple([int(k) for k in stop_str.split(',')])


def parse_instruction(instruction):

    return (get_start(instruction.split(' ')[-3]),
            get_stop(instruction.split(' ')[-1]),
            get_action(instruction.split(' ')[-4]))


def main():

    house_size = 1000
    house = initialize_house([], house_size)
    with open('input.txt') as input:

        for instruction in input.readlines():
            start, stop, action = parse_instruction(instruction)
            house = apply_action_in_range(house, start, stop, action)

    count = 0
    for row in house:
        for col in row:
            count += 1 if col else 0
    print(count)


if __name__ == '__main__':

    main()
