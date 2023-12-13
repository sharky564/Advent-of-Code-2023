
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return (a * b) // gcd(a, b)


def part1():
    f = open("input.txt", 'r')
    out = f.read().split('\n')
    seq = out[0]

    vals = {}
    i = 2
    while i < len(out):
        node, left_right = out[i].split(' = ')
        left, right = left_right[1:-1].split(', ')
        vals[node] = [left, right]
        i += 1
    
    curr_key = 'AAA'
    iteration = 0
    while curr_key != 'ZZZ':
        iteration += 1
        for char in seq:
            if char == 'L':
                curr_key = vals[curr_key][0]
            else:
                curr_key = vals[curr_key][1]
    
    print(iteration * len(seq))
    

def part2():
    f = open("input.txt", 'r')
    out = f.read().split('\n')
    seq = out[0]

    vals = {}
    i = 2
    while i < len(out):
        node, left_right = out[i].split(' = ')
        left, right = left_right[1:-1].split(', ')
        vals[node] = [left, right]
        i += 1


    curr_nodes = [key for key in vals.keys() if key[-1] == 'A']
    periods = []
    count = 0
    for key in curr_nodes:
        curr_key = key
        iteration = 0
        while curr_key[-1] != 'Z':
            iteration += 1
            for char in seq:
                if char == 'L':
                    curr_key = vals[curr_key][0]
                else:
                    curr_key = vals[curr_key][1]
        periods.append(iteration)

    out = 1
    for num in periods:
        out = lcm(out, num)

    print(out * len(seq))


part1()
part2()