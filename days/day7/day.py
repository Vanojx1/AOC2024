import re
from functools import reduce
from operator import mul, add
from itertools import product

def main(day_input):
    def concat(a, b):
        return int(str(a)+str(b))

    def calibration(operators):
        total = 0
        for row in day_input:
            (t, nums), = re.findall(r'(\d+): ((?:\d+ ?)+)', row)
            t, nums = int(t), [int(n) for n in nums.split(' ')]
            for ops in product(operators, repeat=len(nums)-1):
                i_nums = list(enumerate(nums))
                _, r = reduce(lambda c,n: (n[0], ops[c[0]](c[1], n[1])),i_nums[1:], i_nums[0])
                if r == t:
                    total += r
                    break
        return total

    return calibration((add, mul)), calibration((add, mul, concat))