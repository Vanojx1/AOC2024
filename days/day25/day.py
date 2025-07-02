def main(day_input):
    locks = [[]]
    keys = [[]]

    is_lock = None
    for i, row in enumerate(day_input):
        if is_lock is None:
            if row[0] == '#': is_lock = True
            else: is_lock = False

        if row == '':
            if is_lock: locks.append([])
            else: keys.append([])
            is_lock = None
        elif is_lock: locks[-1].append(row)
        else: keys[-1].append(row)
    
    if locks[-1] == []: locks.pop()
    elif keys[-1] ==[]: keys.pop()

    n_locks = []
    for lock in locks:
        n_locks.append([[lock[row][col] for row in range(7)].count('#')-1 for col in range(5)])

    n_keys = []
    for key in keys:
        n_keys.append([[key[row][col] for row in range(7)].count('#')-1 for col in range(5)])

    fit = 0
    for n_lock in n_locks:
        for n_key in n_keys:
            if all(l+k <= 5 for l, k in zip(n_lock, n_key)):
                fit += 1

    return fit, None