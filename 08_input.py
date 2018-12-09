import sys

l = list(map(int, open('08_input.txt').read().strip().split(' ')))
s = 0
def go(i):
    global s
    size_children = l[i]
    size_metadata = l[i+1]
    nxt = i + 2
    for i in range(size_children):
        nxt = go(nxt)
    s += sum(l[nxt: nxt + size_metadata])
    nxt = nxt + size_metadata
    return nxt
print(go(0))
print(s)

sys.setrecursionlimit(10000)

def go2(i):
    print(i)
    size_children = l[i]
    size_metadata = l[i+1]
    nxt = i + 2
    if not size_children:
        return (nxt+size_metadata, sum(l[nxt :nxt+size_metadata]))

    sums = []
    for _ in range(size_children):
        nxt, s = go2(nxt)
        sums.append(s)

    s = 0
    for i in range(nxt, nxt+size_metadata):
        m = l[i]
        if m <= len(sums):
            s += sums[m - 1]

    nxt = nxt + size_metadata
    return (nxt, s)
print(go2(0))
