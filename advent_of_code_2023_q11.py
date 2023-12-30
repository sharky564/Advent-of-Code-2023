def solve(expansion_coeff, expansion_rows, expansion_cols, galaxies):
    total = 0
    i = 0
    while i < len(galaxies):
        galaxy1 = galaxies[i]
        j = i + 1
        while j < len(galaxies):
            galaxy2 = galaxies[j]
            dist_x = abs(galaxy1[0] - galaxy2[0]) + (expansion_coeff - 1) * sum(1 for row in range(min(galaxy1[0], galaxy2[0]), max(galaxy1[0], galaxy2[0])) if row in expansion_rows)
            dist_y = abs(galaxy1[1] - galaxy2[1]) + (expansion_coeff - 1) * sum(1 for col in range(min(galaxy1[1], galaxy2[1]), max(galaxy1[1], galaxy2[1])) if col in expansion_cols)
            dist = dist_x + dist_y
            total += dist
            j += 1
        i += 1
    return total

def part1():
    f = open("input.txt", 'r')
    out = f.read().split('\n')

    grid = [list(line) for line in out]
    expansion_rows = [i for i in range(len(grid)) if grid[i].count('.') == len(grid[0])]
    expansion_cols = [i for i in range(len(grid[0])) if [row[i] for row in grid].count('.') == len(grid)]

    galaxies = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '#':
                galaxies.append((i, j))

    print(solve(2, expansion_rows, expansion_cols, galaxies))


def part2():
    f = open("input.txt", 'r')
    out = f.read().split('\n')

    grid = [list(line) for line in out]
    expansion_rows = [i for i in range(len(grid)) if grid[i].count('.') == len(grid[0])]
    expansion_cols = [i for i in range(len(grid[0])) if [row[i] for row in grid].count('.') == len(grid)]


    galaxies = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '#':
                galaxies.append((i, j))

    print(solve(1000000, expansion_rows, expansion_cols, galaxies))


part1()
part2()