
def part1():
    f = open("input.txt", 'r')
    out = f.read().split('\n')

    total = 0
    i = 0
    while i < len(out):
        grid = []
        while i < len(out) and out[i] != '':
            grid.append(out[i])
            i += 1

        reflection_found = False
        lower_bound = 1
        while lower_bound < len(grid):
            num_above = lower_bound
            num_below = len(grid) - lower_bound
            if num_above <= num_below:
                if grid[:num_above] == grid[num_above*2-1:num_above-1:-1]:
                    reflection_found = True
                    break
            else:
                if grid[-num_below:] == grid[-num_below-1:-num_below*2-1:-1]:
                    reflection_found = True
                    break
            lower_bound += 1

        if reflection_found:
            total += 100 * lower_bound

        else:
            grid = list(map(list, zip(*grid)))
            for j in range(len(grid)):
                grid[j] = ''.join(grid[j])
            lower_bound = 1
            while lower_bound < len(grid):
                num_above = lower_bound
                num_below = len(grid) - lower_bound
                if num_above <= num_below:
                    if grid[:num_above] == grid[num_above*2-1:num_above-1:-1]:
                        reflection_found = True
                        break
                else:
                    if grid[-num_below:] == grid[-num_below-1:-num_below*2-1:-1]:
                        reflection_found = True
                        break
                lower_bound += 1

            total += lower_bound

        i += 1

    print(total)


def check(a, b):
    diff = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            diff += 1
        if diff > 1:
            return False
    return diff == 1

def part2():
    f = open("input.txt", 'r')
    out = f.read().split('\n')

    total = 0
    i = 0
    while i < len(out):
        grid = []
        while i < len(out) and out[i] != '':
            grid.append(out[i])
            i += 1

        reflection_found = False
        lower_bound = 1
        while lower_bound < len(grid):
            num_above = lower_bound
            num_below = len(grid) - lower_bound
            if num_above <= num_below:
                above = ''.join(grid[:num_above])
                below = ''.join(grid[num_above*2-1:num_above-1:-1])
                if check(above, below):
                    reflection_found = True
                    break
            else:
                above = ''.join(grid[-num_below:])
                below = ''.join(grid[-num_below-1:-num_below*2-1:-1])
                if check(above, below):
                    reflection_found = True
                    break
            lower_bound += 1

        if reflection_found:
            total += 100 * lower_bound

        else:
            grid = list(map(list, zip(*grid)))
            for j in range(len(grid)):
                grid[j] = ''.join(grid[j])
            lower_bound = 1
            while lower_bound < len(grid):
                num_above = lower_bound
                num_below = len(grid) - lower_bound
                if num_above <= num_below:
                    above = ''.join(grid[:num_above])
                    below = ''.join(grid[num_above*2-1:num_above-1:-1])
                    if check(above, below):
                        reflection_found = True
                        break
                else:
                    above = ''.join(grid[-num_below:])
                    below = ''.join(grid[-num_below-1:-num_below*2-1:-1])
                    if check(above, below):
                        reflection_found = True
                        break
                lower_bound += 1

            total += lower_bound

        i += 1

    print(total)

part1()
part2()