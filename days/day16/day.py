import heapq

def main(day_input):

    maze = set([])
    for y, row in enumerate(day_input):
        for x, v in enumerate(row):
            if v in 'SE.': maze.add((x, y))
            if v == 'S': start = (x, y)
            if v == 'E': end = (x, y)

    d_map = {0: ( 1, 0), 
             1: ( 0, 1), 
             2: (-1, 0),
             3: ( 0,-1)}
    d_turn = {0: [3, 1],
              1: [2, 0],
              2: [1, 3],
              3: [0, 2]}

    q = [(0, 0, *start, [start])]
    visited = set([(0, *start)])
    heapq.heapify(q)

    min_score = None
    good_spots = set([])

    while q:
        c_score, c_dir, cx, cy, spots = heapq.heappop(q)

        if min_score is not None and c_score > min_score: continue

        if (cx, cy) == end:
            if c_score == min_score or min_score is None:
                good_spots |= set(spots)
            min_score = c_score
        
        visited.add((c_dir, cx, cy))

        nx, ny = map(sum, zip((cx, cy), d_map[c_dir]))
        if (nx, ny) in maze and (c_dir, nx, ny) not in visited:
            heapq.heappush(q, (c_score + 1, c_dir, nx, ny, spots + [(nx, ny)]))
            
        for n_dir in d_turn[c_dir]:
            nx, ny = map(sum, zip((cx, cy), d_map[n_dir]))
            if (nx, ny) in maze and (n_dir, nx, ny) not in visited:
                heapq.heappush(q, (c_score + 1001, n_dir, nx, ny, spots + [(nx, ny)]))

    return min_score, len(good_spots)