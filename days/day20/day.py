import heapq

def main(day_input):

    track = set([])
    for y, row in enumerate(day_input):
        for x, v in enumerate(row):
            if v in 'SE.': track.add((x, y))
            if v == 'S': start = (x, y)
            if v == 'E': end = (x, y)

    def get_min_steps():
        q = [(0, *start)]
        heapq.heapify(q)

        visited = [start]

        while q:
            min_steps, cx, cy = q.pop(0)

            if (cx, cy) == end:
                return visited

            for nx, ny in [(cx+ox, cy+oy) for ox, oy in [(1, 0), (0, 1), (-1, 0), (0, -1)]]:
                if (nx, ny) in track and (nx, ny) not in visited:
                    visited.append((nx, ny))
                    heapq.heappush(q, (min_steps + 1, nx, ny))


    path = get_min_steps()

    def cheat(max_cheat):
        for t1, (x1, y1) in enumerate(path):
            for t2 in range(t1 + 3, len(path)):
                x2, y2 = path[t2]
                d = abs(x1-x2) + abs(y1-y2)
                if d <= max_cheat and t2 - t1 > d:
                    yield t2 - t1 - d

    return sum(saved >= 100 for saved in cheat(2)), sum(saved >= 100 for saved in cheat(20))