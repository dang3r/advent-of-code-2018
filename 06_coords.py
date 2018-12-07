coords = [tuple(map(int, line.strip().split(','))) for line in open('06_input.txt').readlines()]

# Part 1
finite = set([i for i in range(len(coords))])
min_x = min(coords, key=lambda c: c[0])[0]
max_x = max(coords, key=lambda c: c[0])[0]
min_y = min(coords, key=lambda c: c[1])[1]
max_y = max(coords, key=lambda c: c[1])[1]
area = {i: 0 for i in range(len(coords))}

def distance(x1, x2, y1, y2):
    return abs(x1 - x2) + abs(y1 - y2)

for x in range(min_x, max_x + 1):
    for y in range(min_y, max_y + 1):
        m = min(coords, key=lambda c: distance(c[0], x, c[1], y))
        min_dist = distance(m[0], x, m[1], y)
        min_coords = [i for i,c in enumerate(coords) if min_dist == distance(c[0], x, c[1], y)]
        if len(min_coords) == 1:
            i = coords.index(m)
            area[i] += 1
            if x == min_x or x == max_x or y == max_y or y == min_y:
                if i in finite:
                    finite.remove(i)

print(max(area.values()))

# Part 2
max_distance = 10000
t = 0
for x in range(min_x, max_x + 1):
    for y in range(min_y, max_y + 1):
        s = sum([distance(c[0], x, c[1], y) for c in coords])
        if s < max_distance:
            t += 1
print(t)
