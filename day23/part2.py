from queue import PriorityQueue


slot_pos = ['A', 'B', 'C', 'D']
s_cost = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000
}
slot_caps = {2, 4, 6, 8}


def h(slots, hall):
    n = 0
    for i, s in enumerate(slots):
        for j, spot in enumerate(s):
            if spot is not None and slot_pos[i] != spot:
                n += (abs(slot_pos.index(spot) - i) * 2 + 1 + j) * s_cost[spot]
                #print(i, spot, n)
    for i, snail in enumerate(hall):
        if snail is not None:
            n += (abs(i - (slot_pos.index(snail) + 1) * 2) + 1) * s_cost[snail]
    return n


def upd_hall(hall, changes):
    new_hall = list(hall)
    for i, ch in changes:
        new_hall[i] = ch
    return tuple(new_hall)


def upd_slots(slots, i, j, ch):
    new_slots = [list(slot) for slot in slots]
    new_slots[i][j] = ch
    return tuple(tuple(s) for s in new_slots)


def blocked(hall, src, dst):
    dst = (dst + 1) * 2
    if src > dst:
        for h in hall[dst:src]:
            if h is not None:
                return True
    elif src < dst:
        for h in hall[src + 1: dst + 1]:
            if h is not None:
                return True
    return False


def hall_dist(i, j):
    return max(i, j) - min(i, j)


def find_slot(slots, hall, i, snail):
    index = slot_pos.index(snail)
    if not blocked(hall, i, index):
        lastgood = None
        frozen = False
        for slot_i, slot in enumerate(slots[index]):
            if slot is None:
                if frozen:
                    return None
                lastgood = slot_i
            elif slot != snail:
                return None
            elif lastgood is None:
                return None
            else:
                frozen = True
        new_hall = upd_hall(hall, [(i, None)])
        new_slots = upd_slots(slots, index, lastgood, snail)
        dist = abs(i - (index + 1) * 2) + 1 + lastgood
        return (new_slots, new_hall, dist * s_cost[snail])


def find_hall(slots, hall, i, j, snail):
    hidx = (i + 1) * 2
    changes = []
    for index in range(hidx, -1, -1):
        if hall[index] is not None:
            break
        if index in slot_caps:
            continue
        new_slots = upd_slots(slots, i, j, None)
        new_hall = upd_hall(hall, [(index, snail)])
        dist = abs(index - hidx) + j + 1
        changes.append((new_slots, new_hall, dist * s_cost[snail]))
    for index in range(hidx, len(hall)):
        if hall[index] is not None:
            break
        if index in slot_caps:
            continue
        new_slots = upd_slots(slots, i, j, None)
        new_hall = upd_hall(hall, [(index, snail)])
        dist = abs(index - hidx) + j + 1
        changes.append((new_slots, new_hall, dist * s_cost[snail]))
    return changes


def upd_sl(slots, new_sl, i):
    new_slots = []
    for j, slot in enumerate(slots):
        if j == i:
            new_slots.append(new_sl)
        else:
            new_slots.append(slot)
    return tuple(new_slots)


def poss_changes(slots, hall):
    changes = []
    for i, snail in enumerate(hall):
        if snail is not None:
            sl = find_slot(slots, hall, i, snail)
            if sl:
                changes.append(sl)
    for i, s in enumerate(slots):
        for j, slot in enumerate(s):
            if slot is not None:
                changes.extend(find_hall(slots, hall, i, j, slot))
                break
    return changes


def print_past(past):
    for slots, hall, cost in past:
        print(slots, hall, cost)


good = (
    ('A', 'A', 'A', 'A'),
    ('B', 'B', 'B', 'B'),
    ('C', 'C', 'C', 'C'),
    ('D', 'D', 'D', 'D'),
)


def solve(input_list: list):
    slots = (('D', 'D', 'D', 'B'), ('D', 'C', 'B', 'A'),
             ('C', 'B', 'A', 'A'), ('B', 'A', 'C', 'C'))  # input
    #slots = (('B', 'D', 'D', 'A'), ('C', 'C', 'B', 'D'),
    #         ('B', 'B', 'A', 'C'), ('D', 'A', 'C', 'A'))  # sample
    #slots = (('B', 'A'), ('C', 'D'), ('B', 'C'), ('D', 'A'))  # sample
    #slots = (
    #    ('B', 'B', 'A', 'A'),
    #    ('A', 'A', 'B', 'B'),
    #    ('C', 'C', 'C', 'C'),
    #    ('D', 'D', 'D', 'D'),
    #)
    q = PriorityQueue()
    hall = tuple([None] * 11)
    states = {0: (slots, hall, 0, [])}
    stct = 1
    q.put((h(slots, hall), 0))
    passed = set()
    thresh = 0
    while q:
        x, i = q.get()
        slots, hall, cost, past = states[i]
        #if hall[0] == 'A':
            #print(x, slots, hall, cost)
        states.pop(i)
        if cost > thresh:
            print(x, slots, hall, cost)
            thresh += 100
        if (slots, hall) in passed:
            continue
        if h(slots, hall) == 0:
            print(x, slots, hall)
            print_past(past)
            return cost
        passed.add((slots, hall))
        for ns, nh, nc in poss_changes(slots, hall):
            if (ns, nh) not in passed:
                #if nh[1] == 'A' and nh[3] == 'B' and nh[5] == 'A':
                    #print(ns, nh, nc, cost, h(ns, nh))
                    #print(slots, hall, cost, past)
                states[stct] = (ns, nh, cost + nc, past + [(slots, hall, cost)])
                q.put((cost + nc + h(ns, nh), stct))
                stct += 1
    raise 'NONONONONON'


if __name__ == '__main__':
    print(solve([]))
    #print(push_down(('B', None, None, 'B'), 1))
