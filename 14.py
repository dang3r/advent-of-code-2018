magic = 440231
magic_str = str(magic)
magic_len = len(magic_str)

def part_1():
    recipes = [3,7]
    elfs = [0, 1]
    while len(recipes) < magic + 10:
        s = sum([recipes[idx] for idx in elfs])
        recipes.extend([int(digit) for digit in str(s)])
        elfs = [(idx + 1 + recipes[idx]) % len(recipes) for idx in elfs]

    print(''.join(map(str, recipes[magic:magic+10])))


def part_2():
    recipes = [3,7]
    elfs = [0, 1]
    cnt = 0

    while True:

        s = sum([recipes[idx] for idx in elfs])
        recipes.extend([int(digit) for digit in str(s)])
        elfs = [(idx + 1 + recipes[idx]) % len(recipes) for idx in elfs]

        new_recipes= str(s)
        if len(recipes) % 100000 == 0:
            print(len(recipes), cnt)
        for i, r in enumerate(new_recipes):
            if magic_str[cnt] == r:
                cnt += 1
            elif magic_str[0] == r:
                cnt = 1
            else:
                cnt = 0

            if cnt == magic_len:
                print(len(recipes) - len(new_recipes) + i - magic_len + 1)
                return
        

part_1()
part_2()