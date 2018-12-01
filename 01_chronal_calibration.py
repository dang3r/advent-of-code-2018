import sys

def changes():
    return [int(line) for line in open('01_input.txt')]

def prefix_array(a):
    p = [a[0]]
    for i in range(1, len(a)):
        p.append(p[-1] + a[i])
    return p

def pair(a, divisor):
    """Find a pair of numbers divisble by divisor.
    Return the indices of the pair with the smallest quotient"""
    rs = []
    for i in range(0, len(a) - 1):
        for j in range(i + 1, len(a)):
            if abs(a[j] - a[i]) % divisor == 0:
                quotient = abs(a[j] - a[i]) / divisor
                if not rs:
                    rs = (i, j)
                elif quotient < (abs(a[rs[0]] - a[rs[1]]) / divisor):
                    rs = (i, j)
    return rs

# Part 1
c = changes()
c_sum = sum(c)
print(f'Sum is {c_sum}')

# Part 2
p = prefix_array(c)
i, j = pair(p, c_sum)
diff = abs(p[j] - p[i])
quotient = diff / c_sum
print(f'Pair is ({i},{j}) with quotient {quotient}')
print(f'Answer is {p[max(i, j)]}')
sys.exit(1)

# Old Part 2
i = 0
total = 0
length = len(changes)
frequency = set([total])
while True:
    print(i, changes[i])
    total += changes[i]
    if total in frequency:
        print(total)
        print('here')
        break
    i = (i + 1) % length
