from itertools import accumulate
import sys

def changes(input_file='01_input.txt'):
    """Return a list of frequency changes"""
    return [int(line) for line in open(input_file)]


def pair(a, divisor):
    """Find a pair of numbers in a divisble by divisor.
    Return the indices of the pair in a with the smallest quotient"""
    quotient = lambda x, y: abs(x -y) / divisor
    indices = None
    for i in range(0, len(a) - 1):
        for j in range(i + 1, len(a)):
            if abs(a[j] - a[i]) % divisor == 0:
                if not indices:
                    indices = (i, j)
                elif quotient(a[i], a[j]) < quotient(a[indices[0]], a[indices[1]]):
                    indices = (i, j)
    return indices

# Part 1
c = changes()
c_sum = sum(c)
print(f'Sum is {c_sum}')

# Part 2
p = list(accumulate(c))
i, j = pair(p, c_sum)
diff = abs(p[i] - p[j])
quotient = diff / c_sum
print(f'Pair is ({i},{j}) with quotient {quotient}')
print(f'Answer is {p[max(i, j)]}')
