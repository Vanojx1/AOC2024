import heapq

def main(day_input):

    memory = [(int(x), int(y)) for x, y in map(lambda x: x.split(','), day_input)]

    def d(a, b):
        return abs(a[0]-b[0]) + abs(a[1]-b[1])

    def get_min_steps(curr_memory, mem_size):
        start, stop = (0, 0), (mem_size-1, mem_size-1)
        q = [(0, d(start, stop), *start)]
        heapq.heapify(q)

        visited = set([start])

        while q:

            min_steps, _, cx, cy = q.pop(0)

            if (cx, cy) == stop:
                return min_steps

            for nx, ny in [(cx+ox, cy+oy) for ox, oy in [(1, 0), (0, 1), (-1, 0), (0, -1)]]:
                if 0 <= nx < mem_size and 0 <= ny < mem_size and (nx, ny) not in visited and (nx, ny) not in curr_memory:
                    visited.add((nx, ny))
                    heapq.heappush(q, (min_steps + 1, d((nx, ny), stop), nx, ny))
    
    bytes = 1024
    mem_size = 71

    min_steps = get_min_steps(memory[:bytes], mem_size)

    for i in range(1, len(memory)):
        if get_min_steps(memory[:-i], mem_size):
            x, y = memory[-i]
            not_exit_byte = f'{x},{y}'
            break

    return min_steps, not_exit_byte