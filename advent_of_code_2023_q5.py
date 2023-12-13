def part1():
    f = open("input.txt", 'r')
    out = f.read().split('\n')
    seeds = [int(x) for x in out[0].split()[1:]]

    curr_line_ind = 3
    maps = []
    while curr_line_ind < len(out):
        curr_map = {}
        while curr_line_ind < len(out) and out[curr_line_ind] != '' and out[curr_line_ind][0].isdigit():
            line = list(map(int, out[curr_line_ind].split()))
            curr_map[line[1]] = [line[0], line[2]]
            curr_line_ind += 1
        
        curr_line_ind += 2
        maps.append(curr_map)

    vals = list(seeds)
    for i in range(len(maps)):
        curr_dict = maps[i]
        new_vals = []
        while len(vals) > 0:
            val = vals.pop(0)
            for key, value in curr_dict.items():
                if val < key + value[1] and key < val:
                    new_val = val + (value[0] - key)
                    new_vals.append(new_val)
                    break
            else:
                new_vals.append(val)
        vals = new_vals

    print(min(vals))


def part2():
    f = open("input.txt", 'r')
    out = f.read().split('\n')
    seeds = [int(x) for x in out[0].split()[1:]]
    seeds = list(zip(seeds[::2], seeds[1::2]))

    curr_line_ind = 3
    maps = []
    while curr_line_ind < len(out):
        curr_map = {}
        while curr_line_ind < len(out) and out[curr_line_ind] != '' and out[curr_line_ind][0].isdigit():
            line = list(map(int, out[curr_line_ind].split()))
            curr_map[line[1]] = [line[0], line[2]]
            curr_line_ind += 1
        
        curr_line_ind += 2
        maps.append(curr_map)

    vals = list(seeds)
    for i in range(len(maps)):
        curr_dict = maps[i]
        new_vals = []
        while len(vals) > 0:
            val = vals.pop(0)
            for key, value in curr_dict.items():
                if val[0] < key + value[1] and key < val[0] + val[1]:
                    left_bound = max(val[0], key)
                    right_bound = min(val[0] + val[1], key + value[1])
                    interval_size = right_bound - left_bound
                    new_left_bound = left_bound + (value[0] - key)
                    new_vals.append((new_left_bound, interval_size))
                    if val[0] < key:
                        vals.append((val[0], key - val[0]))
                    if val[0] + val[1] > key + value[1]:
                        vals.append((key + value[1], val[0] + val[1] - key - value[1]))
                    break
            else:
                new_vals.append(val)
        vals = new_vals
        # print(vals)

    print(min(vals)[0])


part1()
part2()