from functools import cache

def main(day_input):
    stones = [int(s) for s in day_input[0].split(' ')]

    def arrange(blinks):
        @cache
        def engrave(stone, blink):
            if blink == 0: return 1
            if stone == 0:
                return engrave(1, blink-1)
            elif (st_l := len(str(stone))) % 2 == 0:
                return engrave(int(str(stone)[:st_l//2]), blink-1) + engrave(int(str(stone)[st_l//2:]), blink-1)
            else:
                return engrave(stone * 2024, blink-1)
        return sum(engrave(stone, blinks) for stone in stones) 
    
    return arrange(25), arrange(75)