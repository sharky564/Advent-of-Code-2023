from functools import cache

@cache
def num_sols(nums_to_fit, curr_vals):
    if len(nums_to_fit) == 0:
        if curr_vals.count('#') == 0:
            return 1
        else:
            return 0
    modified = curr_vals + '.'
    total = 0
    num_to_fit = nums_to_fit[0]
    i = 0
    while i < len(curr_vals):
        while i < len(curr_vals) and modified[i] == '.':
            i += 1
        j = i
        damaged_found = False
        while j < len(curr_vals) and modified[j] != '.':
            if modified[j] == '#':
                damaged_found = True
            if j - i + 1 >= num_to_fit:
                if modified[j - num_to_fit] == '#':
                    j = len(curr_vals)
                elif modified[j + 1] != '#':
                    total += num_sols(nums_to_fit[1:], curr_vals[j + 2:])
            j += 1
        if damaged_found:
            break
        i = j
    return total

def part1():
    f = open("input.txt", 'r')
    out = f.read().split('\n')

    total = 0
    for line in out:
        curr_val, nums_to_fit = line.split()
        nums_to_fit = tuple(map(int, nums_to_fit.split(',')))
        total += num_sols(nums_to_fit, curr_val)
    
    print(total)

def part2():
    f = open("input.txt", 'r')
    out = f.read().split('\n')

    total = 0
    for line in out:
        curr_val, nums_to_fit = line.split()
        nums_to_fit = tuple(map(int, nums_to_fit.split(',')))
        new_curr_val = '?'.join([curr_val for _ in range(5)])
        new_nums_to_fit = nums_to_fit * 5
        total += num_sols(new_nums_to_fit, new_curr_val)

    print(total)

part1()
part2()