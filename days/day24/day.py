import re
from collections import defaultdict
from operator import and_, xor, or_

def main(day_input):
    
    gates = defaultdict(int)
    links = defaultdict(list)
    connections = []
    for row in day_input:
        if m := re.match(r'(\w\d+): (\d)', row):
            gate, value = m.groups(1)
            gates[gate] = int(value) 
        elif m := re.match(r'(\w+) (\w+) (\w+) -> (\w+)', row):
            g1, op, g2, out = m.groups(1)
            connections.append((g1, op, g2, out))
            links[g1].append(len(connections)-1)
            links[g2].append(len(connections)-1)

    op_map = {
        'AND': lambda o: and_(*o),
        'XOR': lambda o: xor(*o),
        'OR': lambda o: or_(*o)
    }

    def apply(g1, op, g2, out):
        # print(f'Run {g1}:{gates[g1]} - {op} - {g2}:{gates[g2]} = {out}:{op_map[op]((gates[g1], gates[g2]))}')
        old_v = gates[out]
        gates[out] = op_map[op]((gates[g1], gates[g2]))
        if old_v != gates[out]: propagate(out)

    def propagate(g):
        for l in links[g]: apply(*connections[l])

    [apply(*c) for c in connections]

    for o in sorted(connections, key=lambda x: x[0]):
        print(*o)

    num = ''.join([str(v) for k, v in sorted(gates.items(), key=lambda x: x[0], reverse=True) if k[0] == 'z'])

    return int(num, 2), None