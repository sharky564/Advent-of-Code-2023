f = open("input.txt", 'r')
out = f.read().split('\n')
total = 0
num_cards = [1 for _ in range(len(out))]
for line in out:
    win, nums = line.split(':')[1].split('|')
    win = win.split()
    nums = nums.split()
    x = num_cards[0]
    total += x
    num_cards = num_cards[1:]
    new_cards = len([x for x in nums if x in win])
    for i in range(new_cards):
        num_cards[i] += x
    print(total)

print(total)