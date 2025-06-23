import re

def main(day_input):

    for row in day_input:
        if m := re.match(r'Register A: (\d+)', row):
            RegA = int(m.group(1))
        if m := re.match(r'Register B: (\d+)', row):
            RegB = int(m.group(1))
        if m := re.match(r'Register C: (\d+)', row):
            RegC = int(m.group(1))
        if m := re.match(r'Program: ([\w,]+)', row):
            program = [int(x) for x in m.group(1).split(',')]

    class ChronospatialComputer:

        def __init__(self, program):
            self.registry = {
                'A': RegA,
                'B': RegB,
                'C': RegC,
                'op': 0,
                'out': []
            }
                            
            self.fn_list = ['adv', 'bxl', 'bst', 'jnz', 'bxc', 'out', 'bdv', 'cdv']
            self.program = program
        
        def get_combo(self, n):
            if 0 <= n <= 3: return n
            if n == 4: return self.registry['A']
            if n == 5: return self.registry['B']
            if n == 6: return self.registry['C']
        
        def txt_combo(self, n):
            if 0 <= n <= 3: return n
            if n == 4: return 'REGA'
            if n == 5: return 'REGB'
            if n == 6: return 'REGC'
    
        def adv(self, p):
            self.registry['A'] = self.registry['A'] // (2**self.get_combo(p))
        
        def bxl(self, p):
            self.registry['B'] = self.registry['B'] ^ p
        
        def bst(self, p):
            self.registry['B'] = self.get_combo(p) % 8
        
        def jnz(self, p):
            if self.registry['A'] == 0: return
            self.registry['op'] = p
            return True
        
        def bxc(self, p):
            self.registry['B'] = self.registry['B'] ^ self.registry['C']

        def out(self, p):
            self.registry['out'] += [self.get_combo(p) % 8]
        
        def bdv(self, p):
            self.registry['B'] = self.registry['A'] // (2**self.get_combo(p))
        
        def cdv(self, p):
            self.registry['C'] = self.registry['A'] // (2**self.get_combo(p))
        
        def run(self):
            while self.registry['op'] < len(self.program):
                op_i = self.registry['op']
                if (getattr(self, self.fn_list[self.program[op_i]])(self.program[op_i+1]) is True): continue
                self.registry['op'] += 2
        
        @property
        def output(self):
            return ','.join(map(str, self.registry['out']))


    cpu = ChronospatialComputer(program)
    cpu.run()
    part1 = cpu.output

    RegA = 0
    for i in reversed(range(len(program))):
        RegA <<= 3
        while True:
            cpu = ChronospatialComputer(program)
            cpu.run()
            if cpu.registry['out'] == program[i:]: break
            RegA += 1

    return part1, RegA
