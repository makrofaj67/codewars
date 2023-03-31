import math

def proper_fractions(n):
    wanted = []
    for r in range(1, n):
        if math.gcd(r, n) == 1:
            wanted.append(r)       
    return len(wanted)


