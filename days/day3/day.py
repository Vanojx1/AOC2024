import re

def main(day_input):
    program, = day_input
    total = 0
    for n1, n2 in re.findall(r'mul\((\d+),(\d+)\)', program):
        total += int(n1)*int(n2)

    total_do_dont = 0
    for m in re.findall(r"^.*?don't\(\)|do\(\).*?don't\(\)|do\(\).*?$", program):
        for n1, n2 in re.findall(r'mul\((\d+),(\d+)\)', m):
            total_do_dont += int(n1)*int(n2)
    return total, total_do_dont