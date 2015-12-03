with open('input.txt') as input:
    items = ''.join(input.readlines())
    up = len([i for i in items if i == '('])
    down = len([i for i in items if i == ')'])
    print(up - down)
    floor = 0
    for position, i in enumerate(items):
        if i == '(':
            floor += 1
        else:
            floor -= 1
        if floor < 0:
            print(position + 1)
            break
