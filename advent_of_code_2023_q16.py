def part1():
    f = open("input.txt", 'r')
    out = f.read().split('\n')
    out = [list(row) for row in out]

    m = len(out)
    n = len(out[0])
    beams = [(0, -1, 'E')]
    curr_node_beam_vals = {(i, j): [] for i in range(m) for j in range(n)}
    curr_node_beam_vals[(0, -1)] = ['E']
    while beams:
        # print(beams)
        beam = beams.pop(0)
        i, j, val = beam
        if val == 'E':
            if j == n - 1:
                continue
            if out[i][j + 1] in '/|' and 'N' not in curr_node_beam_vals[(i, j + 1)]:
                beams.append((i, j + 1, 'N'))
                curr_node_beam_vals[(i, j + 1)].append('N')
            if out[i][j + 1] in '\\|' and 'S' not in curr_node_beam_vals[(i, j + 1)]:
                beams.append((i, j + 1, 'S'))
                curr_node_beam_vals[(i, j + 1)].append('S')
            if out[i][j + 1] in ['-', '.'] and 'E' not in curr_node_beam_vals[(i, j + 1)]:
                beams.append((i, j + 1, 'E'))
                curr_node_beam_vals[(i, j + 1)].append('E')
        elif val == 'N':
            if i == 0:
                continue
            if out[i - 1][j] in '/-' and 'E' not in curr_node_beam_vals[(i - 1, j)]:
                beams.append((i - 1, j, 'E'))
                curr_node_beam_vals[(i - 1, j)].append('E')
            if out[i - 1][j] in '\\-' and 'W' not in curr_node_beam_vals[(i - 1, j)]:
                beams.append((i - 1, j, 'W'))
                curr_node_beam_vals[(i - 1, j)].append('W')
            if out[i - 1][j] in ['|', '.'] and 'N' not in curr_node_beam_vals[(i - 1, j)]:
                beams.append((i - 1, j, 'N'))
                curr_node_beam_vals[(i - 1, j)].append('N')
        elif val == 'W':
            if j == 0:
                continue
            if out[i][j - 1] in '/|' and 'S' not in curr_node_beam_vals[(i, j - 1)]:
                beams.append((i, j - 1, 'S'))
                curr_node_beam_vals[(i, j - 1)].append('S')
            if out[i][j - 1] in '\\|' and 'N' not in curr_node_beam_vals[(i, j - 1)]:
                beams.append((i, j - 1, 'N'))
                curr_node_beam_vals[(i, j - 1)].append('N')
            if out[i][j - 1] in ['-', '.'] and 'W' not in curr_node_beam_vals[(i, j - 1)]:
                beams.append((i, j - 1, 'W'))
                curr_node_beam_vals[(i, j - 1)].append('W')
        elif val == 'S':
            if i == m - 1:
                continue
            if out[i + 1][j] in '/-' and 'W' not in curr_node_beam_vals[(i + 1, j)]:
                beams.append((i + 1, j, 'W'))
                curr_node_beam_vals[(i + 1, j)].append('W')
            if out[i + 1][j] in '\\-' and 'E' not in curr_node_beam_vals[(i + 1, j)]:
                beams.append((i + 1, j, 'E'))
                curr_node_beam_vals[(i + 1, j)].append('E')
            if out[i + 1][j] in ['|', '.'] and 'S' not in curr_node_beam_vals[(i + 1, j)]:
                beams.append((i + 1, j, 'S'))
                curr_node_beam_vals[(i + 1, j)].append('S')

    count = 0
    for i in range(m):
        for j in range(n):
            if len(curr_node_beam_vals[(i, j)]) >= 1:
                count += 1
    print(count)


def part2():
    f = open("input.txt", 'r')
    out = f.read().split('\n')

    m = len(out)
    n = len(out[0])
    init_left = [(i, -1, 'E') for i in range(m)]
    init_right = [(i, n, 'W') for i in range(m)]
    init_top = [(-1, j, 'S') for j in range(n)]
    init_bottom = [(m, j, 'N') for j in range(n)]
    init_vals = init_left + init_right + init_top + init_bottom
    max_val = 0
    for init_beam in init_vals:
        beams = [init_beam]
        curr_node_beam_vals = {(i, j): [] for i in range(m) for j in range(n)}
        curr_node_beam_vals[init_beam[:2]] = [init_beam[2]]
        while beams:
            # print(beams)
            beam = beams.pop(0)
            i, j, val = beam
            if val == 'E':
                if j == n - 1:
                    continue
                if out[i][j + 1] in '/|' and 'N' not in curr_node_beam_vals[(i, j + 1)]:
                    beams.append((i, j + 1, 'N'))
                    curr_node_beam_vals[(i, j + 1)].append('N')
                if out[i][j + 1] in '\\|' and 'S' not in curr_node_beam_vals[(i, j + 1)]:
                    beams.append((i, j + 1, 'S'))
                    curr_node_beam_vals[(i, j + 1)].append('S')
                if out[i][j + 1] in ['-', '.'] and 'E' not in curr_node_beam_vals[(i, j + 1)]:
                    beams.append((i, j + 1, 'E'))
                    curr_node_beam_vals[(i, j + 1)].append('E')
            elif val == 'N':
                if i == 0:
                    continue
                if out[i - 1][j] in '/-' and 'E' not in curr_node_beam_vals[(i - 1, j)]:
                    beams.append((i - 1, j, 'E'))
                    curr_node_beam_vals[(i - 1, j)].append('E')
                if out[i - 1][j] in '\\-' and 'W' not in curr_node_beam_vals[(i - 1, j)]:
                    beams.append((i - 1, j, 'W'))
                    curr_node_beam_vals[(i - 1, j)].append('W')
                if out[i - 1][j] in ['|', '.'] and 'N' not in curr_node_beam_vals[(i - 1, j)]:
                    beams.append((i - 1, j, 'N'))
                    curr_node_beam_vals[(i - 1, j)].append('N')
            elif val == 'W':
                if j == 0:
                    continue
                if out[i][j - 1] in '/|' and 'S' not in curr_node_beam_vals[(i, j - 1)]:
                    beams.append((i, j - 1, 'S'))
                    curr_node_beam_vals[(i, j - 1)].append('S')
                if out[i][j - 1] in '\\|' and 'N' not in curr_node_beam_vals[(i, j - 1)]:
                    beams.append((i, j - 1, 'N'))
                    curr_node_beam_vals[(i, j - 1)].append('N')
                if out[i][j - 1] in ['-', '.'] and 'W' not in curr_node_beam_vals[(i, j - 1)]:
                    beams.append((i, j - 1, 'W'))
                    curr_node_beam_vals[(i, j - 1)].append('W')
            elif val == 'S':
                if i == m - 1:
                    continue
                if out[i + 1][j] in '/-' and 'W' not in curr_node_beam_vals[(i + 1, j)]:
                    beams.append((i + 1, j, 'W'))
                    curr_node_beam_vals[(i + 1, j)].append('W')
                if out[i + 1][j] in '\\-' and 'E' not in curr_node_beam_vals[(i + 1, j)]:
                    beams.append((i + 1, j, 'E'))
                    curr_node_beam_vals[(i + 1, j)].append('E')
                if out[i + 1][j] in ['|', '.'] and 'S' not in curr_node_beam_vals[(i + 1, j)]:
                    beams.append((i + 1, j, 'S'))
                    curr_node_beam_vals[(i + 1, j)].append('S')

        count = 0
        for i in range(m):
            for j in range(n):
                if len(curr_node_beam_vals[(i, j)]) >= 1:
                    count += 1
        if count > max_val:
            max_val = count
    
    print(max_val)



part1()
part2()