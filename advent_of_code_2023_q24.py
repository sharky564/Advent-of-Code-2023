class Vector:
    '''
    Class object for 3D vectors.
    '''
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    # vector addition
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    
    # vector subtraction
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
    
    # scalar multiplication
    def __mul__(self, other):
        return Vector(self.x * other, self.y * other, self.z * other)
    
    # scalar division
    def __truediv__(self, other):
        return Vector(self.x / other, self.y / other, self.z / other)
    
    def __repr__(self):
        return f"({self.x}, {self.y}, {self.z})"

def dot_product(vec1, vec2):
    return vec1.x * vec2.x + vec1.y * vec2.y + vec1.z * vec2.z

def cross_product(vec1, vec2):
    return Vector(vec1.y * vec2.z - vec1.z * vec2.y,
                  vec1.z * vec2.x - vec1.x * vec2.z,
                  vec1.x * vec2.y - vec1.y * vec2.x)

def determinant(vec1, vec2, vec3):
    return dot_product(vec1, cross_product(vec2, vec3))

def transpose(array: list[Vector]):
    return [Vector(*[row.x for row in array]),
            Vector(*[row.y for row in array]),
            Vector(*[row.z for row in array])]

def inverse_matrix(array):
    # gets inverse for 3x3 matrix
    row1, row2, row3 = array
    if determinant(row1, row2, row3) == 0:
        return None
    else:
        val = [cross_product(row2, row3) / determinant(row1, row2, row3),
                cross_product(row3, row1) / determinant(row1, row2, row3),
                cross_product(row1, row2) / determinant(row1, row2, row3)]
        return transpose(val)


def intersect(hailstone1, hailstone2, lower_bound, upper_bound):
    x1, y1, z1, vx1, vy1, vz1 = hailstone1
    x2, y2, z2, vx2, vy2, vz2 = hailstone2
    if vx1 * vy2 == vy1 * vx2:
        if (x1 - x2) * vy1 == (y1 - y2) * vx1:
            if abs((x1 + 0.001 * vx1) - (x2 + 0.001 * vx2)) >= abs(x1 - x2):
                return False
            elif abs((y1 + 0.001 * vy1) - (y2 + 0.001 * vy2)) >= abs(y1 - y2):
                return False
            else:
                lbx, ubx = sorted([(lower_bound - x2) / (x1 - x2), (upper_bound - x2) / (x1 - x2)])
                lby, uby = sorted([(lower_bound - y2) / (y1 - y2), (upper_bound - y2) / (y1 - y2)])
                if lbx > uby or lby > ubx:
                    return False
                else:
                    return True
        else:
            return False
    else:
        int_x = (vx2 * (y1 * vx1 - x1 * vy1) - vx1 * (y2 * vx2 - x2 * vy2)) / (vx1 * vy2 - vy1 * vx2)
        int_y = (vy2 * (y1 * vx1 - x1 * vy1) - vy1 * (y2 * vx2 - x2 * vy2)) / (vx1 * vy2 - vy1 * vx2)
        if (int_x - x1) / vx1 < 0 or (int_x - x2) / vx2 < 0:
            return False
        elif (int_y - y1) / vy1 < 0 or (int_y - y2) / vy2 < 0:
            return False
        elif int_x < lower_bound or int_x > upper_bound or int_y < lower_bound or int_y > upper_bound:
            return False
        else:
            return True
    

def part1():
    f = open("input.txt", 'r')
    out = f.read().split('\n')

    hailstones = []
    for line in out:
        line = line.replace('@', ',')
        x, y, z, vx, vy, vz = map(int, line.split(','))
        hailstones.append((x, y, z, vx, vy, vz))
    
    count = 0
    lower_bound = 200000000000000
    upper_bound = 400000000000000
    for i in range(len(hailstones)):
        for j in range(i + 1, len(hailstones)):
            t = intersect(hailstones[i], hailstones[j], lower_bound, upper_bound)
            if t:
                count += 1
    print(count)


def part2():
    f = open("input.txt", 'r')
    out = f.read().split('\n')

    hailstones = []
    for line in out:
        line = line.replace('@', ',')
        x, y, z, vx, vy, vz = map(int, line.split(','))
        hailstones.append((x, y, z, vx, vy, vz))
    
    pos1, vel1 = Vector(*hailstones[0][:3]), Vector(*hailstones[0][3:])
    pos2, vel2 = Vector(*hailstones[1][:3]), Vector(*hailstones[1][3:])
    pos3, vel3 = Vector(*hailstones[2][:3]), Vector(*hailstones[2][3:])

    vec_a1 = vel1 - vel2
    vec_b1 = cross_product(pos1, vel1) - cross_product(pos2, vel2)
    vec_c1 = pos1 - pos2

    vec_a2 = vel1 - vel3
    vec_b2 = cross_product(pos1, vel1) - cross_product(pos3, vel3)
    vec_c2 = pos1 - pos3
    
    vec_a3 = vel2 - vel3
    vec_b3 = cross_product(pos2, vel2) - cross_product(pos3, vel3)
    vec_c3 = pos2 - pos3

    coeff_mat = [cross_product(vec_a1, vec_c1), cross_product(vec_a2, vec_c2), cross_product(vec_a3, vec_c3)]
    const_vec = Vector(dot_product(vec_b1, vec_c1), dot_product(vec_b2, vec_c2), dot_product(vec_b3, vec_c3))
    p = Vector(*[int(dot_product(const_vec, row)) for row in inverse_matrix(coeff_mat)])
    
    print(p.x + p.y + p.z)
    


part1()
part2()