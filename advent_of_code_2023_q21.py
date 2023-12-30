def part1():
    f = open("input.txt", 'r')
    out = f.read().split('\n')

    grid = {complex(x, y): v for y, row in enumerate(out) for x, v in enumerate(row)}
    directions = [1, -1, 1j, -1j]
    start = [k for k, v in grid.items() if v == 'S'][0]
    grid[start] = '.'
    open_squares = {start}
    for _ in range(64):
        open_squares = {coord + d for coord in open_squares for d in directions if coord + d in grid and grid[coord + d] == '.'}
    print(len(open_squares))

def part2():
    f = open("input.txt", 'r')
    out = f.read().split('\n')

    grid = {complex(x, y): v for y, row in enumerate(out) for x, v in enumerate(row)}
    directions = [1, -1, 1j, -1j]
    start = [k for k, v in grid.items() if v == 'S'][0]
    grid[start] = '.'
    N = 26501365
    num_cells = N // 131
    
    reachable = {start}
    for _ in range(len(out)):
        reachable = {coord + d for coord in reachable for d in directions + [0] if coord + d in grid and grid[coord + d] == '.'}
    
    even_reachable = {start}
    odd_reachable = {}
    for i in range(len(out)):
        if i % 2 == 0:
            odd_reachable = {coord + d for coord in even_reachable for d in directions if coord + d in grid and grid[coord + d] == '.'}
        else:
            even_reachable = {coord + d for coord in odd_reachable for d in directions if coord + d in grid and grid[coord + d] == '.'}

    central_region = {start}
    for _ in range(len(out)//2):
        central_region = {coord + d for coord in central_region for d in directions + [0] if coord + d in grid and grid[coord + d] == '.'}
    central_even_region = central_region & even_reachable
    central_odd_region = central_region & odd_reachable

    num_odd_centrals = (num_cells + 1) ** 2
    num_even_centrals = num_cells ** 2
    num_corners = num_cells * (num_cells + 1)

    total = num_even_centrals * len(central_even_region) + num_odd_centrals * len(central_odd_region) + num_corners * len(reachable - central_region)
    print(total)


part1()
part2()