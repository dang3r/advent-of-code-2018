from collections import deque

l = open('09_input.txt').read().strip().split(' ')
players = int(l[0])
last_mb = int(l[-2])

current = 0
marbles =deque([0])
scores = [0 for i in range(players)]

for i in range(1, (last_mb*100) +1):
    print(i)
    player = (i - 1) % players
    marble_worth = 0
    if i % 23 == 0:
        marble_worth += i
        marble_worth += marbles[current - 7]
        del marbles[current - 7]
        # Special handling if you wrap around
        if current - 7 >= 0:
            current = current - 7
        else:
            current = (current - 6) % len(marbles)
    else:
        nxt = (current + 2) % len(marbles)
        marbles.insert(nxt, i)
        current = nxt
    scores[player] += marble_worth
    #print(scores[player])
print(max(scores))
