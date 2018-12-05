polymer = open('05_input.txt').read().strip()

def reacts(s1, s2):
    return s1 != s2 and (s1.upper() == s2 or s1.lower() == s2)

def react(polymer):
    s = [polymer[0]]
    for i in range(1, len(polymer)):
        if s and reacts(s[-1], polymer[i]):
            s.pop()
        else:
            s.append(polymer[i])
    return ''.join(s)

s = react(polymer)
print(f'Length of reacted default polymer is {len(s)}')

cs = set([c.lower() for c in polymer])
rs = [react(list(polymer.replace(c,'').replace(c.upper(), ''))) for c in cs]
l = min(rs, key=lambda x: len(x))
print(f'Length of shortest polymer with one type removed is {len(l)}')
