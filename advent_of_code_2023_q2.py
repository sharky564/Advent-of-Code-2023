f = open("Advent of Code/aoc_2023_day_2.txt", 'r')
out = f.read().split('\n')
total = 0
for line in out:
    game, draws = line.split(':')
    id = int(game.split()[1])
    draws = draws.split(';')
    draws = [draw.split(',') for draw in draws]
    draws = [[tup.split() for tup in draw] for draw in draws]
    red = 0
    green = 0
    blue = 0
    for draw in draws:
        for tup in draw:
            if tup[1] == 'red':
                red = max(red, int(tup[0]))
            elif tup[1] == 'green':
                green = max(green, int(tup[0]))
            elif tup[1] == 'blue':
                blue = max(blue, int(tup[0]))
    total += red * green * blue
print(total)