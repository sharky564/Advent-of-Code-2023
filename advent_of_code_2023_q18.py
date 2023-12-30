def shoelace(points):
    return abs(sum([(points[i - 1][0] - points[i][0]) * points[i][1] for i in range(len(points))]))

def part1():
    f = open("input.txt", 'r')
    out = f.read().split('\n')
    
    x, y = 0, 0
    coords = [(0, 0)]
    point_count = 0
    for line in out:
        d, n, c = line.split()
        n = int(n)
        point_count += n
        if d == 'R':
            y += n
        elif d == 'L':
            y -= n
        elif d == 'U':
            x -= n
        elif d == 'D':
            x += n
        coords.append((x, y))
        
    print(shoelace(coords) + point_count // 2 + 1)
    


def part2():
    f = open("input.txt", 'r')
    out = f.read().split('\n')
    
    x, y = 0, 0
    coords = [(0, 0)]
    point_count = 0
    for line in out:
        c = line.split()[2]
        c = c[2:-1]
        d, n = c[-1], c[:-1]
        n = int(n, 16)
        d = 'RDLU'[int(d)]
        point_count += n
        if d == 'R':
            y += n
        elif d == 'L':
            y -= n
        elif d == 'U':
            x -= n
        elif d == 'D':
            x += n
        coords.append((x, y))
        
    print(shoelace(coords) + point_count // 2 + 1)

part1()
part2()