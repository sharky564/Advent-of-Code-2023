f = open("aoc_2023_day_7.txt", 'r')
out = f.read().split('\n')

ranks = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
def cmp(a):
    if a == 'A':
        return 14
    elif a == 'K':
        return 13
    elif a == 'Q':
        return 12
    elif a == 'J':
        return 1
    elif a == 'T':
        return 10
    else:
        return int(a)

for line in out:
    hand, bid = line.split()
    hand = list(hand)
    bid = int(bid)
    hand_without_joker = [x for x in hand if x != 'J']
    num_jokers = len(hand) - len(hand_without_joker)
    if num_jokers == 5:
        ranks[0].append((hand, bid))
    else:
        hand_without_joker = sorted(hand_without_joker, key=lambda x: (hand_without_joker.count(x), cmp(x)), reverse=True)
        # jokers become the highest card in the hand
        working_hand = [hand_without_joker[0]] * num_jokers + hand_without_joker
        if working_hand[0] == working_hand[4]:
            ranks[0].append((hand, bid))
        elif working_hand[0] == working_hand[3]:
            ranks[1].append((hand, bid))
        elif working_hand[0] == working_hand[2] and working_hand[3] == working_hand[4]:
            ranks[2].append((hand, bid))
        elif working_hand[0] == working_hand[2]:
            ranks[3].append((hand, bid))
        elif working_hand[0] == working_hand[1] and working_hand[2] == working_hand[3]:
            ranks[4].append((hand, bid))
        elif working_hand[0] == working_hand[1]:
            ranks[5].append((hand, bid))
        else:
            ranks[6].append((hand, bid))
    
    

ranks[0].sort(key=lambda x: tuple(map(cmp, x[0])), reverse=True)
ranks[1].sort(key=lambda x: tuple(map(cmp, x[0])), reverse=True)
ranks[2].sort(key=lambda x: tuple(map(cmp, x[0])), reverse=True)
ranks[3].sort(key=lambda x: tuple(map(cmp, x[0])), reverse=True)
ranks[4].sort(key=lambda x: tuple(map(cmp, x[0])), reverse=True)
ranks[5].sort(key=lambda x: tuple(map(cmp, x[0])), reverse=True)
ranks[6].sort(key=lambda x: tuple(map(cmp, x[0])), reverse=True)

# # print ranks
# for i in range(7):
#     print(i, ranks[i])

# concatenate all the ranks
all_ranks = []
for i in range(7):
    all_ranks += ranks[i]

all_ranks = all_ranks[::-1]
total = 0
i = 1
while i <= len(all_ranks):
    total += i * all_ranks[i-1][1]
    print(i, ''.join(all_ranks[i-1][0]), all_ranks[i-1][1], total)
    i += 1

print(total)