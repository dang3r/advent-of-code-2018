import re



lines = open('10_input.txt').readlines()
p = []
for line in lines:
    m = re.match(r'^position=<\s*(-?\d+),\s*(-?\d+)> velocity=<\s*(-?\d+),\s*(-?\d+)>$', line)
    p.append(tuple(map(int, m.groups())))

threshold = 15

def check_grid(p):
    min_y = min(p, key=lambda x: x[1])[1]
    max_y = max(p, key=lambda x: x[1])[1]
    diff = abs(max_y - min_y) + 1
    if diff <= threshold:
        return True
    return False


def print_grid(p):
    min_y = min(p, key=lambda x: x[1])[1]
    max_y = max(p, key=lambda x: x[1])[1]
    min_x = min(p, key=lambda x: x[0])[0]
    max_x = max(p, key=lambda x: x[0])[0]
    s = { (x, y) for x, y, _, _ in p}

    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (x,y) in s:
                print('#',end='')
            else:
                print('.', end='')
        print()

cnt = 0
while True:
    if check_grid(p):
        print_grid(p)
        print(cnt)
        break
    for i, point in enumerate(p):
        p[i] = (point[0] + point[2], point[1] + point[3], point[2], point[3])
    cnt += 1