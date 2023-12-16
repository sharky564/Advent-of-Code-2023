def find_loop(network, start, m, n):
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for dir in dirs:
        bad_dir = False
        loop_length = 0
        loop_nodes = [start]
        if 0 <= start[0] + dir[0] < m and 0 <= start[1] + dir[1] < n and start in network[(start[0] + dir[0], start[1] + dir[1])]:
            prev_node = start
            curr_node = (start[0] + dir[0], start[1] + dir[1])
            loop_length += 1
            loop_nodes.append(curr_node)
            while curr_node != start:
                for next_node in network[curr_node]:
                    if next_node != prev_node:
                        if next_node == start or curr_node in network[next_node]:
                            prev_node = curr_node
                            curr_node = next_node
                            loop_length += 1
                            loop_nodes.append(curr_node)
                            break
                else:
                    bad_dir = True
                    break
            if not bad_dir:
                return loop_nodes, loop_length
    return None, None

def part1():
    f = open("input.txt", 'r')
    out = f.read().split('\n')

    network = {}
    start = (-1, -1)
    for i in range(len(out)):
        for j in range(len(out[i])):
            pipe = out[i][j]    
            if pipe == 'F':
                network[(i, j)] = [(i, j + 1), (i + 1, j)]
            elif pipe == '-':
                network[(i, j)] = [(i, j + 1), (i, j - 1)]
            elif pipe == '7':
                network[(i, j)] = [(i + 1, j), (i, j - 1)]
            elif pipe == '|':
                network[(i, j)] = [(i + 1, j), (i - 1, j)]
            elif pipe == 'J':
                network[(i, j)] = [(i, j - 1), (i - 1, j)]
            elif pipe == 'L':
                network[(i, j)] = [(i, j + 1), (i - 1, j)]
            elif pipe == 'S':
                network[(i, j)] = []
                start = (i, j)
            else:
                network[(i, j)] = []


    loop_length = find_loop(network, start, len(out), len(out[0]))[1]
    print(loop_length//2)


def part2():
    f = open("input.txt", 'r')
    out = f.read().split('\n')

    network = {}
    start = (-1, -1)
    for i in range(len(out)):
        for j in range(len(out[i])):
            pipe = out[i][j]    
            if pipe == 'F':
                network[(i, j)] = [(i, j + 1), (i + 1, j)]
            elif pipe == '-':
                network[(i, j)] = [(i, j + 1), (i, j - 1)]
            elif pipe == '7':
                network[(i, j)] = [(i + 1, j), (i, j - 1)]
            elif pipe == '|':
                network[(i, j)] = [(i + 1, j), (i - 1, j)]
            elif pipe == 'J':
                network[(i, j)] = [(i, j - 1), (i - 1, j)]
            elif pipe == 'L':
                network[(i, j)] = [(i, j + 1), (i - 1, j)]
            elif pipe == 'S':
                network[(i, j)] = []
                start = (i, j)
            else:
                network[(i, j)] = []
    
    out = [list(line) for line in out]
    loop = find_loop(network, start, len(out), len(out[0]))[0]
    network[start] = [loop[1], loop[-2]]
    dirs = set([tuple(map(lambda x: x[0] - x[1], zip(loop[1], loop[0]))), tuple(map(lambda x: x[0] - x[1], zip(loop[-2], loop[-1])))])
    if dirs == {(0, 1), (1, 0)}:
        out[start[0]][start[1]] = 'F'
    elif dirs == {(0, 1), (-1, 0)}:
        out[start[0]][start[1]] = 'L'
    elif dirs == {(0, -1), (-1, 0)}:
        out[start[0]][start[1]] = 'J'
    elif dirs == {(0, -1), (1, 0)}:
        out[start[0]][start[1]] = '7'
    elif dirs == {(0, 1), (0, -1)}:
        out[start[0]][start[1]] = '-'
    elif dirs == {(1, 0), (-1, 0)}:
        out[start[0]][start[1]] = '|'


    for i in range(len(out)):
        for j in range(len(out[i])):
            if (i, j) not in loop:
                out[i][j] = '.'

    total = 0
    for x in range(len(out)):
        loop_nodes = 0
        y = 0
        while y < len(out[x]):
            if (x, y) in loop:
                if out[x][y] in ['L', 'J', '|']:
                    loop_nodes += 1
            else:
                if loop_nodes % 2 == 1:
                    total += 1
            y += 1
    print(total)

part1()
part2()