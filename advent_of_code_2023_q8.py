f = open("Advent of Code/aoc_2023_day_8.txt", 'r')
out = f.read().split('\n')

seq = out[0]

vals = {}
i = 2
while i < len(out):
    node, left_right = out[i].split(' = ')
    left, right = left_right[1:-1].split(', ')
    vals[node] = [left, right]
    i += 1

# print(vals)

# curr_nodes = [key for key in vals.keys() if key[-1] == 'A']
# seen = dict()
# count = 0
# iteration = 0
# while any(curr_node[-1] != 'Z' for curr_node in curr_nodes):
#     for i, curr_node in enumerate(curr_nodes):
#         if curr_node[-1] == 'Z':
#             if (i, curr_node) not in seen:
#                 seen[(i, curr_node)] = [iteration]
#             else:
#                 seen[(i, curr_node)].append(iteration)
#     count += len(seq)
#     for char in seq:
#         if char == 'R':
#             curr_nodes = [vals[curr_node][1] for curr_node in curr_nodes]
#         else:
#             curr_nodes = [vals[curr_node][0] for curr_node in curr_nodes]
#     total_valid = sum([curr_node[-1] == 'Z' for curr_node in curr_nodes])
#     iteration += 1
#     if iteration % 1000 == 0:
#         print(iteration, total_valid, seen)

print(len(seq) * 51954251329)