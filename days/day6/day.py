def main(day_input):
    H = len(day_input)
    W = len(day_input[0])
    obstructions = set([])
    for y, row in enumerate(day_input):
        for x, v in enumerate(row):
            if v == '#':
                obstructions.add((y, x)) 
            elif v == '^':
                guard = (y, x)

    dirs = [(-1,0), (0,1), (1,0), (0,-1), (-1,0)]
    
    def check_loop(obs_check):
        c_dir, curr = (-1, 0), guard
        history = set([c_dir, curr])
        while True:
            ny, nx = map(sum, zip(curr, c_dir))
            if (c_dir, (ny, nx)) in history: return 1
            if ny < 0 or ny == H or nx < 0 or nx == W: return 0
            if (ny, nx) in obstructions or (ny, nx) == obs_check:
                c_dir = dirs[dirs.index(c_dir)+1]
                continue
            curr = (ny, nx)
            history.add((c_dir, (ny, nx)))

    c_dir, curr = (-1, 0), guard
    visited = set([guard])
    total_loop = 0
    while True:
        ny, nx = map(sum, zip(curr, c_dir))
        if ny < 0 or ny == H or nx < 0 or nx == W: break
        if (ny, nx) in obstructions:
            c_dir = dirs[dirs.index(c_dir)+1]
            continue
        curr = (ny, nx)
        visited.add(curr)

    for v in visited:
        if v == guard: continue
        total_loop += check_loop(v)

    return len(visited), total_loop