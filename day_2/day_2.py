
with open('input.txt') as input:

    total = 0
    t_ribbon = 0
    for item in input.readlines():
        dims = [int(i.strip()) for i in item.split('x')]
        m_sides = sorted(dims)[0:2]
        ribbon = 2 * sum(m_sides) + reduce(lambda x, y: x * y, dims)
        s_area = [dims[0] * dims[1], dims[1] * dims[2], dims[0] * dims[2]]
        m = min(s_area)
        t_area = 2 * (sum(s_area)) + m
        print(dims, m_sides, m, s_area, ribbon, t_area)
        total += t_area
        t_ribbon += ribbon
    print("total wrap:  %d" % total)
    print("total ribbon:  %d" % t_ribbon)
