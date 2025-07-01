import functools

def main(day_input):
    t_patterns, _, *design_list = day_input
    t_patterns = sorted(t_patterns.split(', '), key=len)

    @functools.lru_cache
    def iter_pattern(d):
        p_count = 0

        if len(d) == 0: return 1

        for t in t_patterns:
            if d.startswith(t):
                p_count += iter_pattern(d[len(t):])
        return p_count

    designs = list(filter(lambda p_inc: p_inc > 0, map(iter_pattern, design_list)))

    return len(designs), sum(designs)