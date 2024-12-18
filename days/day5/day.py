import re, sys
from collections import defaultdict
from functools import cmp_to_key

def main(day_input):
    full_day_input = '\n'.join(day_input)
    rules = [tuple(int(p) for p in r.split('|')) for r in re.findall(r'\d+\|\d+', full_day_input)]
    updates = [list(map(int, u.split(','))) for u in re.findall(r'^(?:\d+,?)+$', full_day_input, re.MULTILINE)]

    lowers = defaultdict(lambda: set([]))
    for p1, p2 in rules:
        lowers[p2].add(p1)

    def validate(update):
        for p1, p2 in rules:
            if p1 in update and p2 in update:
                if update.index(p1) > update.index(p2):
                    return False
        return True

    def cmp(p1, p2):
        if p1 in lowers[p2]: return -1
        return 1

    middle_sum = 0
    middle_sum_sorted = 0
    for update in updates:
        if validate(update):
            middle_sum += update[len(update)//2]
        else:
            u_sorted = sorted(update, key=cmp_to_key(cmp))
            middle_sum_sorted += u_sorted[len(u_sorted)//2]

    return middle_sum, middle_sum_sorted