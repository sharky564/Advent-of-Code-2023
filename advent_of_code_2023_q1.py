def part1():
    f = open("input.txt", 'r')
    out = f.read().split('\n')
    total = 0
    for line in out:
        found_first_digit = False
        first_digit = 0
        i = 0
        while i < len(line) and not found_first_digit:
            if line[i].isdigit():
                first_digit = int(line[i])
                found_first_digit = True
            i += 1
        
        if not found_first_digit:
            continue
        
        found_second_digit = False
        second_digit = 0
        i = len(line) - 1
        while i >= 0 and not found_second_digit:
            if line[i].isdigit():
                second_digit = int(line[i])
                found_second_digit = True
            i -= 1
        if not found_second_digit:
            continue

        if found_first_digit and found_second_digit:
            total += 10 * first_digit + second_digit

    print(total)

def part2():
    f = open("input.txt", 'r')
    out = f.read().split('\n')
    total = 0
    nums = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
    for line in out:
        found_first_digit = False
        first_digit = 0
        i = 0
        while i < len(line) and not found_first_digit:
            if line[i].isdigit():
                first_digit = int(line[i])
                found_first_digit = True
            else:
                for key, val in nums.items():
                    if line[i:i+len(val)] == val:
                        first_digit = key
                        found_first_digit = True
                        break
            i += 1
        
        if not found_first_digit:
            continue
        
        found_second_digit = False
        second_digit = 0
        i = len(line) - 1
        while i >= 0 and not found_second_digit:
            if line[i].isdigit():
                second_digit = int(line[i])
                found_second_digit = True
            else:
                for key, val in nums.items():
                    if line[i-len(val)+1:i+1] == val:
                        second_digit = key
                        found_second_digit = True
                        break
            i -= 1
        if not found_second_digit:
            continue

        if found_first_digit and found_second_digit:
            total += 10 * first_digit + second_digit

    print(total)


part1()
part2()