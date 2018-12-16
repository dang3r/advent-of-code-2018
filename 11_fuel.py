magic = 5235

width = 300
height = 300
box_width = 3

def power(x, y, magic):
    rack_id = (x) + 10
    power = rack_id * y
    power += magic
    power *= rack_id
    h = (power // 100) % 10
    return h - 5

# Populate grid
grid = [[0] * width for _ in range(height)]
for y in range(0, height):
    for x in range(0, width):
        grid[y][x] = power(x + 1, y + 1, magic)

# Part 1
coords = None
max_power = 0
for y in range(0, height - box_width + 1):
    for x in range(0, width - box_width + 1):
        p = sum(grid[y][x:x+box_width])
        p += sum(grid[y+1][x:x+box_width])
        p += sum(grid[y+2][x:x+box_width])
        if p > max_power:
            max_power = p
            coords = (x + 1, y + 1)
print(coords, max_power)

# Part 2
def grid_edge_sum(grid, x, y, width):
    s = 0
    # Bottom Row
    s += sum(grid[y + width - 1][x:x+width])
    # Right Column
    for _y in range(y, y + width):
        s += grid[_y][x + width - 1]
    # Rm bottom right corner
    s -= grid[x + width -1][y + width - 1]
    return s

def box_sum(grid):
    max_g_sum = 0
    c = None

    for y in range(0, height):
        for x in range(0, width):
            box_width = min(height - y, width - x)
            prev = 0
            for w in range(1, box_width + 1):
                box_sum = prev + grid_edge_sum(grid, x, y, w)
                prev = box_sum
                if box_sum > max_g_sum:
                    max_g_sum = box_sum
                    c = (x + 1, y + 1, w)
    return c

print(box_sum(grid))