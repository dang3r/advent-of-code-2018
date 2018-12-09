i = {}  # Number of pointers to each node
v = {}  # Map from node to the nodes that depend on it
n = []
non_sources = set()
for line in open('07_input.txt'):
    tokens = line.split(' ')
    x = (tokens[1], tokens[-3])
    n.append((tokens[1], tokens[-3]))
    if x[0] not in v:
        v[x[0]] = set()
    if x[1] not in v:
        v[x[1]] = set()
    i[x[1]] = i.get(x[1], 0) + 1
    v[x[0]].add(x[1])
    non_sources.add(x[1])

# Nodes that no one points to
sources = set([x[0] for x in n]) - non_sources

work = [[0,0] for i in range(4)]
l = ''

h = [s for s in sources]
seen = set()
while h:
    h.sort(key=lambda x: (i.get(x, 0), x))
    for w in work:
        if w[1] == 0 and h:
            if h:
                work[i][0] = h[0]
                work[i][1] = 60 + ord(h[0]) - (ord('A') - 1)
    head = h[0]
    h = h[1:]
    if head in seen:
        continue
    seen.add(head)

    l += head
    for node in v[head]:
        i[node] -= 1
        h.append(node)
print(l)
