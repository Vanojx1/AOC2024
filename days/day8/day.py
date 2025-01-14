from collections import defaultdict
from itertools import combinations

def main(day_input):
    H = len(day_input)
    W = len(day_input[0])

    antennas = defaultdict(list)

    for y, row in enumerate(day_input):
        for x, v in enumerate(row):
            if v != '.':
                antennas[v].append((y, x))

    def iter_antinodes(p, yd, xd, new_model=False):
        if new_model: yield p
        while True:
            p = (p[0]+yd,p[1]+xd)
            if 0 <= p[0] < H and 0 <= p[1] < W: yield p
            else: break
            if not new_model: break

    def get_antinodes(new_model=False):
        q = set([])
        for _, ants in antennas.items():
            for (y1, x1), (y2, x2) in combinations(ants, 2):
                
                yd = abs(y1-y2)
                xd = abs(x1-x2)

                if y1 > y2:
                    if x1 > x2:
                        # 
                        # p2
                        #    p1
                        #
                        a_nodes = [*iter_antinodes((y1,x1),-yd,-xd, new_model)] + [*iter_antinodes((y2,x2),yd,xd, new_model)]
                    else:
                        # 
                        #    p2
                        # p1  
                        #
                        a_nodes = [*iter_antinodes((y2,x2),-yd,xd, new_model)] + [*iter_antinodes((y1,x1),yd,-xd, new_model)]
                else:
                    if x1 > x2:
                        # 
                        #    p1
                        # p2
                        #
                        a_nodes = [*iter_antinodes((y1,x1),-yd,+xd, new_model)] + [*iter_antinodes((y2,x2),+yd,-xd, new_model)]
                    else:
                        # 
                        # p1
                        #    p2
                        #
                        a_nodes = [*iter_antinodes((y1,x1),-yd,-xd, new_model)] + [*iter_antinodes((y2,x2),+yd,+xd, new_model)]
                q |= set(a_nodes)
        return q

    part1 = get_antinodes()
    part2 = get_antinodes(True)

    return len(part1), len(part2)