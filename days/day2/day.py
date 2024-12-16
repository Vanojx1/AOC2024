from functools import reduce

def main(day_input):
    strict_safe = 0
    safe = 0
    for row in day_input:
        level = [int(n) for n in row.split(' ')]
        
        def validate(level):
            diff_l = reduce(lambda c,n: (c[0]+[c[1]-n], n), level[1:], ([], level[0]))[0]
            N = len(diff_l)
            diff_check = sum(1 <= abs(d) <= 3 for d in diff_l)
            pos_check = sum(d > 0 for d in diff_l)
            neg_check = sum(d < 0 for d in diff_l)
            return diff_check == N and (pos_check == N or neg_check == N)

        if validate(level):
            strict_safe += 1
            safe += 1
        else:
            for i in range(len(level)):
                if validate(level[:i]+level[i+1:]):
                    safe += 1
                    break

    return strict_safe, safe