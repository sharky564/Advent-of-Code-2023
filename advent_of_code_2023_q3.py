f = open("input.txt", 'r')
out = f.read().split('\n')
lines = [list(line) for line in out]
for line in lines:
    i = 0
    num = False
    beg_ind = -1
    curr_num = ''
    while i < len(line):
        if line[i].isdigit():
            if not num:
                beg_ind = i
                num = True
            curr_num += line[i]
        else:
            if num:
                num = False
                for j in range(beg_ind, i):
                    line[j] = int(curr_num)
                curr_num = ''
        i += 1
    if num:
        for j in range(beg_ind, i):
            line[j] = int(curr_num)
        curr_num = ''


m = len(lines)
n = len(lines[0])
total = 0
for i in range(m):
    for j in range(n):
        if lines[i][j] == '*':
            adj_squares = [(x, y) for x in range(-1, 2) for y in range(-1, 2) if 0 <= i + x < m and 0 <= j + y < n and (x, y) != (0, 0)]
            nums = []
            prev_sq = False
            for x, y in adj_squares:
                if type(lines[i + x][j + y]) == int:
                    if not prev_sq:
                        nums.append(lines[i + x][j + y])
                        if (x, y) in [(-1, -1), (-1, 0), (1, -1), (1, 0)]:
                            prev_sq = True
                else:
                    prev_sq = False
            if len(nums) == 2:
                total += nums[0] * nums[1]
            
print(total)