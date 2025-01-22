import re

def main(day_input):

    plays = [{}]
    for row in day_input:
        if m := re.match(r'Button A: X([+-]\d+), Y([+-]\d+)', row):
            plays[-1]['A'] = tuple(map(int, (m.group(1), m.group(2))))
        elif m := re.match(r'Button B: X([+-]\d+), Y([+-]\d+)', row):
            plays[-1]['B'] = tuple(map(int, (m.group(1), m.group(2))))
        elif m := re.match(r'Prize: X=(\d+), Y=(\d+)', row):
            plays[-1]['P'] = tuple(map(int, (m.group(1), m.group(2))))
        else:
            plays.append({})

    def solve(ax, ay, bx, by, px, py, mult=1):
        px += mult
        py += mult
        A = (px*by - py*bx) / (ax*by - ay*bx)
        B = (py - ay * A) / by
        if A.is_integer() and B.is_integer():
            return int(A*3 + B)
        return 0

    total_t = 0
    total_t_2 = 0
    for play in plays:
        px, py = play['P']
        ax, ay = play['A']
        bx, by = play['B']

        # ax A + bx B = px
        # ay A + by B = py

        total_t += solve(ax, ay, bx, by, px, py)
        total_t_2 += solve(ax, ay, bx, by, px, py, 10000000000000)

    return total_t, total_t_2
