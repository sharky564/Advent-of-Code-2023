f = open("Advent of Code/aoc_2023_day_10.txt", 'r')
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

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
loop = []
for dir in dirs:
    bad_dir = False
    loop_found = False
    loop_length = 0
    loop_nodes = [start]
    if 0 <= start[0] + dir[0] < len(out) and 0 <= start[1] + dir[1] < len(out[0]) and start in network[(start[0] + dir[0], start[1] + dir[1])]:
        prev_node = start
        curr_node = (start[0] + dir[0], start[1] + dir[1])
        loop_length += 1
        loop_nodes.append(curr_node)
        while curr_node != start:
            # proceed thru network
            for next_node in network[curr_node]:
                if next_node != prev_node:
                    if next_node == start or curr_node in network[next_node]:
                        prev_node = curr_node
                        curr_node = next_node
                        loop_length += 1
                        loop_nodes.append(curr_node)
                        break
            else:
                # bad network
                bad_dir = True
                break
        if not bad_dir:
            loop_found = True
    if loop_found:
        print(dir, loop_length//2)
        loop = loop_nodes

out = [list(line) for line in out]
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


# replace all non-loop nodes with '.'
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