def part1():
    f = open("input.txt", 'r')
    out = f.read().split('\n')
    
    workflows = {}
    i = 0
    while out[i] != '':
        # print(out[i])
        name, vals = out[i].split('{')
        workflows[name] = vals[:-1].split(',')
        i += 1
    
    parts = []
    for line in out[i+1:]:
        vals = line[1:-1].split(',')
        out = {}
        for val in vals:
            key, value = val.split('=')
            out[key] = int(value)
        parts.append(out)

    # print(workflows)
    # print(parts)

    total = 0
    for part in parts:
        end = False
        curr_map = 'in'
        while not end:
            for cond in workflows[curr_map]:
                if ':' in cond:
                    condition, out_map = cond.split(':')
                    if '<' in condition:
                        key, value = condition.split('<')
                        if part[key] < int(value):
                            curr_map = out_map
                            break
                    elif '>' in condition:
                        key, value = condition.split('>')
                        if part[key] > int(value):
                            curr_map = out_map
                            break
                else:
                    curr_map = cond
                    break
            if curr_map == 'A' or curr_map == 'R':
                end = True
                if curr_map == 'A':
                    for key in part:
                        total += part[key]
    
    print(total)


def part2():
    f = open("input.txt", 'r')
    out = f.read().split('\n')
    
    workflows = {}
    i = 0
    while out[i] != '':
        name, vals = out[i].split('{')
        workflows[name] = vals[:-1].split(',')
        i += 1

    min_bounds = {'x': 1, 'm': 1, 'a': 1, 's': 1}
    max_bounds = {'x': 4000, 'm': 4000, 'a': 4000, 's': 4000}


    def num_parts(workflow, min_bounds, max_bounds):
        outs = []
        if any([min_bounds[key] > max_bounds[key] for key in min_bounds]):
            return 0
        working_min_bounds = min_bounds.copy()
        working_max_bounds = max_bounds.copy()
        for cond in workflows[workflow]:
            new_min_bounds = working_min_bounds.copy()
            new_max_bounds = working_max_bounds.copy()
            if ':' in cond:
                condition, out_map = cond.split(':')
                if '<' in condition:
                    key, value = condition.split('<')
                    new_max_bounds[key] = min(new_max_bounds[key], int(value) - 1)
                    working_min_bounds[key] = max(working_min_bounds[key], int(value))
                    if out_map == 'A':
                        out = 1
                        for key in new_min_bounds:
                            out *= max(0, new_max_bounds[key] - new_min_bounds[key] + 1)
                        outs.append(out)
                    elif out_map != 'R':
                        out = num_parts(out_map, new_min_bounds, new_max_bounds)
                        outs.append(out)
                elif '>' in condition:
                    key, value = condition.split('>')
                    new_min_bounds[key] = max(new_min_bounds[key], int(value) + 1)
                    working_max_bounds[key] = min(working_max_bounds[key], int(value))
                    if out_map == 'A':
                        out = 1
                        for key in new_min_bounds:
                            out *= max(0, new_max_bounds[key] - new_min_bounds[key] + 1)
                        outs.append(out)
                    elif out_map != 'R':
                        out = num_parts(out_map, new_min_bounds, new_max_bounds)
                        outs.append(out)
            else:
                if cond == 'A':
                    out = 1
                    for key in new_min_bounds:
                        out *= max(0, new_max_bounds[key] - new_min_bounds[key] + 1)
                    outs.append(out)
                elif cond != 'R':
                    out = num_parts(cond, new_min_bounds, new_max_bounds)
                    outs.append(out)
        total = sum(outs)
        return total
    
    print(num_parts('in', min_bounds, max_bounds))
    

part1()
part2()