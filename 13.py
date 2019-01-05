cart_symbols = set('^><v')
vertical_symbols = set('|' )
horizontal_symbols = set('<>')
corner_symbols = set('/\\')

class Cart:
    move = {
        '^': (-1, 0),
        '>': (0, 1),
        'v': (1, 0),
        '<': (0, -1)
    }
    corner_rules = {
        '>':{'/': '^', '\\': 'v'},
        '^':{'/': '>', '\\': '<'},
        '<':{'/': 'v', '\\': '^'},
        'v':{'/': '<', '\\': '>'},
    }
    order = list('<^>v')

    def __init__(self, y, x, symb):
        self.y = y
        self.x = x
        self.symbol = symb
        self.count = 0

    def __repr__(self):
        return f'({self.x}, {self.y}, {self.symbol})'

    def walk(self, tracks):
        # Determine direction if on an intersection
        if tracks[self.y][self.x] == '+':
            i = self.order.index(self.symbol)
            if self.count == 0:
                self.symbol = self.order[i-1]
            elif self.count == 2:
                self.symbol = self.order[(i+1) % 4]
            self.count = (self.count + 1) % 3

        # Apply move.
        v_y, v_x = self.move[self.symbol]
        self.y += v_y
        self.x += v_x
        point = tracks[self.y][self.x]

        # If on a corner, change the symbol orientation
        if point in corner_symbols:
            self.symbol = self.corner_rules[self.symbol][point]


def starting_carts(tracks):
    carts = []
    for y, track in enumerate(tracks):
        for x, char in enumerate(track):
            if char in cart_symbols:
                carts.append(Cart(y, x, char))
                tracks[y][x] = '-' if char in horizontal_symbols else '|'
    return carts


def walk(tracks, carts):
    count = 0
    while True:
        if len(carts) == 1:
            print(carts)
            break

        crashed = set()
        for cart in sorted(carts, key= lambda c: (c.y, c.x)):
            cart.walk(tracks)

            # Detect collisions with other carts
            collisions = set([c for c in carts if (c.x, c.y) == (cart.x, cart.y)])
            if len(collisions) > 1:
                for collided_cart in collisions:
                    crashed.add(collided_cart)
                print(count, collisions)

        carts = list(set(carts) - crashed)
        count += 1


def print_tracks(tracks, carts):
    l = [['' for _ in tracks[0]] for _ in tracks]
    for c in carts:
        l[c.y][c.x] = c.symbol
    for i, track in enumerate(tracks):
        for j, _ in enumerate(track):
            l[i][j] = tracks[i][j] if l[i][j] == '' else l[i][j]
    print('\n'.join([''.join(line) for line in l]))
    print()


tracks = [list(line[:-1]) for line in open('13.txt')]
carts = starting_carts(tracks)
print(carts)
walk(tracks, carts)