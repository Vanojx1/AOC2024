import re

def main(day_input):
    hd = day_input[0]

    disc = [n for i, (file, sp) in enumerate(re.findall(r"(\d)(\d)?", hd)) for n in ([i]*int(file) + [-1]*int(sp or 0))]
    last_id = max(disc)

    left_i = 0
    right_i = len(disc)-1

    while True:
        if disc[left_i] == -1:
            while True:
                if disc[right_i] != -1:
                    disc[left_i] = disc[right_i]
                    disc[right_i] = -1
                    right_i -= 1
                    break
                right_i -= 1
                if right_i == left_i: break
        left_i += 1
        if right_i == left_i: break

    checksum = sum(i*n for i, n in enumerate(disc) if n != -1)

    disc = '|'.join([str(n) for i, (file, sp) in enumerate(re.findall(r"(\d)(\d)?", hd)) for n in ([i]*int(file) + ['S']*int(sp or 0))])

    while last_id > 0:
        block_m = re.search(re.compile(f'({last_id}\|)*{last_id}'), disc)
        block_s = block_m.start()
        block_l = block_m.group().count(str(last_id))
        av_space = re.search(re.compile(f"(?:S\|){{{block_l-1}}}S"), disc)
        if av_space and av_space.start() < block_s:
            disc = re.sub(str(last_id), 'S', disc)
            disc = disc[:av_space.start()] + block_m.group() + disc[av_space.end():]
        last_id -= 1

    checksum_2 = sum(i*int(n) for i, n in enumerate(disc.split('|')) if n != 'S')

    return checksum, checksum_2

    