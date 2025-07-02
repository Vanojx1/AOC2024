import re
from collections import defaultdict
from operator import __and__, __xor__, __or__
from functools import partial

def main(day_input):
    
    gates = defaultdict(int)
    links = defaultdict(list)
    connections = []
    wire_map = {}
    for row in day_input:
        if m := re.match(r'(\w\d+): (\d)', row):
            gate, value = m.groups(1)
            gates[gate] = int(value) 
        elif m := re.match(r'(\w+) (\w+) (\w+) -> (\w+)', row):
            g1, op, g2, out = m.groups(1)
            wire_map[out] = (op, g1, g2)
            connections.append((g1, op, g2, out))
            links[g1].append(len(connections)-1)
            links[g2].append(len(connections)-1)

    op_map = {
        'AND': lambda o: __and__(*o),
        'XOR': lambda o: __xor__(*o),
        'OR': lambda o: __or__(*o)
    }

    def apply(g1, op, g2, out):
        # print(f'Run {g1}:{gates[g1]} - {op} - {g2}:{gates[g2]} = {out}:{op_map[op]((gates[g1], gates[g2]))}')
        old_v = gates[out]
        gates[out] = op_map[op]((gates[g1], gates[g2]))
        if old_v != gates[out]: propagate(out)

    def propagate(g):
        for l in links[g]: apply(*connections[l])

    [apply(*c) for c in connections]

    num = ''.join([str(v) for k, v in sorted(gates.items(), key=lambda x: x[0], reverse=True) if k[0] == 'z'])

    # https://github.com/mgtezak/Advent_of_Code/blob/master/2024/24/p2.py

    def make_wire(char: str, i: int) -> str:
        return f'{char}{i:02}'

    make_x, make_y, make_z = [partial(make_wire, char) for char in 'xyz']

    null_values = {}
    for i in range(45):
        null_values[make_x(i)] = 0
        null_values[make_y(i)] = 0

    def init_values(i: int, x: int, y: int, carry: int) -> dict:
        x_values = {
            make_x(i): x, 
            make_x(i-1): carry
        }
        y_values = {
            make_y(i): y, 
            make_y(i-1): carry
        }
        return null_values | x_values | y_values

    operators = {
        'AND': __and__,
        'XOR': __xor__,
        'OR': __or__
    }

    def get_value(wire: str, values: dict) -> int:
        if wire in values:
            return values[wire]
        op, in1, in2 = wire_map[wire]
        values[wire] = operators[op](get_value(in1, values), get_value(in2, values))
        return values[wire]

    def find_wire(op1: str, ins1: set[str]) -> str | None:
        for out, (op2, *ins2) in wire_map.items():
            if op1 == op2 and ins1.issubset(set(ins2)):
                return out

    def fix_bit(i: int) -> set[str]:
        curr_x, curr_y = make_x(i), make_y(i)
        prev_x, prev_y = make_x(i-1), make_y(i-1)
        curr_xor = find_wire('XOR', {curr_x, curr_y})
        prev_xor = find_wire('XOR', {prev_x, prev_y})
        direct_carry = find_wire('AND', {prev_x, prev_y})
        recarry = find_wire('AND', {prev_xor})
        carry = find_wire('OR', {direct_carry, recarry})
        z = find_wire('XOR', {curr_xor, carry})
        if z is None:
            z_ins = set(wire_map[make_z(i)][1:])
            print(z_ins,curr_xor, carry)
            w1, w2 = z_ins ^ {curr_xor, carry}
        else:
            w1, w2 = {z, make_z(i)}
        wire_map[w1], wire_map[w2] = wire_map[w2], wire_map[w1]
        return {w1, w2}

    swapped_wires = set()
    for i in range(1, 45):
        if any(
            x ^ y ^ c != get_value(make_z(i), init_values(i, x, y, c))
            for x in range(2)
            for y in range(2)
            for c in range(2) 
        ):
            swapped_wires |= fix_bit(i)

    return int(num, 2), ','.join(sorted(swapped_wires))