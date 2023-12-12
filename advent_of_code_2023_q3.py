f = open("input.txt", 'r')
out = f.read().split('\n')

def part1():
    lines = [list(line) for line in out]
    total = 0
    for line_ind, line in enumerate(lines):
        i = 0
        num = False
        beg_ind = -1
        curr_num = ''
        while i < len(line) + 1:
            if i == len(line) or not line[i].isdigit():
                if num:
                    num = False
                    int_num = int(curr_num)
                    j = beg_ind
                    while j < i:
                        adj_row = -1
                        while adj_row < 2:
                            adj_col = -1
                            while adj_col < 2:
                                if 0 <= line_ind + adj_row < len(lines) and 0 <= j + adj_col < len(line[0]):
                                    if lines[line_ind + adj_row][j + adj_col] != '.' and not lines[line_ind + adj_row][j + adj_col].isdigit():
                                        print(int_num)
                                        total += int_num
                                        adj_col = 2
                                        adj_row = 2
                                        j = i
                                adj_col += 1
                            adj_row += 1
                        j += 1
                    curr_num = ''
            else:
                if not num:
                    beg_ind = i
                    num = True
                curr_num += line[i]
            i += 1
    print(total)
    
    


def part2():
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

part1()
part2()