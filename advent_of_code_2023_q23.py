import time

def condense_grid(grid, start, end):
    nodes = [start, end]
    NSEW = N, S, E, W = -1j, 1j, 1, -1
    for node in grid:
        if grid[node] == '.':
            neighbours = [grid[node + d] for d in NSEW if node + d in grid]
            if neighbours.count('#') < 2:
                nodes.append(node)
    graph = {node: set() for node in nodes}
    for node in nodes:
        for d in NSEW:
            if node + d in grid and grid[node + d] != '#':
                intersection_found = False
                prev_node = node
                z = node + d
                dist = 1
                while not intersection_found:
                    if z == start or z == end:
                        graph[node].add((z, dist))
                        intersection_found = True
                        break
                    else:
                        neighbours = [grid[z + d] for d in NSEW if z + d in grid]
                        if neighbours.count('#') < 2:
                            graph[node].add((z, dist))
                            intersection_found = True
                            break
                        else:
                            dirs = {'^': [N], 'v': [S], '>': [E], '<': [W]}
                            possible_directions = dirs.get(grid[z], NSEW)
                            for direction in possible_directions:
                                if z + direction in grid and z + direction != prev_node and grid[z + direction] != '#':
                                    prev_node = z
                                    z += direction
                                    dist += 1
                                    break
                            else:
                                intersection_found = True
                                break
    return graph


def longest_path(graph, start, end, path_nodes=[], path=[]):
    if path == []:
        path_nodes = [start]
        path = [(start, 0)]
    if start == end:
        return sum([x[1] for x in path])
    vals = [0]
    for next_cell in graph[start]:
        if next_cell[0] in path_nodes:
            continue
        dist = longest_path(graph, next_cell[0], end, path_nodes + [next_cell[0]], path + [next_cell])
        vals.append(dist)
    return max(vals)


def part1():
    f = open("input.txt", 'r')
    out = f.read().split('\n')

    start = out[0].index('.')
    end = out[-1].index('.') + (len(out) - 1) * 1j

    grid = {complex(x, y): v for y, row in enumerate(out) for x, v in enumerate(row)}
    graph = condense_grid(grid, start, end)
    path = longest_path(graph, start, end)
    print(path)   


def part2():
    f = open("input.txt", 'r')
    out = f.read().split('\n')
    
    start = out[0].index('.')
    end = out[-1].index('.') + (len(out) - 1) * 1j
    
    grid = {complex(x, y): v for y, row in enumerate(out) for x, v in enumerate(row)}
    for node in grid:
        if grid[node] in '^v<>':
            grid[node] = '.'
    
    graph = condense_grid(grid, start, end)
    path = longest_path(graph, start, end)
    print(path)

                    

part1()

start = time.time()
part2()
print(time.time() - start)