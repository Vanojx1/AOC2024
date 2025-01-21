def main(day_input):
    farm_map = {(y, x): r for y, row in enumerate(day_input) for x, r in enumerate(row)}

    def walk(pos):
        region = farm_map[pos]
        dir_list = [(-1,0), (0,1), (1,0), (0,-1)]
        dir_l = 'URDL'
        q = [pos]
        visited = set([pos])
        perimeter = set([])
        while q:
            cy, cx = q.pop(0)
            for (yd, xd), dl in zip(dir_list, dir_l):
                n_pos = (cy+yd, cx+xd)
                p_key = (*n_pos, dl)
                if n_pos in farm_map:
                    if farm_map[n_pos] == region:
                        if n_pos not in visited:
                            visited.add(n_pos)
                            q.append(n_pos)
                    else: perimeter.add(p_key)
                else: perimeter.add(p_key)
        return visited, perimeter

    total_price = 0
    total_price_2 = 0
    total_visited = set([])
    for k in farm_map.keys():
        if k in total_visited: continue
        area, perimeter = walk(k)
        total_visited |= area
        total_price += len(area)*len(perimeter)

        side_r = set([])
        sides = 0
        for y, x, d in sorted(perimeter):
            if (y, x, d) in side_r: continue
            sides += 1
            side_r.add((y, x, d))
            if d in 'UD':
                cx = x-1
                while (y, cx, d) in perimeter:
                    side_r.add((y, cx, d))
                    cx -= 1
                cx = x+1
                while (y, cx, d) in perimeter:
                    side_r.add((y, cx, d))
                    cx += 1
            elif d in 'RL': 
                cy = y-1
                while (cy, x, d) in perimeter:
                    side_r.add((cy, x, d))
                    cy -= 1
                cy = y+1
                while (cy, x, d) in perimeter:
                    side_r.add((cy, x, d))
                    cy += 1
        total_price_2 += len(area)*sides

    return total_price, total_price_2