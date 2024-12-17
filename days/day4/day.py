def main(day_input):
    H = len(day_input)
    W = len(day_input[0])
    xmas = 0
    x_mas = 0
    for y in range(H):
        for x in range(W):
            if day_input[y][x] == 'X':
                for dy, dx in ((0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)):
                    yids = [y+dy*i for i in range(1,4)]
                    xids = [x+dx*i for i in range(1,4)]
                    if all(0 <= id < H for id in yids) and all(0 <= id < W for id in xids):
                        if ''.join([day_input[y+dy*i][x+dx*i] for i in range(1,4)]) == 'MAS': xmas += 1
            if day_input[y][x] == 'A':
                yids = [y-1, y+1]
                xids = [x-1, x+1]
                if all(0 <= id < H for id in yids) and all(0 <= id < W for id in xids):
                    if ''.join(day_input[y+dy][x+dx] for dy,dx in [(-1, -1), (-1, 1), (1, -1), (1, 1)]) in ('MSMS', 'SSMM', 'SMSM', 'MMSS'):
                        x_mas += 1
    return xmas, x_mas