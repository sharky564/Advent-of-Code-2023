def move_west(grid):
    ind = 0
    while ind < len(grid):
        row = grid[ind]
        new_row = []
        i = 0
        while i < len(row):
            if row[i] == 'O':
                new_row.append('O')
            elif row[i] == '#':
                j = len(new_row)
                while j < i:
                    new_row.append('.')
                    j += 1
                new_row.append('#')
            i += 1
        j = len(new_row)
        while j < len(row):
            new_row.append('.')
            j += 1
        grid[ind] = new_row
        ind += 1


def part1():
    f = open("input.txt", 'r')
    out = f.read().split('\n')

    grid = []
    for line in out:
        grid.append(list(line))
    
    grid = list(map(list, zip(*grid)))
    move_west(grid)
    grid = list(map(list, zip(*grid)))
    n = len(grid)
    total = 0
    for i in range(n):
        total += (n - i) * grid[i].count('O')
    print(total)


def spin(grid):
    new_grid = list(map(list, zip(*grid)))
    move_west(new_grid)
    new_grid = list(map(list, zip(*new_grid)))
    move_west(new_grid)
    new_grid = list(map(lambda x: list(x)[::-1], zip(*new_grid)))
    move_west(new_grid)
    new_grid = list(map(lambda x: list(x)[::-1], zip(*map(lambda x: x[::-1], new_grid))))
    move_west(new_grid)
    new_grid = list(map(lambda x: list(x)[::-1], new_grid))
    return new_grid
    

def part2():
    f = open("input.txt", 'r')
    out = f.read().split('\n')

    grid = []
    for line in out:
        grid.append(list(line))
    
    new_grid = spin(grid)
    i = 1
    seen_grids = dict()
    seen_grids[tuple(map(tuple, grid))] = 0

    while tuple(map(tuple, new_grid)) not in seen_grids:
        seen_grids[tuple(map(tuple, new_grid))] = i
        grid = new_grid
        new_grid = spin(grid)
        i += 1
    
    val = seen_grids[tuple(map(tuple, new_grid))]
    # print(i, val)
    period = i - val
    # print(period)
    res = ((1000000000 - val) % period) + val
    for key, value in seen_grids.items():
        if value == res:
            grid = list(map(list, key))
            n = len(grid)
            total = 0
            for i in range(n):
                total += (n - i) * grid[i].count('O')
            print(total)
            break

part1()
part2()