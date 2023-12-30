class Brick():
    def __init__(self, id, x1, y1, z1, x2, y2, z2):
        self.id = id
        self.x1 = x1
        self.y1 = y1
        self.z1 = z1
        self.x2 = x2 + 1
        self.y2 = y2 + 1
        self.z2 = z2 + 1

def part1():
    f = open("input.txt", 'r')
    out = f.read().split('\n')

    bricks = []
    for i in range(len(out)):
        brick_left, brick_right = out[i].split('~')
        brick_left = brick_left.split(',')
        brick_right = brick_right.split(',')
        brick = brick_left + brick_right
        if int(brick[0]) > int(brick[3]):
            brick[0], brick[3] = brick[3], brick[0]
        if int(brick[1]) > int(brick[4]):
            brick[1], brick[4] = brick[4], brick[1]
        if int(brick[2]) > int(brick[5]):
            brick[2], brick[5] = brick[5], brick[2]
        bricks.append(Brick(i, int(brick[0]), int(brick[1]), int(brick[2]), int(brick[3]), int(brick[4]), int(brick[5])))
            
    bricks.sort(key=lambda x: x.z1)
    i = 0
    lowest_z_coords = {}
    supports = {brick.id: set() for brick in bricks}
    supported_by = {brick.id: set() for brick in bricks}
    while i < len(bricks):
        brick = bricks[i]
        x, y  = brick.x1, brick.y1
        l, w, h = brick.x2 - brick.x1, brick.y2 - brick.y1, brick.z2 - brick.z1
        lowest_z = 0
        lowest_z_ids = set()
        for j in range(x, x + l):
            for k in range(y, y + w):
                if lowest_z_coords.get((j, k), (1, None))[0] > lowest_z:
                    lowest_z = lowest_z_coords.get((j, k), (1, None))[0]
                    lowest_z_ids = {lowest_z_coords.get((j, k), (1, None))[1]}
                elif lowest_z_coords.get((j, k), (1, None))[0] == lowest_z:
                    lowest_z_ids.add(lowest_z_coords.get((j, k), (1, None))[1])

        if None in lowest_z_ids:
            lowest_z_ids.remove(None)
        if len(lowest_z_ids) != 0:
            supported_by[brick.id] = lowest_z_ids
            for lowest_z_id in lowest_z_ids:
                supports[lowest_z_id].add(brick.id)
        brick.z1 = lowest_z
        brick.z2 = brick.z1 + h
        for j in range(x, x + l):
            for k in range(y, y + w):
                lowest_z_coords[(j, k)] = (brick.z2, brick.id)
        i += 1
    
    not_removable = set()
    for brick in bricks:
        if len(supported_by[brick.id]) == 1:
            not_removable.add(supported_by[brick.id].pop())
    removable = {brick.id for brick in bricks} - not_removable
    print(len(removable))
    

def part2():
    f = open("input.txt", 'r')
    out = f.read().split('\n')

    bricks = []
    for i in range(len(out)):
        brick_left, brick_right = out[i].split('~')
        brick_left = brick_left.split(',')
        brick_right = brick_right.split(',')
        brick = brick_left + brick_right
        if int(brick[0]) > int(brick[3]):
            brick[0], brick[3] = brick[3], brick[0]
        if int(brick[1]) > int(brick[4]):
            brick[1], brick[4] = brick[4], brick[1]
        if int(brick[2]) > int(brick[5]):
            brick[2], brick[5] = brick[5], brick[2]
        bricks.append(Brick(i, int(brick[0]), int(brick[1]), int(brick[2]), int(brick[3]), int(brick[4]), int(brick[5])))
            
    bricks.sort(key=lambda x: x.z1)
    i = 0
    lowest_z_coords = {}
    supports = {brick.id: set() for brick in bricks}
    supported_by = {brick.id: set() for brick in bricks}
    while i < len(bricks):
        brick = bricks[i]
        x, y  = brick.x1, brick.y1
        l, w, h = brick.x2 - brick.x1, brick.y2 - brick.y1, brick.z2 - brick.z1
        lowest_z = 0
        lowest_z_ids = set()
        for j in range(x, x + l):
            for k in range(y, y + w):
                if lowest_z_coords.get((j, k), (1, None))[0] > lowest_z:
                    lowest_z = lowest_z_coords.get((j, k), (1, None))[0]
                    lowest_z_ids = {lowest_z_coords.get((j, k), (1, None))[1]}
                elif lowest_z_coords.get((j, k), (1, None))[0] == lowest_z:
                    lowest_z_ids.add(lowest_z_coords.get((j, k), (1, None))[1])

        if None in lowest_z_ids:
            lowest_z_ids.remove(None)
        if len(lowest_z_ids) != 0:
            supported_by[brick.id] = lowest_z_ids
            for lowest_z_id in lowest_z_ids:
                supports[lowest_z_id].add(brick.id)
        brick.z1 = lowest_z
        brick.z2 = brick.z1 + h
        for j in range(x, x + l):
            for k in range(y, y + w):
                lowest_z_coords[(j, k)] = (brick.z2, brick.id)
        i += 1

    bricks.sort(key=lambda x: x.z1)
    total = 0
    for removed_brick in bricks:
        falling = {brick.id: False for brick in bricks}
        falling[removed_brick.id] = True
        count = 0
        falling_queue = [removed_brick.id]
        while len(falling_queue) != 0:
            brick = falling_queue.pop(0)
            for supported_brick in supports[brick]:
                if all(falling[supported_by_brick] for supported_by_brick in supported_by[supported_brick]):
                    if not falling[supported_brick]:
                        falling_queue.append(supported_brick)
                        falling[supported_brick] = True
                        count += 1
        total += count
            
    print(total)


                    

part1()
part2()