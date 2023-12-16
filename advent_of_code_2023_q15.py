def hash_val(string):
    val = 0
    for c in string:
        val += ord(c)
        val = (val * 17) % 256
    return val

def part1():
    f = open("input.txt", 'r')
    out = f.read().split('\n')

    instructions = out[0].split(',')
    total = 0
    for instruction in instructions:
        total += hash_val(instruction)
    print(total)

def part2():
    f = open("input.txt", 'r')
    out = f.read().split('\n')

    instructions = out[0].split(',')
    boxes = [dict() for _ in range(256)]
    for instruction in instructions:
        if '-' in instruction:
            seq, op, num = instruction[:-1], instruction[-1], 0
        else:
            seq, num = instruction.split('=')
            op = '='
        label = hash_val(seq)
        if op == '-':
            # remove from dict if it exists
            if seq in boxes[label]:
                del boxes[label][seq]
        else:
            boxes[label][seq] = int(num)
    total = 0
    for box_ind, box in enumerate(boxes):
        ind = 0
        for key in box:
            total += box[key] * (ind + 1) * (box_ind + 1)
            ind += 1
    print(total)



part1()
part2()