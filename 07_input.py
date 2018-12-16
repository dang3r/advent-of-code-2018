import heapq

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
j = {**i}
def part_1():
    l = ''
    h = []
    for s in sources:
        heapq.heappush(h, (i.get(s, 0), s))

    seen = set()
    while h:
        count, node = heapq.heappop(h)
        if node in seen:
            continue
        seen.add(node)
        for child in v[node]:
            i[child] -= 1
            heapq.heappush(h, (i[child], child))
        l += node
    print(l)

part_1()
i = j
print(i)
class Elf:
    def __init__(self):
        self.count = 0
        self.node = None
print(sources)
def part_2():
    l = ''
    h = []
    for s in sources:
        heapq.heappush(h, (i.get(s, 0), s))

    elfs = [Elf() for _ in range(5)]
    seen = set()
    cnt = 0
    while h or sum([elf.count for elf in elfs]):
        for idx, elf in enumerate(elfs):
            elf.count = max(elf.count - 1, 0)
            print(cnt, idx, elf.count, elf.node)
            if not elf.count:
                if elf.node:
                    l += elf.node
                    for child in v[elf.node]:
                        i[child] -= 1
                        heapq.heappush(h, (i[child], child))
                    elf.node = None
                while h:
                    count, node = heapq.heappop(h)
                    if node in seen:
                        continue
                    if count:
                        heapq.heappush(h, (count, node))
                        break
                    elf.count = 60 + ord(node) - ord('A') + 1
                    elf.node = node
                    seen.add(node)
                    break
        cnt += 1
    print(cnt)
part_2()
