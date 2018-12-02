from collections import Counter


def box_checksum(box_ids):
    d = {2:0, 3:0}
    for box in box_ids:
        c = Counter(box)
        done = {2:False,3:False}
        for char, count in c.most_common():
            if not done[3] and count == 3:
                done[3] = True
                d[3] += 1
            elif not done[2] and count == 2:
                done[2] = True
                d[2] += 1
            elif count < 2 or (done[2] and done[3]):
                break
    return d[2] * d[3]


def diff(s1, s2):
    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1
    return count

def correct_boxes(box_ids):
    for i in range(len(box_ids) - 1):
        for j in range(i + 1, len(box_ids)):
            if diff(box_ids[i], box_ids[j]) == 1:
                return box_ids[i], box_ids[j]


# Part 1
box_ids = list([line.strip() for line in open('02_input.txt')])
print(box_checksum(box_ids))

# Part 2
b1, b2 = correct_boxes(box_ids)
common = ''.join([b1[i] for i in range(len(b1)) if b1[i] == b2[i]])
print(b1, b2, common)
