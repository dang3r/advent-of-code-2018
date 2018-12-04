from datetime import datetime

sample = '[1518-05-13 00:03]'

def records(filename='04_input.txt'):
    for line in open(filename):
        line = line.strip()
        d = datetime.strptime(line[1:len(sample) - 1], '%Y-%m-%d %H:%M')
        cmd = line[len(sample) + 1:]
        yield (d, cmd)

r = sorted(list(records()), key=lambda r: r[0])
d = {}
def fill(gid, start, end):
    if gid not in d:
        d[gid] = {}
    for i in range(start, end+1):
        d[gid][i] = d[gid].get(i, 0) + 1

gid = None
guard_begins = lambda x: x[0] == 'G'
wakes_up = lambda x: x[0] == 'w'
falls_asleep = lambda x: x[0] == 'f'

for i in range(len(r)):
    date, event = r[i]
    if guard_begins(event):
        gid = int(event.split(' ')[1][1:])
    elif wakes_up(event):
        p_date, p_event = r[i-1]
        fill(gid, p_date.time().minute, date.time().minute - 1)

best_gid = max(d.keys(), key=lambda gid: sum(d[gid].values()))
best_min = max(d[best_gid].keys(), key=lambda minute: d[best_gid][minute])
print(best_gid, best_min, best_gid * best_min)

most = max(d, key=lambda gid: max(d[gid].values()))
print(most, max(d[most], key=lambda time:d[most][time]))
