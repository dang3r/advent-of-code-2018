from collections import namedtuple

Rectangle = namedtuple('Rectangle', ['id', 'x', 'y', 'x_len', 'y_len'])

def rectangles(filename='03_input.txt'):
    for line in open(filename):
        tokens = line.strip().split(' ')
        x, y = [int(f) for f in tokens[2][:-1].split(',')]
        x_len, y_len = [int(f) for f in tokens[3].split('x')]
        yield Rectangle(tokens[0][1:], x, y, x_len, y_len)

rects = list(rectangles())
collide = set()
first = {}
count = {}
for r in rects:
    for i in range(r.x, r.x + r.x_len):
        for j in range(r.y, r.y + r.y_len):
            if i not in count:
                count[i] = {}
                first[i] = {}
            if j in count[i]:
                collide.add(r.id)
                collide.add(first[i][j])
            else:
                first[i][j] = r.id
            count[i][j] = count[i].get(j, 0) + 1

claimed = 0
for x in count.keys():
    for y, total_count in count[x].items():
        if total_count > 1:
            claimed += 1
print(claimed)
print(set([r.id for r in rects]) - collide)
