import math


def num_sols(time, dist):
    min_val = math.floor((time - math.sqrt(time**2 - 4*dist))/2) + 1
    max_val = math.ceil((time + math.sqrt(time**2 - 4*dist))/2) - 1
    return max_val - min_val + 1

def part1():
    f = open("input.txt", 'r')
    out = f.read().split('\n')
    times = list(map(int, out[0].split()[1:]))
    distances = list(map(int, out[1].split()[1:]))
    total = num_sols(times[0], distances[0])
    for i in range(1, len(times)):
        total *= num_sols(times[i], distances[i])
    print(total)

def part2():
    f = open("input.txt", 'r')
    out = f.read().split('\n')
    time = int(''.join(out[0].split()[1:]))
    distance = int(''.join(out[1].split()[1:]))
        
    print(num_sols(time, distance))

part1()
part2()