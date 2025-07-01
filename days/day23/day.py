def main(day_input):
    pairs = sorted(map(lambda r: set(r.split('-')), day_input))

    full = set([])
    for computer in pairs:
        full |= computer

    lan = {}
    for computer in full:
        lan[computer] = set([t for p in pairs for t in p if computer in p and t != computer])

    visited = set([])
    triples = set([])
    largest_lan = tuple()
    def expand(curr_lan):
        nonlocal largest_lan
        t_curr_lan = tuple(curr_lan)

        if t_curr_lan in visited: return
        visited.add(t_curr_lan)

        if len(curr_lan) == 3:
            triples.add(t_curr_lan)
        
        if len(curr_lan) > len(largest_lan):
            largest_lan = t_curr_lan
        
        for computer in full:
            if all(computer in lan[l] for l in curr_lan):
                expand(sorted(curr_lan + [computer]))

    for computer in full: expand([computer])

    t_triples = [t for t in triples if any(p[0] == 't' for p in t)]
    password = ','.join(largest_lan)

    return len(t_triples), password
