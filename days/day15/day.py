def main(day_input):
    i = day_input.index('')
    warehouse = day_input[:i]
    moves = list(''.join(day_input[i+1:]))

    walls = set([])
    boxes = set([])
    for y in range(len(warehouse)):
        for x in range(len(warehouse)):
            if warehouse[y][x] == '#': walls.add((x, y))
            elif warehouse[y][x] == 'O': boxes.add((x, y))
            elif warehouse[y][x] == '@': curr_pos = (x, y)

    d_off = {'<': (-1, 0), '^': (0, -1), '>': (1, 0), 'v': (0, 1)}
    cx, cy = curr_pos
    for m in moves:        
        nx, ny = map(sum, zip([cx, cy], d_off[m]))
        if (nx, ny) in walls: continue
        if (nx, ny) in boxes:
            to_push = set([(nx, ny)])
            zx, zy = map(sum, zip([nx, ny], d_off[m]))
            while (zx, zy) in boxes:
                to_push.add((zx, zy))
                zx, zy = map(sum, zip([zx, zy], d_off[m]))
            if (zx, zy) in walls: continue
            else:
                pushed = set([tuple(map(sum, zip(tp, d_off[m]))) for tp in to_push])
                boxes -= to_push
                boxes |= pushed
        cx, cy = nx, ny
    
    p1_final = boxes

    v_map = {'#': '##', 'O': '[]', '.': '..', '@': '@.'}
    warehouse = [list(''.join([v_map[v] for v in row])) for row in warehouse]

    walls = set([])
    boxes = {}
    boxes_id = {}
    box_c = 0

    for y in range(len(warehouse)):
        for x in range(len(warehouse[0])):
            if warehouse[y][x] == '#': walls.add((x, y))
            elif warehouse[y][x] == '[':
                boxes[(x, y)] = box_c
                boxes[(x+1, y)] = box_c
                boxes_id[box_c] = [(x, y), (x+1, y)]
                box_c += 1
            elif warehouse[y][x] == '@': curr_pos = (x, y)
    cx, cy = curr_pos

    def propagate_push(box_id, d):
        nboxes = [tuple(map(sum, zip(box, d))) for box in boxes_id[box_id]]
        if any(b in walls for b in nboxes): return {-1: None}
        
        new_boxes = {}
        for b in nboxes:
            if b in boxes and boxes[b] != box_id:
                new_boxes = {**new_boxes, **propagate_push(boxes[b], d)}
        
        return {box_id: nboxes, **new_boxes}

    for m in moves:
        nx, ny = map(sum, zip([cx, cy], d_off[m]))
        if (nx, ny) in walls: continue
        if (nx, ny) in boxes:
            new_boxes = propagate_push(boxes[(nx, ny)], d_off[m])

            if -1 in new_boxes: continue

            for nb_id, ((nx1, ny1), (nx2, ny2)) in new_boxes.items():
                for b in boxes_id[nb_id]: del boxes[b]
            
            for nb_id, ((nx1, ny1), (nx2, ny2)) in new_boxes.items():
                boxes[(nx1, ny1)] = nb_id
                boxes[(nx2, ny2)] = nb_id
                boxes_id[nb_id] = [(nx1, ny1), (nx2, ny2)]

        cx, cy = nx, ny
    p2_final = map(lambda b: (min(b[0][0], b[1][0]), b[0][1]), boxes_id.values())
 
    return sum([x+y*100 for x, y in p1_final]), sum([x+y*100 for x, y in p2_final])