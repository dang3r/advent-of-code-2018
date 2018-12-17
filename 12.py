from collections import deque

lines = [l.strip() for l in open('12.txt').readlines()]
state = deque(lines[0].split(' ')[-1])
rules = {line[:5]: line[-1] for line in lines[2:]}

def string(iter):
    return ''.join(iter)


def run(it, char='.'):
    cnt = 0
    for i in it:
        if i == char:
            cnt += 1
        else:
            break
    return cnt

# 1, 2, 3, 4, 5, 6, 7
# 3, 4, 5, 6, 7, 1, 2
# 4, 5, 6, 7, 1, 2, 3
# 5, 6, 7, 1, 2, 3, 4

def generate(state, generations):
    state_set = set()
    middle = 0
    for i in range(generations):
        # Pad either side with empty pots
        l_count = run([state[j] for j in range(0, 5)], '.')
        r_count = run([state[j] for j in range(-1, -6, -1)], '.')
        #print(l_count, r_count)
        state.extendleft(['.' for _ in range(5 - l_count)])
        state.extend(['.' for _ in range(5 - r_count)])
        middle += 5 - l_count
        #input()
        
        memo = [state[0], state[1]]
        state.rotate(-2)
        for _ in range(0, len(state) - 4):
            section = string(memo + [state[0], state[1], state[2]])
            memo = [memo[1], state[0]]
            state[0] = rules[section]
            state.rotate(-1)
        state.rotate(-2)

    return state, middle

def pots(state, middle):
    indexes = [i for i in range(-middle, len(state) - middle)]
    return sum([i for c, i in zip(state, indexes) if c =='#'])


state, middle = generate(state, 20)
print(state, len(state), middle, pots(state, middle))

state, middle = generate(state, 50000)
print(pots(state, middle))


#state, middle = generate(state, 50000000000)
#indexes = [i for i in range(-middle, len(state) - middle)]
#print(sum([i for c, i in zip(state, indexes) if c =='#']))#