import math

f = open("Advent of Code/aoc_2023_day_6.txt", 'r')
out = f.read().split('\n')

time = int(''.join(out[0].split()[1:]))
distance = int(''.join(out[1].split()[1:]))

def num_sols(time, dist):
    min_val = math.floor((time - math.sqrt(time**2 - 4*dist))/2) + 1
    max_val = math.ceil((time + math.sqrt(time**2 - 4*dist))/2) - 1
    return max_val - min_val + 1
    
print(num_sols(time, distance))