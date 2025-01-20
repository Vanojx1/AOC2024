def main(day_input):
    trail_map = {}
    trailheads = []
    for y, row in enumerate(day_input):
        for x, h in enumerate(row):
            if h == '.': continue
            if h == '0': trailheads.append((y, x))
            trail_map[(y, x)] = int(h)

    dir_list = [(-1,0), (0,1), (1,0), (0,-1)]
    total_score = 0
    for t_head in trailheads:
        q = [t_head]
        visited = set([t_head])
        while q:
            cy, cx = q.pop(0)
            if trail_map[(cy, cx)] == 9: total_score += 1

            for yd, xd in dir_list:
                n_pos = (cy+yd, cx+xd)
                if n_pos in trail_map and n_pos not in visited and trail_map[n_pos] - trail_map[(cy, cx)] == 1:
                    visited.add(n_pos)
                    q.append(n_pos)

    rating = 0
    for t_head in trailheads:
        def walk(cy, cx, curr_path):
            nonlocal visited, rating
            if trail_map[(cy, cx)] == 9: rating += 1

            for yd, xd in dir_list:
                n_pos = (cy+yd, cx+xd)
                if n_pos in trail_map and n_pos not in curr_path and trail_map[n_pos] - trail_map[(cy, cx)] == 1:
                    walk(*n_pos, curr_path + [n_pos])
        walk(*t_head, [t_head])

    return total_score, rating