from collections import defaultdict

def main(day_input):

    def evolve(secret):
        secret = (secret * 64) ^ secret
        secret %= 16777216
        
        secret = (secret // 32) ^ secret
        secret %= 16777216

        secret = (secret * 2048) ^ secret
        secret %= 16777216

        return secret

    tot_b = defaultdict(int)
    def nth_secret(start_s, n):
        secret = start_s
        history = [0,0,0,0]
        seq_h = set([])

        for i in range(n):
            prev_sec = secret
            secret = evolve(secret)
            history.pop(0)
            history.append((secret % 10) - (prev_sec % 10))

            t_history = tuple(history)
            if i >= 3 and t_history not in seq_h:
                tot_b[t_history] += secret % 10
                seq_h.add(t_history)
        
        return secret
    
    return sum(nth_secret(int(s), 2000) for s in day_input), max(tot_b.values())